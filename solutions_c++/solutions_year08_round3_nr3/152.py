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
longlong *cnt, *last;
int size = 500001;

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
}

longlong solve (longlong n)
{
   for (int i = 0; i < n; ++i)
   {
      last[i] = p[i];
      cnt[i] = 1;
      for (int j = 0; j < i; ++j)
         if (last[j] < last[i])
            cnt[i] = (cnt[i] + cnt[j]) % 1000000007ll;
   }      
   longlong res = 0;
   for (int j = 0; j < n; ++j)
      res = (res + cnt[j]) % 1000000007ll;

   return res;
}

#include <windows.h>

int main() {
   freopen("bin.txt", "r", stdin);
   freopen("bout.txt", "w", stdout);

   int tn;
   longlong a[1001];
   cnt = new longlong[size];
   last = new longlong[size];
   cin >> tn;
   for (int i = 0; i < tn; ++i)
   {
      longlong n, m, x, y, z;
      cin >> n >> m >> x >> y >> z;

      for (int j = 0; j < m; ++j)
         cin >> a[j];

      for (int j = 0; j < n; ++j)
      {  
         p[j] = a[j % m];
         //cout << " " << p[j];
         a[j % m] = (x * a[j % m] + y * (j + 1)) % z;
      }  
      //cout << "\n";

      //sortdec(ln);

      longlong ans = solve(n);
      cout << "Case #" << i + 1 << ": " << ans << "\n";
   }
   while (!(GetAsyncKeyState(VK_RETURN)&0x8000))
      ;

   return 0;
}
