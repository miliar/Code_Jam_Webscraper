#include <vector>
#include <iostream>
using namespace std;

const int mx = 2100;
int s[mx], one[mx], ts, o, n, i, j, k, m, aa, bb, ok;
vector<int> v[mx];

void read() {
     cin >> n >> m;
     memset(one, 0, sizeof(one));
     for (i=0; i<m; i++) {
         cin >> k; v[i].clear();
         for (j=0; j<k; j++) {
             cin >> aa >> bb;
             if (bb) one[i] = aa; else v[i].push_back(aa);
         }
     }
}

void solve() {
     memset(s, 0, sizeof(s));
     while (1) {
           ok = 1;
           for (i=0; i<m; i++) {
               aa = 0;
               if (one[i] && s[one[i]]) { aa = 1; continue; }
               for (j=0; j<v[i].size(); j++)
                   if (s[v[i][j]] == 0) {aa = 1; break; }
               if (!aa) { ok = 0; break; }
           }
           if (!ok) {
              if (!one[i] || s[one[i]]) { cout << " IMPOSSIBLE" << endl; return; }
              s[one[i]] = 1;
           } else break;
     }
     for (i=1; i<=n; i++) cout << ' ' << s[i];
     cout << endl;
}

main() {
       freopen("b1.in", "r", stdin);
       freopen("b1.out", "w", stdout);
       
       for (cin >> ts; ++o<=ts; ) {
           read();
           cout << "Case #" << o << ":";
           solve();
       }
}
