#include <string>
#include <iostream>
using namespace std;

int l, d, n;
string pa[6000];
int ch[6000], le[200];
char c;

main() {
       
       cin >> l >> d >> n;
       for (int i=0; i<d; i++)
           cin >> pa[i];
       for (int i=0; i<n; i++) {
           cout << "Case #" << i+1 << ": ";
           for (int j=0; j<d; j++) ch[j] = 1;
           for (int j=0; j<l; j++) {
               memset(le, 0, sizeof(le));
               cin >> c;
               if (c != '(') le[c] = 1; else {
                  while (1) {
                        cin >> c;
                        if (c == ')') break;
                        le[c] = 1;
                  }
               }
               for (int k=0; k<d; k++)
                   if (!le[pa[k][j]]) ch[k] = 0;
           }
           int ans = 0;
           for (int j=0; j<d; j++) if (ch[j]) ans++;
           cout << ans << endl;
       }
}
