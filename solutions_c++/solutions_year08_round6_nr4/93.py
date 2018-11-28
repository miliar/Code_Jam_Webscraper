#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<string>
#include<math.h>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;

int ncase,test,n,m,a[10][10],b[10][10],c[10][10],p[10];
int sx,sy,f1[10],f2[10];
int cnt(int k)
{
    int s=0;
    while (k>0)
    {
          s+=k%2;
          k/=2;
    }
    return s;
}
bool dfs(int px,int py,int x,int y)
{
     int i,j,k;
     int visit[10];
     memset(visit,0,sizeof(visit));
     for (i=0;i<m;i++)
     if (c[x][i] && i!=px)
     {
         k=0;
         for (j=0;j<m;j++)
         if (j!=py && visit[j]==0 && b[y][j] && dfs(x,y,i,j))
         {
            visit[j]=1;
            k=1;
            break;
         }
         if (k==0) return 0;
     }
     for (j=0;j<m;j++)
     if (j!=py && visit[j]==0 && b[y][j]) return 0;
     return 1;
 }
int main()
{
    int i,j,x,y,k,ans;
    test=1;
    freopen("Din","r",stdin);
    freopen("D.out","w",stdout);
    scanf("%d",&ncase);
    while (test<=ncase)
    {
          scanf("%d",&n);
          memset(a,0,sizeof(a));
          memset(b,0,sizeof(b));
          memset(c,0,sizeof(c));
          for (i=1;i<n;i++)
          {
              scanf("%d%d",&x,&y);
              x--;y--;
              a[x][y]=a[y][x]=1;
          }
          scanf("%d",&m);
          for (i=1;i<m;i++)
          {
              scanf("%d%d",&x,&y);
              x--;y--;
              b[x][y]=b[y][x]=1;
          }
//          dfs(-1,-1,0,0);
          ans=0;
          for (i=1;i<(1<<n);i++)
          if (cnt(i)==m)
          { 
              memset(c,0,sizeof(c));
              k=0;
              for (j=0;j<n;j++)
              if ((i&(1<<j))>0) p[k++]=j;
              for (j=0;j<m;j++)
               for (k=0;k<m;k++)
               if (a[p[j]][p[k]]) c[j][k]=1;
              for (j=0;j<m;j++)
               for (k=0;k<m;k++)
               {
                   if (dfs(-1,-1,j,k)) ans=1;
               }
          }
          printf("Case #%d: ",test++);
          if (ans) printf("YES\n");
          else printf("NO\n");
    }
    return 0;
}
