#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

const int infi = 1000001;
int ts, o;
int mnx, mxx, mny, mxy;
int i, j, x, y, n, nt, tq;
int c[2010][2], q[2010][3];
string s;

void out(int a[], int len) {
     for (int i=0; i<len; i++) cout << a[i] << ' ';
     cout << endl;
}

void clear(int sx, int tx, int sy, int ty) {
//     cout << sx << ' ' << tx << ' ' << sy << ' ' << ty << endl;
     for (int i=0; i<tq; i++) if (q[i][2] == 0)
         if (sx <= q[i][0] && q[i][0] <= tx && sy <= q[i][1] && q[i][1] <= ty)
            q[i][2] = 2;
}

main() {
       freopen("4.in", "r", stdin);
       freopen("4.out", "w", stdout);
       
       for (cin >> ts; ++o <= ts; ) {
           cout << "Case #" << o << ": " << endl;
           cin >> n;
           memset(q, 0, sizeof(q));
           mnx = mny = infi;
           mxx = mxy = nt = 0;
           for (i=0; i<n; i++) {
               cin >> x >> y >> s;
               if (s == "NOT") {
                  cin >> s;
                  c[nt][0] = x; c[nt][1] = y;
                  nt ++;
               } else {
                  mnx <?= x; mny <?= y;
                  mxx >?= x; mxy >?= y;
               }
           }//thatthatthatthatthatthatthatthatthatthat
           cin >> tq;
           for (i=0; i<tq; i++) {
               cin >> q[i][0] >> q[i][1];
               if (mnx <= q[i][0] && q[i][0] <= mxx && mny <= q[i][1] && q[i][1] <= mxy)
                  q[i][2] = 1;
           }
           if (mnx > mxx) {
              for (i=0; i<nt; i++)
                  clear(c[i][0], c[i][0], c[i][1], c[i][1]);
           } else {
           for (i=0; i<nt; i++) {
               if (c[i][0] > mxx) {
                  if (c[i][1] < mny) clear(c[i][0], infi, 0, c[i][1]); else
                  if (c[i][1] > mxy) clear(c[i][0], infi, c[i][1], infi); else
                                     clear(c[i][0], infi, 0, infi);
               } else
               if (c[i][0] < mnx) {
                  if (c[i][1] < mny) clear(0, c[i][0], 0, c[i][1]); else
                  if (c[i][1] > mxy) clear(0, c[i][0], c[i][1], infi); else
                                     clear(0, c[i][0], 0, infi);
               } else
               if (c[i][1] < mny) clear(0, infi, 0, c[i][1]); else
                                  clear(0, infi, c[i][1], infi);
           }
           }
           for (i=0; i<tq; i++)
               if (q[i][2] == 1) cout << "BIRD" << endl; else
               if (q[i][2] == 2) cout << "NOT BIRD" << endl; else
                                 cout << "UNKNOWN" << endl;
       }
//       system("pause");
}
