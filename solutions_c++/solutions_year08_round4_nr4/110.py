#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define lim 1001

int cs,c,k,cnt,mn,i,j,n;
char str[lim],s[lim];
int A[6];

int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d",&k);
	scanf("%s",str);
	n=strlen(str);
	for(i=0;i<k;i++)
	  A[i]=i;
	mn=-1;
	while(1)
	{
	  for(i=0;i<n;i+=k)
	    for(j=0;j<k;j++)
		  s[i+j]=str[i+A[j]];
	  cnt=0;
	  for(i=0;i<n;i++)
	    if(i==0 || s[i]!=s[i-1])
		  cnt++;
	  if(mn==-1)
	    mn=cnt;
	  mn=min(mn,cnt);
	  if(!next_permutation(A,A+k))
	    break;
	}
	printf("Case #%d: %d\n",c+1,mn);
  }
  return 0;
}
