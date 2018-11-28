#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define maxn 505
using namespace std;

string board[maxn];
int T,m,n,d;
int a[maxn][maxn];
long long linear[maxn][maxn],Xsum[maxn][maxn],Ysum[maxn][maxn];

long long linearSum(int u1,int v1,int u2,int v2)
{
     long long ans = linear[u2][v2];
     if (u1) ans -= linear[u1 - 1][v2];
     if (v1) ans -= linear[u2][v1 - 1];
     if (u1 && v1) ans += linear[u1 - 1][v1 - 1];
     return ans;
 }
 
long long getX(int u1,int v1,int u2,int v2)
{
     long long ans = Xsum[u2][v2];
     if (u1) ans -= Xsum[u1 - 1][v2];
     if (v1) ans -= Xsum[u2][v1 - 1];
     if (u1 && v1) ans += Xsum[u1 - 1][v1 - 1];
     return ans;
 }
 
long long getY(int u1,int v1,int u2,int v2)
{
     long long ans = Ysum[u2][v2];
     if (u1) ans -= Ysum[u1 - 1][v2];
     if (v1) ans -= Ysum[u2][v1 - 1];
     if (u1 && v1) ans += Ysum[u1 - 1][v1 - 1];
     return ans;
}

int main()
{
    freopen("b.i2","r",stdin);
    freopen("b.o2","w",stdout);
    
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
      scanf("%d %d %d", &m, &n, &d);
      for (int i = 0; i < m; i++) cin >> board[i];
      
      for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
        {
            a[i][j] = linear[i][j] = board[i][j] - '0';
            Xsum[i][j] = 1LL * linear[i][j] * i;
            Ysum[i][j] = 1LL * linear[i][j] * j;
        }
      
      for (int j = 1; j < n; j++)
        for (int i = 0; i < m; i++)
        {
            linear[i][j] += linear[i][j - 1];
            Xsum[i][j] += Xsum[i][j - 1];
            Ysum[i][j] += Ysum[i][j - 1];
        }
        
      for (int i = 1; i < m; i++)
        for (int j = 0; j < n; j++)
        {
            linear[i][j] += linear[i - 1][j];
            Xsum[i][j] += Xsum[i - 1][j];
            Ysum[i][j] += Ysum[i - 1][j];
        }
        
      int ret = -1;
      for (int poss = min(m,n); poss >= 3; poss--)
      {
        bool flag = false;
        for (int u1 = 0; u1 + poss - 1 < m; u1++)
          for (int v1 = 0; v1 + poss - 1 < n; v1++)
          {
              int u2 = u1 + poss - 1,v2 = v1 + poss - 1;
              double X = 0.5 * (u1 + u2),Y = 0.5 * (v1 + v2);  
              double negX = X * linearSum(u1,v1,u2,v2),negY = Y * linearSum(u1,v1,u2,v2);
              double posX = getX(u1,v1,u2,v2),posY = getY(u1,v1,u2,v2);
              double dx = posX - negX,dy = posY - negY;
              dx -= (u1 - X) * a[u1][v1];  dy -= (v1 - Y) * a[u1][v1];
              dx -= (u1 - X) * a[u1][v2];  dy -= (v2 - Y) * a[u1][v2];
              dx -= (u2 - X) * a[u2][v1];  dy -= (v1 - Y) * a[u2][v1];
              dx -= (u2 - X) * a[u2][v2];  dy -= (v2 - Y) * a[u2][v2];
              if (abs(dx) < 1e-9 && abs(dy) < 1e-9) flag = true;
          }
        if (flag)
        {
          ret = poss;  break;
        }
      }
      
      printf("Case #%d: ", it);
      if (ret < 0) printf("IMPOSSIBLE\n"); else printf("%d\n", ret);
    }
}
