#include "stdio.h"
#include "stdlib.h"
#include "string.h"
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
#define VPII vector<PII >
#define VR vector<real>
#define A first
#define B second

const int maxn = 512;

char a[maxn][maxn], vis[maxn][maxn];
//char can[maxn][maxn][maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   int i, j, k;
   int m, n;
   for (sc = 0; sc < T; sc++) {
      cin >> m >> n;
      for (i = 0; i < m; i++) {
         string s; cin >> s;
         for (j = 0; j < n/4; j++) {
            int t = s[j] <= '9' ? s[j]-'0' : s[j]-'A'+10;
            for (k = 0; k < 4; k++) {
               a[i][j*4+3-k] = t % 2;
               t /= 2;
            }
         }   
      }

      memset(vis, 0, sizeof(vis));
      
      /*memset(can, 0, sizeof(can));
      for (i = 0; i < m; i++)
         for (j = 0; j < n; j++)
            can[i][j][1] = 1;
      for (sz = 0; sz <= m; sz++)
         for (i = 0; i < m; i++)
            for (j = 0; j < n; j++) {
               
            }*/
            
      VPII ans;
      for (k = m; k >= 1; k--) {
         int was = 0;
         for (i = 0; i < m; i++)
            for (j = 0; j < n; j++)
               if (i+k-1 < m && j+k-1 < n) {
                  int ok = 1;
                  for (int dx = 0; dx < k; dx++) {
                     for (int dy = 0; dy < k; dy++) {
                        if (vis[i+dx][j+dy]) {ok = 0; break;}
                        if (dx && a[i+dx][j+dy] == a[i+dx-1][j+dy]) {ok = 0; break;}
                        if (dy && a[i+dx][j+dy] == a[i+dx][j+dy-1]) {ok = 0; break;}
                     }
                     if (!ok) break;
                  }   
                  if (ok) {
                     was++;
                     for (int dx = 0; dx < k; dx++)
                        for (int dy = 0; dy < k; dy++)
                           vis[i+dx][j+dy] = 1;
                  }
               }
         if (was) ans.PB(PII(k, was));
      }

      cout << "Case #" << sc+1 << ": ";
      cout << ans.size();
      for (i = 0; i < ans.size(); i++)
         cout << endl << ans[i].A << " " << ans[i].B;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}