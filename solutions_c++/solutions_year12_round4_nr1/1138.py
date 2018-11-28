#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <math.h>
#include <iostream>
#include <string>
#include <map>
using namespace std;
int dp[11000];
int d[11000];
int l[11000];
int n;
int le;
int main()
{
    int t;
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&t);
    int num=0;
    while (t--)
    {
      scanf("%d",&n);
      int i,j;
      for (i=0;i<n;i++)
      {
          scanf("%d%d",&d[i],&l[i]);
      }
      scanf("%d",&le);
      memset(dp,0,sizeof(dp));
      dp[0]=d[0];
      for (i=0;i<n-1;i++)
      if (dp[i]!=0)
      {
         // printf("%d %d\n",i,dp[i]);
          for (j=i+1;j<n;j++)
          {
              if (d[j]-d[i]<=dp[i])
              {
                        int q=min(d[j]-d[i],l[j]);
                        dp[j]=max(dp[j],q);
              }
              else
              break;
          }
      }
      bool ok=false;
      for (i=0;i<n;i++)
      if (dp[i]!=0)
      {
      //printf("%d %d\n",i,dp[i]);
      if (d[i]+dp[i]>=le)
      ok=true;
      }
      printf("Case #%d: ",++num);
      if (ok)
      printf("YES\n");
      else
      printf("NO\n");
    }
}
      
         
