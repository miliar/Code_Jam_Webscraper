/*
 Problem B, Round 1B, Google Code Jam 2009
   Author:   stqhmf
   Language: C++
   Method:   next permutation
 */

#include <cstdio>
#include <algorithm>
#include <cstring>

char number[32];
char buf[32];
int  buf_length;

int main()
{
  int num_cases,cnt,length,i;
  char min;
  int min_pos;
  scanf("%d",&num_cases);
  for ( cnt=1; cnt<=num_cases; ++cnt ) {
    scanf("%s",number);
    length = strlen(number);
    if ( std::next_permutation(number,number+length) )
      printf("Case #%d: %s\n",cnt,number);
    else {
      printf("Case #%d: ",cnt);
      min = 127;
      for ( i=0; i<length; ++i )
	if ( number[i]!='0' && number[i]<min ) {
	  min = number[i];
	  min_pos = i;
	}
      buf_length = 0;
      for ( i=0; i<length; ++i )
	if ( i!=min_pos )
	  buf[buf_length++] = number[i];
      buf[buf_length] = '\0';
      std::sort(buf,buf+buf_length);
      printf("%c0%s\n",min,buf);
    }
  }
}
