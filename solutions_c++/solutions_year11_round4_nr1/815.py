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

const int maxn = 2048;

struct line
{
   int b, e, w;
   line() {}
   line(int _b, int _e, int _w): b(_b), e(_e), w(_w) {}
};

line a[maxn];

bool less0(const line& a, const line& b)
{
   return a.b < b.b;
}

bool less1(const line& a, const line& b)
{
   return a.w < b.w;
}

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int i, j, k;
      int x, s, r, n;
      double t;
      cin >> x >> s >> r >> t >> n;
      for (i = 0; i < n; i++) {
         cin >> a[i].b >> a[i].e >> a[i].w;
         a[i].w += s;
      }
      sort(a+0, a+n, less0);
      int m = n;
      for (i = 0; i < n-1; i++) {
         if (a[i+1].b > a[i].e) {
            a[m].b = a[i].e;
            a[m].e = a[i+1].b;
            a[m].w = s;
            m++; 
         }
      }
      if (a[0].b > 0) {
         a[m].b = 0;
         a[m].e = a[0].b;
         a[m].w = s;
         m++; 
      }
      if (a[n-1].e < x) {
         a[m].b = a[n-1].e;
         a[m].e = x;
         a[m].w = s;
         m++; 
      }
      sort(a+0, a+m, less1);
      
      double ans = 0.0;
      for (i = 0; i < m; i++) {
         double L = a[i].e - a[i].b;
         double V = a[i].w;
         double dV = r - s;
         if (L / (V + dV) < t) {
            double cur = L / (V + dV);
            ans += cur;
            t -= cur;
         } else {
            double dist = t * (V + dV);
            ans += t + (L - dist) / V;
            t = 0;
         }
      }

      cout << "Case #" << sc+1 << ": ";
      cout << fixed << setprecision(8) << ans;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}