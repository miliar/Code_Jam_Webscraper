#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 110;

int n, m, a[maxn][maxn], vis[maxn][maxn], k;
char ans[maxn][maxn];
VI g[maxn][maxn];

void add(int i, int j)
{
   int best = a[i][j], xx = i, yy = j;
   for (int dx = -1; dx <= 1; dx++)
      for (int dy = -1; dy <= 1; dy++)
         if (abs(dx) + abs(dy) == 1) {
            int x = i + dx, y = j + dy;
            if (x >= 0 && x < n && y >= 0 && y < m && a[x][y] < a[i][j]) {
               if (a[x][y] < best) {
                  best = a[x][y]; 
                  xx = x; yy = y;
               }
            }
         }
   g[i][j].PB(xx*m + yy);
   g[xx][yy].PB(i*m + j);
}

void dfs(int i, int j)
{
   vis[i][j] = 1;
   ans[i][j] = k + 'a';
   for (int sc = 0; sc < g[i][j].size(); sc++) {
      int x = g[i][j][sc] / m, y = g[i][j][sc] % m;
      if (!vis[x][y]) dfs(x, y);
   }
}

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int i, j;
   int t; cin >> t;
   for (int sc = 0; sc < t; sc++) {
      cin >> n >> m;
      for (i = 0; i < n; i++)
         for (j = 0; j < m; j++)
            cin >> a[i][j];
      
      memset(vis, 0, sizeof(vis));
      for (i = 0; i < n; i++)
         for (j = 0; j < m; j++) g[i][j].clear();
      for (i = 0; i < n; i++)
         for (j = 0; j < m; j++)
            add(i, j);
      k = 0;
      for (i = 0; i < n; i++)
         for (j = 0; j < m; j++)
            if (!vis[i][j]) {
               dfs(i, j);
               k++;
            }
      
      cout << "Case #" << sc+1 << ": " << endl;
      for (i = 0; i < n; i++) {
         for (j = 0; j < m; j++)
            cout << ans[i][j] << " ";
         cout << endl;
      }      
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}