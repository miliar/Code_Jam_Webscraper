#include <string>
#include <iostream>
using namespace std;
void p(int a, int b = -1234, int c = -1234, int d = -1234) { cout << a << ' ';
if (b != -1234)  cout << b << ' ';
if (c != -1234)  cout << c << ' ';
if (d != -1234)  cout << d << ' '; cout << endl; 
 }

int ts, l, n, m, i, j, k, mn, ii, jj, d;
int a[110][110], fa[110*110];
int dx[] = {-1, 0, 0, 1}, dy[] = {0, -1, 1, 0}; 

void update(int x, int y) {
     x += dx[k]; y += dy[k];
     if (x < 0 || y < 0 || x >= n || y >= m) return;
     if (a[x][y] < mn) {
        mn = a[x][y]; d = k+1;
     }
}

int f(int x) {
    return (fa[x] == x || fa[x] < 0) ? x : fa[x] = f(fa[x]);
}

main() {
       freopen("b1.in", "r", stdin);
       freopen("2.out", "w", stdout);
       
       for (cin >> ts; ++l <= ts; ) {
           cout << "Case #" << l << ": " << endl;
           cin >> n >> m;
           for (i=0; i<n; i++)
               for (j=0; j<m; j++) {
                   cin >> a[i][j];
                   fa[i*m+j] = i*m+j;
               }
           for (i=0; i<n; i++)
               for (j=0; j<m; j++) {
                   mn = a[i][j]; d = 0;
                   for (k=0; k<4; k++) update(i, j);
//                   p(i, j, d);
                   if (d) fa[f(i*m+j)] = f((i+dx[d-1])*m+j+dy[d-1]);
               }
           mn = 'a';
           for (i=0; i<n; i++)
               for (j=0; j<m; j++)// { p(i, f(i*m+j), fa[f(i*m+j)], mn);
                   if (fa[f(i*m+j)] >= 0) fa[f(i*m+j)] = - mn++;// p(fa[6]);}
//           p(n, m); 
           for (i=0; i<n; i++) {
               for (j=0; j<m; j++) //{ p(i, j, i*m+j);
                   cout << char(-fa[f(i*m+j)]) << ' ';// }
               cout << endl;
           }
       }
}
