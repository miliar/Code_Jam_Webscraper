#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

typedef long long longlong;

typedef pair<int,int> pairii;

const int inf = 1000000009;
const double pi = atan(1.0) * 4.0;
const double eps = 1e-8;

longlong p[1001];

longlong gcd(longlong x, longlong y) { return y ? gcd(y, x%y) : x; }

void sortdec (int ln)
{            
   longlong t;
   for (int i = 0; i < ln; ++i)
      for (int j = ln - 1; j > i; --j)
         if (p[j] > p[j - 1])
         {
            t = p[j];
            p[j] = p[j-1];
            p[j-1] = t;
         }
   //for (int i = 0; i < ln; ++i)
   //   printf(" %i", p[i]);
   //printf("\n");
}

longlong solve (int lpk, int kn, int ln)
{                   
   longlong minkeyp = 0;
   for (int i = 0; i < ln; ++i)
      minkeyp += p[i] * (i / kn + 1);
   return minkeyp;
}

//#include <windows.h>

int main() {
   freopen("ain.txt", "r", stdin);
   freopen("aout.txt", "w", stdout);
                                
   int tn;
   cin >> tn;
   for (int i = 0; i < tn; ++i)
   {
      int lpk, kn, ln;
      cin >> lpk >> kn >> ln;
      
      for (int j = 0; j < ln; ++j)
         cin >> p[j];

      if (ln > kn * lpk)
      {
         printf("Case #%d: Impossible\n", i+1);
         continue;
      }           
      sortdec(ln);

      longlong ans = solve(lpk, kn, ln);
      cout << "Case #" << i + 1 << ": " << ans << "\n";
      //printf("Case #%d: %d\n", i+1, ans);
   }
   //while (!(GetAsyncKeyState(VK_RETURN)&0x8000))
   //   ;

   return 0;
}
