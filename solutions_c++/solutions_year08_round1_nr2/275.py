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

const int maxn = 110;
const int inf = 1000000;

int n, m, v;
int g[maxn][maxn], t[maxn][maxn];

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, k, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> n >> m;
      for (i = 0; i < m; i++) {
         cin >> g[i][0];
         for (k = 1; k <= g[i][0]; k++) {
            cin >> g[i][k] >> t[i][k];
            g[i][k]--;
         }   
      }

      int ans = -1, best = inf; 
      for (i = 0; i < 1 << n; i++) {
         int ok = 1;
         for (j = 0; j < m; j++) {
            int ok1 = 0;
            for (k = 1; k <= g[j][0]; k++)
               if (((1 << g[j][k]) & i) == t[j][k]*(1 << g[j][k])) {ok1 = 1; break;}
            if (!ok1) {ok = 0; break;}
         }
         if (ok) {
            k = 0; j = i;
            while (j) {k++; j &= j-1;}
            if (k < best) {ans = i; best = k;}
         }
      }

      if (ans < 0) {      
         cout << "Case #" << sc << ": " << "IMPOSSIBLE" << endl;
      } else {
         cout << "Case #" << sc << ": ";
         for (i = 0; i < n; i++) {cout << ans%2 << " "; ans /= 2;}
         cout << endl;
      }
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}