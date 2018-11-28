#include <stdio.h>
#include <stdlib.h>
int t;
int r;
int n;
long long k; 
long long A[1001];
int go[1001];
long long cost[1001];
long long ans;
int at;
main()
{
 freopen("C-large.in","r",stdin);
 freopen("C-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d",&r);
  scanf("%I64d",&k);
  scanf("%d",&n);
   for(int j=1;j<=n;j++)
   {
    scanf("%I64d",&A[j]);
   }
   for(int j=1;j<=n;j++)
   {
   cost[j]=0;
    cost[j]=A[j];
    at=j+1;
    if(at>n){at=1;}
    go[j]=at;

    while(cost[j]<=k&&at!=j)
    {
     if(cost[j]+A[at]<=k)
     {
     cost[j]+=A[at];
     at++;
     if(at>n){at=1;}
     go[j]=at;
     }
     else
     {
      break;
     }
    }
  //  printf("%d %I64d\n",go[j],cost[j]);
   }
   at=1;
   ans=0;
   for(int j=1;j<=r;j++)
   {
    ans+=cost[at];
    at=go[at];
   }
   printf("Case #%d: %I64d\n",i,ans);
 }
 return 0;
}

