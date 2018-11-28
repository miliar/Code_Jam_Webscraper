#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T> inline T sqr( const T &a ) { return a*a; }
typedef long long int64;

template<typename T>
inline T sqrhypot(const T &dx, const T &dy) {
   return sqr(dx) + sqr(dy);
}


int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      int N, M; cin >> N >> M;
      assert(N == 2);

      int64 x[20], y[20];
      for (int i=0; i<N+M; ++i) {
         cin >> x[i] >> y[i];
      }

      cout << "Case #" << tt << ":";

      long double d = hypotl(x[0]-x[1], y[0]-y[1]);
      int64 d2 =    sqrhypot(x[0]-x[1], y[0]-y[1]);
      for (int i=2; i<N+M; ++i) {
         long double r = hypotl(x[0]-x[i], y[0]-y[i]);
         int64 r2 =    sqrhypot(x[0]-x[i], y[0]-y[i]);
         long double R = hypotl(x[1]-x[i], y[1]-y[i]);
         int64 R2 =    sqrhypot(x[1]-x[i], y[1]-y[i]);

         long double A =
            r2 * acos((d2 + r2 - R2) / (2*d*r)) + 
            R2 * acos((d2 + R2 - r2) / (2*d*R)) -
            0.5 * sqrt((-d + r + R) * (d + r - R) * (d - r + R) * (d + r + R));

         char buf[100];
         sprintf(buf, " %.9f", double(A));
         cout << buf;
      }
      cout << endl;
   }

   return 0;
} 
