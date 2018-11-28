#include <iostream>
using namespace std;

long long n, m, a, x1, x2, y1, y2, ans, ts, o;

main() {
       freopen("a.in", "r", stdin);
       freopen("a.out", "w", stdout);
       
       for (cin >> ts; ++o <= ts; ) {
           cin >> n >> m >> a;
           cout << "Case #" << o << ": ";
           for (x1=0; x1<=n; x1++)
           for (x2=0; x2<=n; x2++)
           for (y1=0; y1<=m; y1++)
           for (y2=0; y2<=m; y2++) if (a >= 0) {
               ans = abs(x1*y2 - x2*y1);
               if (a == ans) {
                  cout << "0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
                  a = -1;
               }
           }
           if (a != -1) cout << "IMPOSSIBLE" << endl;
       }
}
