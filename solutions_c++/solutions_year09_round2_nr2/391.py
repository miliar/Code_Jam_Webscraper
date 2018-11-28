#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,n,i,j;
bool f;
char str[30],str2[30],res[30];
bool B[257];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%s",str);
	n=strlen(str);
	if(!next_permutation(str,str+n))
	{
	  for(i='1';i<='9';i++)
	    B[i]=1;
	  B['0']=0;
	  str[++n]='\0';
	  f=0;
	  for(i='0';i<='9';i++)
	    if(!B[i])
		{
		  for(j=0;j<=n;j++)
		    str2[j]=str[j];
		  str2[n-1]=i;
		  sort(str2,str2+n);
	      for(j=0;j<n;j++)
	        if(str2[j]!='0')
		      break;
	      swap(str2[j],str2[0]);
		  if(!f || strcmp(str2,res)<0)
		  {
		    f=1;
		    strcpy(res,str2);
		  }
		}
	}
	else
	  strcpy(res,str);
	printf("Case #%d: %s\n",c,res);
  }  
  return 0;
}
