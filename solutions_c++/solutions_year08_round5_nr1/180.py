#include <string>
#include <iostream>
using namespace std;

const int maxn = 10000;
const int maxt = 2000;
int l[maxn], r[maxn], uu[maxn], dd[maxn], rr[maxn], dr[maxn], n, rep[maxt], i, j, k;
string s[maxt];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int cx, cy, mianji, d, nx, ny, tot, task, t;

main() {
       freopen("a.in", "r", stdin);
       freopen("a.out", "w", stdout);
       for (cin >> task; ++t <= task; ) {
           cin >> n;
           for (i=0; i<n; i++) cin >> s[i] >> rep[i];
           cx = 5000;
           cy = 5000; 
           mianji = 0;
           d = 0;
           tot = 0;
           for (i=9001; i>0; i--)
           { 
                r[i] = 0; 
                l[i] = 10000;
           } 
           for (i=0; i<n; i++)
               for (j=0; j<rep[i]; j++)
                   for (k=0; k<s[i].length(); k++) 
                   {
                       if (s[i][k] == 'L') 
                        { 
                            d = (d+3) % 4; 
                            continue; 
                        }
                       if (s[i][k] == 'R') 
                       { 
                            d = (d+1)%4; 
                            continue; 
                        }
                       if (!dx[d]) 
                       {
                          if (d == 2) 
                            ny = cy-1; 
                          else 
                            ny = cy;
                          l[ny] <?= cx; 
                          r[ny] >?= cx;
                       }
                       nx = cx + dx[d]; 
                       ny = cy + dy[d];
                       mianji += nx * cy - ny * cx;
                       cx = nx; 
                       cy = ny;
                   }
           dd[0] = uu[9001] = 10000;
           for (i=1; i<9000; i++) 
           {
               dd[i] = dd[i-1] <? l[i];
               dr[i] = dr[i-1] >? r[i];
           }
           for (i=9000; i; i--) 
           {
               uu[i] = uu[i+1] <? l[i];
               rr[i] = rr[i+1] >? r[i];
               l[i] <?= dd[i] >? uu[i];
               r[i] >?= dr[i] <? rr[i];
           }
           for (i=9000; i; i--) 
           {
               tot += r[i]-l[i] >? 0;
           }
           cout << "Case #" << t << ": ";
           cout << tot - abs(mianji)/2 << endl;
       }
}

