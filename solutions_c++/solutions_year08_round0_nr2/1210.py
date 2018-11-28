#include <string>
#include <iostream>
using namespace std;

int b[2][110], n, na, nb, i, j, k, ana, anb, ts, no, q, aa, bb;
pair<int, int> tme[2][200];

bool cmp(pair<int, int> a, pair<int, int> b) {
     if (a.second == b.second) return a.first < a.first;
     return a.second < b.second;
}

main() {
       freopen("b3.in", "r", stdin);
       freopen("b3.out", "w", stdout);
       
       for (scanf("%d", &ts); no < ts; ) {
           scanf("%d%d%d", &n, &na, &nb);
//           cout << na << ' ' << nb << endl;
           cout << "Case #" << ++no << ": ";
           memset(b, 0, sizeof(b));
           for (i=0; i<na; i++) {
               scanf("%d:%d", &aa, &bb);
               tme[0][i].second = aa*60+bb;
               scanf("%d:%d", &aa, &bb);
               tme[0][i].first = aa*60+bb;
           }
           for (i=0; i<nb; i++) {
               scanf("%d:%d", &aa, &bb);
               tme[1][i].second = aa*60+bb;
               scanf("%d:%d", &aa, &bb);
               tme[1][i].first = aa*60+bb;
           }
           sort(tme[0], tme[0]+na, cmp);
           sort(tme[1], tme[1]+nb);
           ana = anb = 0;
           for (i=0; i<na; i++) {
               k = 0;
               for (j=0; j<nb; j++)
                   if (tme[0][i].second >= tme[1][j].first+n && !b[1][j]) {
                      b[1][j] = 1; k = 1; break;
                   }
               if (!k) ana ++;
           }
           sort(tme[0], tme[0]+na);
           sort(tme[1], tme[1]+nb, cmp);
           for (i=0; i<nb; i++) {
               k = 0;
               for (j=0; j<na; j++)
                   if (tme[1][i].second >= tme[0][j].first+n && !b[0][j]) {
                      b[0][j] = 1; k = 1; break;
                   }
               if (!k) anb ++;
           }
           cout << ana << ' ' << anb << endl;
       }
       
}
