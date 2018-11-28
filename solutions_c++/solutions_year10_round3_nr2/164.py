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
#include <fstream>

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
   int i, j, k;
   
   for (sc = 0; sc < T; sc++) {
      TT L, P, C;
      cin >> L >> P >> C;
      k = 0;
      while (1) {
         if (P <= L*C) {k--; break;}
         TT p2 = 1;
         for (i = 0; i < k; i++) p2 *= 2;
         TT t = 1;
         double t1 = 1;
         for (j = 0; j < p2; j++) {t *= C; t1 *= C;}
         t *= t;
         t1 *= t1;
         if (P <= L * t1) break;
         k++;
      }
      k++;
      cout << "Case #" << sc+1 << ": ";
      cout << k;
      cout << endl;
   }
   
   fclose(stdin); fclose(stdout);
   return 0;   
}