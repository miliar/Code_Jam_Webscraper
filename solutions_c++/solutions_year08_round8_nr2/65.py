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

const int maxn = 310;

string c[maxn], w[3];
int a[maxn], b[maxn];
int vis[10010], g, n, ans;

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num, k;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> n;
      for (i = 0; i < n; i++) {
         cin >> c[i] >> a[i] >> b[i];
      }
      
      ans = -1;
      for (i = 0; i < (1 << n); i++) {
         memset(vis, 255, sizeof(vis));
         int ans1 = 0;
         for (j = 0; j < n; j++) if (i & (1 << j)) {
            ans1++;
            for (k = a[j]; k <= b[j]; k++) vis[k] = j;
         }
         
         g = 0;
         int gok = 1;
         for (k = 1; k <= 10000; k++) {
            if (vis[k] < 0) {gok = 0; break;}
            int ok = 0;
            for (j = 0; j < g; j++) if (w[j] == c[vis[k]]) {ok = 1; break;}
            if (!ok) {
               if (g >= 3) {gok = 0; break;}
               w[g] = c[vis[k]]; g++;
            }
         }
         if (gok) {
            if (ans == -1 || ans > ans1) ans = ans1;
         }
      }
      cout << "Case #" << sc << ": ";
      if (ans < 0) cout << "IMPOSSIBLE"; else cout << ans;
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}