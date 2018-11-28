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
#include <map>

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

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int c, i, j, k;
      cin >> c;
      map<int, int> a[2];
      int sum = 0;
      for (i = 0; i < c; i++) {
         int p, v;
         cin >> p >> v;
         a[0][p] = v;
         sum += v;
      }
      
      int step = 0;
      TT ans = 0;
      while (a[step].size() != sum) {
         int was = 0;
         a[1-step].clear();
         for (map<int, int>::iterator g = a[step].begin(); g != a[step].end(); ++g) {
            int v = g->B;
            int k = g->A;
            if (v % 2) {
               if (a[1-step].find(k) == a[1-step].end()) a[1-step][k] = 1; else a[1-step][k]++;
            }   
            if (v > 1) {
               ans += v/2;
               if (a[1-step].find(k-1) == a[1-step].end()) a[1-step][k-1] = v/2; else a[1-step][k-1] += v/2;
               if (a[1-step].find(k+1) == a[1-step].end()) a[1-step][k+1] = v/2; else a[1-step][k+1] += v/2;
            }
         }
         step = 1-step;
      }

      cout << "Case #" << sc+1 << ": ";
      cout << ans;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}