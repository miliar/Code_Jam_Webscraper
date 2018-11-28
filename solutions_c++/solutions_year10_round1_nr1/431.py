#include <iostream>
#include <fstream>
using namespace std;
#define FOR(i, a, b) for (int i=int(a); i<=int(b); ++i)
#define FORD(i, a, b) for (int i=int(a); i>=int(b); i--)
int h[] = {1, 1, 1, 0};
int c[] = {-1, 0, 1, 1};
int main() {
    freopen("A.in2", "r", stdin);
    freopen("A.ou2", "w", stdout);
    int t, n, k;
    string a[51];
    char b[51][51];
    cin >> t;
    FOR(test, 1, t) {
              cin >> n >> k;
              getline(cin, a[0]);
              FOR(i, 1, n) getline(cin, a[i]);
              FOR(j, 1, n) {
                     int p = n;
                     FORD(i, n, 1) 
                             if (a[n+1-j][i-1] != '.') b[p--][j] = a[n+1-j][i-1];
                     FORD(i, p, 1) b[i][j] = '.';
              }
//              FOR(i, 1, n) {FOR(j, 1 , n)cout << b[i][j]; cout << endl;
  //            }
//              cout << endl << endl;
              bool val[2];
              val[0] = val[1] = false;
              int w;
              FOR(i, 1, n)
                     FOR(j, 1, n) 
                     if (b[i][j] != '.' ) {
                            if (b[i][j] == 'R') w = 0; else w = 1;
                            bool ok = false;
                            FOR(dir, 0, 3) {
                                     int x = i, y = j;
                                     FOR(lap, 1, k-1) {
                                              x += h[dir];
                                              y += c[dir];
                                              if (x < 1 || x > n || y < 1 || y > n) break;
                                              if (b[x][y] != b[i][j]) break;
                                              if (lap == k-1) ok = true;
                                     }
                                     if (ok) break;
                            }
                            if (ok) val[w] = true;
                     }
              if (val[0] && val[1]) cout <<"Case #" << test <<": Both" << endl;       
              else if (val[0]) cout <<"Case #" << test <<": Red" << endl;
              else if (val[1]) cout <<"Case #" << test <<": Blue" << endl;
              else cout <<"Case #" << test <<": Neither" << endl;                      
    }
}
