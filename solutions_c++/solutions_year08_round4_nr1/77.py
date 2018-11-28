#include <iostream>
using namespace std;

int f[100000][2], t[100000], c[100000], n, ts, o, fw, l, tar, i;

void solve(int i, int o, int d) {
     int j, k;
     for (j=0; j<2; j++)
         for (k=0; k<2; k++)
             if (o) f[i][j & k] <?= f[i*2][j] + f[i*2+1][k] + d;
               else f[i][j | k] <?= f[i*2][j] + f[i*2+1][k] + d;
}

main() {
       freopen("b.in", "r", stdin);
       freopen("b.out", "w", stdout);
       
       for (cin >> ts; ++o <= ts; ) {
           cin >> n >> tar;
           fw = n-1 >> 1;
           for (i=1; i<=fw; i++)
               cin >> t[i] >> c[i];
           for (i=fw+1; i<=n; i++) {
               cin >> t[i];
               f[i][t[i]] = 0;
               f[i][1-t[i]] = 1000000;
           }
           for (i=fw; i; i--) {
               f[i][0] = f[i][1] = 1000000;
               solve(i, t[i], 0);
               if (c[i]) solve(i, 1-t[i], 1);
//               cout << i << ' ' << f[i][0] << ' ' << f[i][1] << endl;
           }
           cout << "Case #" << o << ": ";
           if (f[1][tar] > fw) cout << "IMPOSSIBLE" << endl;
                         else  cout << f[1][tar] << endl;
       }
}
