#include <stdio.h>
#include <stdlib.h>
int t;
int n;
int dp[50001];
int dist[50001];
int len[50001];
int goals;
bool pri;
int nows;
inline int mins(int a,int b)
{
 if(a<b){return a;}
 else{return b;}
}
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  printf("Case #%d: ",tests);
  scanf("%d",&n);
  for(int i=1;i<=n;i++)
  {
   scanf("%d%d",&dist[i],&len[i]);
   dp[i]=-1;
  }
  pri=false;
  scanf("%d",&goals);
  dp[1]=dist[1];
  for(int i=1;i<=n;i++)
  {
    if(goals<=dist[i]+dp[i]){printf("YES\n");pri=true;break;}
    else
    {
     for(int j=i+1;j<=n;j++)
     {
      if(dist[i]+dp[i]>=dist[j])
      {
       nows=mins(dist[j]-dist[i],len[j]);
       if(nows>dp[j]){dp[j]=nows;}
      }
      else{break;}
     }
    }
  }
  if(pri==false)
  {
   printf("NO\n");
  }
 }
 return 0;
}
