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

int n, m, a;

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> n >> m >> a;
      int p1 = 0, q1 = 0, ok = 0;
      cout << "Case #" << sc << ": ";
      for (int p2 = 0; p2 <= n; p2++)
         for (int q2 = 0; q2 <= m; q2++)
            for (int p3 = 0; p3 <= n; p3++)
               for (int q3 = 0; q3 <= m; q3++) {
                  int sq = abs((p3-p1)*(q2-q1) - (q3-q1)*(p2-p1));
                  if (sq == a && !ok) {
                     ok = 1;
                     cout << p1 << " " << q1 << " " << p2 << " " << q2 << " " << p3 << " " << q3;
                  }
               }
      if (!ok) cout << "IMPOSSIBLE";
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}