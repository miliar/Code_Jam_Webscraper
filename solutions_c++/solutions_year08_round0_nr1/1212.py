#include <string>
#include <iostream>
using namespace std;

int f[1010][110], n, i, j, k, l, ts, no, q;
string name[110], ss;
char tmp[1000];

main() {
       freopen("a3.in", "r", stdin);
       freopen("a3.out", "w", stdout);
       
       for (scanf("%d", &ts); no < ts; ) {
           scanf("%d\n", &n);
           cout << "Case #" << ++no << ": ";
           for (i=0; i<n; i++) {
               gets(tmp);    
               name[i] = tmp;
//               cout << name[i] << endl;
           }
           scanf("%d\n", &q);
           for (i=1; i<=q; i++) {
               gets(tmp); ss = tmp;
               for (j=0; j<n; j++) if (ss == name[j]) break;
               for (k=0; k<n; k++) f[i][k] = 10000;
               for (k=0; k<n; k++)
                   for (l=0; l<n; l++)
                       if (k != j) f[i][k] <?= f[i-1][l] + (k != l);
//           for (k=0; k<n; k++) cout << f[i][k] << ' '; cout << endl;
           }
           k = 10000;
           for (i=0; i<n; i++) k <?= f[q][i];
           cout << k << endl;
       }
       
}
