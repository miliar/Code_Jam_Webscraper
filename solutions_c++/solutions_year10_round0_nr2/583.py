#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int t;
int n;
int A[5];
int mods;
int gcds;
int gcd(int a,int b)
{
 if(b==0)
 {
  return a;
 }
 else
 {
  return gcd(b,a%b);
 }
}
main()
{
 freopen("B-small-attempt0.in","r",stdin);
 freopen("B-small-attempt0.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  printf("Case #%d: ",i);
  scanf("%d",&n);
  for(int j=1;j<=n;j++)
  {
   scanf("%d",&A[j]);
  }
  sort(&A[1],&A[n+1]);
  if(n==2)
  {
   mods=A[1]%(A[2]-A[1]);
   if(mods==0){mods=A[2]-A[1];}
   printf("%d\n",(A[2]-A[1])-mods);
  }
  else
  {
   gcds=gcd(A[2]-A[1],A[3]-A[2]);
   mods=A[1]%gcds;
   if(mods==0){mods=gcds;}
   printf("%d\n",gcds-mods);
  }
 }
 return 0; 
}
