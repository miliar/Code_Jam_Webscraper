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

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      TT n, pd, pg;
      cin >> n >> pd >> pg;
      
      int ok = 0;
      if (pg == 100 && pd != 100)  {
         ok = 0;
      } else if (!pd) {
         ok = 1;
      } else if (!pg) {
         ok = pd ? 0 : 1;
      } else {
         int d = 1;
         if (!(pd % 2)) d *= 2;
         if (!(pd % 4)) d *= 2;
         if (!(pd % 5)) d *= 5;
         if (!(pd % 25)) d *= 5;
         ok = (100 / d <= n) ? 1 : 0;
      }

      cout << "Case #" << sc+1 << ": ";
      cout << (ok ? "Possible" : "Broken");
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}