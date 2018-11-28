#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

#define maxn 101

int n,m;
bool vis[2][maxn][maxn];
void solve(){
  int tot = 0 ,ans = 1;  
  for (int i = 1; i < maxn ; i++)
     for (int j = 1; j < maxn ; j++)
       if (vis[0][i][j]) tot++;
  if (!tot) return;
  int now = 0, next = 1;
  while (tot)
  {
//     printf("%d\n", tot);
     memset(vis[next],false,sizeof(vis[next]));
     tot = 0; ans++;
     for (int i = 1; i < maxn ; i++)
       for (int j = 1; j < maxn ; j++)
         if (vis[now][i][j] && (vis[now][i][j - 1] || vis[now][i - 1][j])) 
           vis[next][i][j] = true;
     for (int i = 1; i < maxn ; i++)
       for (int j = 1; j < maxn ; j++)
         if (vis[now][i - 1][j] && vis[now][i][j - 1])
           vis[next][i][j] = true;
     for (int i = 1; i < maxn ; i++)
        for (int j = 1; j < maxn ; j++)
          if (vis[next][i][j]) tot++;
     swap<int> (now,next);
  }
  printf("%d\n", ans - 1);
}

int main(){
//    freopen("test1.txt","r",stdin);
//    freopen("C.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int p = 1; p <= T ; p++)
    {
       memset(vis,false,sizeof(vis));
       printf("Case #%d: ", p);
       scanf("%d", &n);
       for (int i = 1; i <= n ; i++)
       {
          int x1,x2,y1,y2;
          scanf("%d%d%d%d", &x1  , &y1 , &x2 ,&y2);
          for (int j = x1; j <= x2; j++)
            for (int k = y1; k <= y2; k++)
               vis[0][k][j] = true;
       }
       solve();
    }
    return 0;
}
  
