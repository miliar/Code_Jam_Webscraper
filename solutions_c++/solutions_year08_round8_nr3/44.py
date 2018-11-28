#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VII vector<PII >
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 1010;
const int mod = 1000000009;

int n, k;
int c[maxn][maxn];
TT d[maxn][maxn];
VVI g;

int calcC(int n, int k)
{
   /*if (k < 0 || k > n) return 0;
   return c[n][k];*/
   TT ans = 1;
   for (int i = (n-k)+1; i <= n; i++) ans = (ans*i) % mod;
   return ans;
}

TT dfs(int x, int k1, int p)
{
   int ch = g[x].size();
   if (p >= 0) ch--;
   int can = k-ch;
   if (p >= 0) can--;
   TT ans = 1;
   for (int i = 0; i < g[x].size(); i++) {
      int v = g[x][i];
      if (v != p) {
         if (k < ch) return 0;
         ans = (ans * dfs(v, can, x)) % mod;
      }
   }
   ans = (ans * calcC(k1, ch)) % mod;
   return ans;
}

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   memset(c, 0, sizeof(c));
   c[0][0] = 1;
   for (i = 1; i < maxn; i++) {
      c[i][0] = 1;
      for (j = 1; j <= i; j++) c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod;
   }
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> n >> k; g.clear(); g.resize(n);
      for (i = 0; i < n-1; i++) {
         int u, v; cin >> u >> v; u--; v--; 
         g[u].PB(v); g[v].PB(u);
      }
      
      memset(d, 255, sizeof(d));
      TT ans = dfs(0, k, -1);
      cout << "Case #" << sc << ": ";
      cout << ans;
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}