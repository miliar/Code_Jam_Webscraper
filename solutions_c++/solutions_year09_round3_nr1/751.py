#include <stdio.h>
#include <stdlib.h>
#include <string.h>
long long ans;
long long at;
long long tep;
long long kel;
char A[100];
int C[200];
char max=0;
main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
int t;
int len;
int tmp;
scanf("%d\n",&t);
for(int i=1;i<=t;i++)
{
 max=0;
 ans=0;
 gets(A);
 len=strlen(A);
 for(int j=0;j<=199;j++)
 {
 C[j]=0;
 }
 for(int j=0;j<len;j++)
 {
  if(C[A[j]]==0)
  {
  C[A[j]]=max+1;max++;
  if(C[A[j]]>2){A[j]=C[A[j]]-1;}
  else if(C[A[j]]==2){A[j]=0;}
  else{A[j]=1;}
  }
  else
  {
  if(C[A[j]]>2){A[j]=C[A[j]]-1;}
  else if(C[A[j]]==2){A[j]=0;}
  else{A[j]=1;}
  }
 }
 at=1;
 if(max==1){max++;}
 for(int j=len-1;j>=0;j--)
 {
 tmp=A[j];
 //printf("%d",tmp);
 ans+=(long long) tmp*at;
 at=(long long) at*max;

 }
 printf("Case #%d: %I64d\n",i,ans);
 //printf("Base %d\n",max);
}
return 0;
}
