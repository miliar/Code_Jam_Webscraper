#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<map>
#include<algorithm>
#include<bitset>
#include<cctype>
using namespace std;

typedef long long int64;
const int maxn=1100000;
int vis[2][111][111];
int x[2][maxn],y[2][maxn],t[2];
int tt,r,x1,x2,y1,y2,o1,o2,ans;

void solve()
  {
   memset(vis[o2],0,sizeof(vis[o2]));
   t[o2]=0;
   for (int i=0;i<t[o1];i++)
     {
      if (vis[o1][x[o1][i]-1][y[o1][i]] || vis[o1][x[o1][i]][y[o1][i]-1]) 
        {
         x[o2][t[o2]]=x[o1][i];y[o2][t[o2]++]=y[o1][i];
         vis[o2][x[o1][i]][y[o1][i]]=1;
        }
      if (vis[o1][x[o1][i]+1][y[o1][i]-1] && !vis[o1][x[o1][i]+1][y[o1][i]]) 
        {
         x[o2][t[o2]]=x[o1][i]+1;y[o2][t[o2]++]=y[o1][i];
         vis[o2][x[o1][i]+1][y[o1][i]]=1;
        }
     }
   o2=o1;o1^=1;
   ans++;
  }
  
int main()
  {
   //freopen("check.in","r",stdin);
   //freopen("check.out","w",stdout);
   scanf("%d",&tt); 
   for (int tot=1;tot<=tt;tot++)
     {
      memset(vis,0,sizeof(vis));
      ans=0;
      scanf("%d",&r);
      t[0]=0;
      for (int l=0;l<r;l++)
        {
         scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
         for (int i=x1;i<=x2;i++)
           for (int j=y1;j<=y2;j++)
             {
              vis[0][i][j]=1;
              x[0][t[0]]=i;y[0][t[0]++]=j;
             }
        }
      o1=0;o2=1;t[1]=0;
      while (t[o1])
        { 
         //printf("%d\n",t[o1]);
         /*for (int i=1;i<=5;i++)
           {
            for (int j=1;j<=6;j++)
              printf("%d",vis[o1][i][j]);
            printf("\n");
           }
         printf("\n");*/
         solve();
        }
      printf("Case #%d: %d\n",tot,ans);
     }
   return 0;
  }
