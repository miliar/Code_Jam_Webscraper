#include <iostream>
#include <cstdio>
using namespace std;

int main ()
{
  char file[20];
  cin >> file;
  FILE * fp=fopen(file, "r");
  long long int i, j, k, flag, max, n, p, Ti, T;
  char str[100], num[100][2];
  fscanf(fp,"%lld",&T);
  for(Ti=1; Ti<=T; Ti++) {
    fscanf(fp, "%s", str);
    k=0; n=0;
    num[0][0]='\0';
    for(i=0;str[i];i++) {
      flag = 0;
      for(j=0;j<i;j++)
	if(str[i]==str[j])
	  flag = 1;
      if(!flag)
	num[k++][0]=str[i];
    }
    num[k][0]='\0';
    for(i=0;num[i][0];i++) {
      if(i==0)
	num[i][1]='1';
      else if(i==1)
	num[i][1]='0';
      else
	num[i][1]=(i>9)?(i+'a'):(i+'0');
    }
    for(i=0;str[i];i++) {
      for(j=0;num[j][0];j++) 
	if(str[i]==num[j][0]) {
	  str[i]=num[j][1];
	  break;
	}
    }
    max = str[0];
    for(i=0;str[i];i++)
      if(str[i]>max)
	max=str[i];
    p=1;
    for(i=0;str[i];i++);
    for(--i;i>=0;i--) {
      n+=((str[i]>'9')?(str[i]-'a'):(str[i]-'0'))*p;
      p*=((max>'9')?(max-'a'):(max-'0')) + 1;
    }
    cout << "Case #" << Ti << ": " << n << endl;
  }
  return 0;
} 
