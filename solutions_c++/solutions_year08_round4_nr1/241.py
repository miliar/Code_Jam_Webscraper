#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define VI vector<int>
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 10010;
const int inf = 100000000;

int m, v, k, n, val[maxn], a[maxn][2], g[maxn], c[maxn];

void dfs(int x)
{
   if (x > k) {
      a[x][val[x]] = 0; a[x][1-val[x]] = inf;
   } else {
      dfs(2*x); dfs(2*x+1);
      for (int i = 0; i < 2; i++) if (a[2*x][i] != inf)
         for (int j = 0; j < 2; j++) if (a[2*x+1][j] != inf) {
            int t;
            if (g[x] == 1) t = i&j; else t = i|j;
            if (a[x][t] > a[2*x][i] + a[2*x+1][j]) {
               a[x][t] = a[2*x][i] + a[2*x+1][j];
            }
            if (c[x]) {
               if (g[x] == 1) t = i|j; else t = i&j;
               if (a[x][t] > a[2*x][i] + a[2*x+1][j] + 1)
                  a[x][t] = a[2*x][i] + a[2*x+1][j] + 1;
            }
         }
   }
}

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> m >> v; k = (m-1)/2;
      for (i = 1; i <= k; i++) cin >> g[i] >> c[i];
      for (i = k+1; i <= m; i++) cin >> val[i];
      for (i = 1; i <= m; i++) a[i][0] = a[i][1] = inf;
      dfs(1);      
      cout << "Case #" << sc << ": ";
      if (a[1][v] == inf) cout << "IMPOSSIBLE";
      else cout << a[1][v];
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}