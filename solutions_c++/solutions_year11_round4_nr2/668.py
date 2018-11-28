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
#define VR vector<real>
#define A first
#define B second

const int maxn = 512;

TT a[maxn][maxn];
int n, m;
TT d;

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int i, j, k;
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      cin >> n >> m >> d;
      memset(a, 0, sizeof(a));
      for (i = 0; i < n; i++) {
         string t;
         cin >> t;
         for (j = 0; j < m; j++) {         
            a[i][j] = d + (t[j] - '0');
         }   
      }
      
      /*int was = 0;
      for (sz = min(n, m); sz >= 3; sz--) {
         int w = sz/2;
         for (i = 1; i <= n; i++) {
            L[i][1] = R[i][1] = 0;
            for (j = 0; j < sz; j++) {
               for (k = 0; k < sz; k++) {
                  if (k < w) L[i][1] += ((sz-1) - 2*k) * a[i+j][1+k];
                  if (k > (sz-1 - w)) R[i][1] += ((sz-1) - 2*k) * a[i+j][1+k];
               }
            }
            for (j = 2; j+sz-1 <= m; j++) {
               L[i][j] = L[i][j-1] + 2*calc(i, j, i+sz-1, j+w-1) - ;
            }
         }
         if (was) break;
      }*/
      
      int was = 0;
      for (int sz = min(n, m); sz >= 3; sz--) {
         for (i = 0; i+sz-1 < n; i++)
            for (j = 0; j+sz-1 < m; j++) {
               int ci = sz-1;
               int cj = sz-1;
               TT sumi = 0, sumj = 0; 
               for (int dx = 0; dx < sz; dx++) {
                  for (int dy = 0; dy < sz; dy++) {
                     int cnt = 0;
                     if (dx == 0 || dx == sz-1) cnt++;
                     if (dy == 0 || dy == sz-1) cnt++;
                     if (cnt == 2) continue;
                     sumi += (2*dx - ci) * a[i+dx][j+dy];
                     sumj += (2*dy - cj) * a[i+dx][j+dy];
                  }
               }
               if (!sumi && !sumj) {was = sz; break;}
            }
         if (was) break;
      }

      cout << "Case #" << sc+1 << ": ";
      if (was) {
         cout << was;
      } else {
         cout << "IMPOSSIBLE";
      }
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}