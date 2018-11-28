#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset((a),(b),sizeof(a))

#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

const string fileName = "B-small-attempt0";

int n, m, tmp;
int a[512][512];
int dx[512][512], dy[512][512];
bool Res[512][512];
string s[512];

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int t;
    cin >> t;
    FOR (ntest, 1, t+1) {
        cin >> n >> m >> tmp;
        REP (i, n) cin >> s[i];
        
        REP (i, n) {
            REP (j, m) {
                a[i][j] = s[i][j]-'0';
            }
        }
        
        memset (dx, 0, sizeof (dx));
        memset (dy, 0, sizeof (dy));

        int ans = 0;
        for (int size = 3; size <= min (n, m); size += 2) {
            memset (Res, 0, sizeof (Res));
            int h = size / 2;
            REP (i, n) 
                REP (j, m) {
                    if (j >= h) dx[i][j] += -h * a[i][j-h];
                    if (j+h < m) dx[i][j] += h * a[i][j+h];
                    
                    if (i >= h) dy[i][j] += -h * a[i-h][j];
                    if (i+h < n) dy[i][j] += h * a[i+h][j];                    
                }
            
            FOR (j, h, m-h) {
                int calc = 0;
                REP (i, n) {
                    calc += dx[i][j];
                    if (i >= size) calc -= dx[i-size][j];
                    if (i >= size-1) {
                        int cy = i-h;
                        int cx = j;
                        int f = calc;
                        f -= -h * (a[cy-h][cx-h] + a[cy+h][cx-h]) + 
                              h * (a[cy-h][cx+h] + a[cy+h][cx+h]);                      
                        Res[cy][cx] = (f == 0);
                    }
                }
            }
            FOR (i, h, n-h) {
                int calc = 0;
                REP (j, m) {
                    calc += dy[i][j];
                    if (j >= size) calc -= dy[i][j-size];
                    if (j >= size-1) {
                        int cy = i;
                        int cx = j-h;
                        int f = calc;
                        f -= -h * (a[cy-h][cx-h] + a[cy-h][cx+h]) + 
                              h * (a[cy+h][cx-h] + a[cy+h][cx+h]);                      
                        if (f != 0)
                            Res[cy][cx] = false;
                    }
                }
            }            
            REP (i, n) 
                REP (j, m)
                    if (Res[i][j]) {
                        ans = max(ans, size);
                    }
        }
        memset (dx, 0, sizeof (dx));
        memset (dy, 0, sizeof (dy));

        for (int size = 2; size <= min (n, m); size += 2) {
            memset (Res, 0, sizeof (Res));
            int u = size-1;
            int h = size / 2;
            REP (i, n) 
                REP (j, m) {
                    if (j-h+1 >= 0) dx[i][j] += -u * a[i][j-h+1];
                    if (j+h < m) dx[i][j] += u * a[i][j+h];
                    
                    if (i-h+1 >= 0) dy[i][j] += -u * a[i-h+1][j];
                    if (i+h < n) dy[i][j] += u * a[i+h][j];                    
                }
            
            FOR (j, h-1, m-h) {
                int calc = 0;
                REP (i, n) {
                    calc += dx[i][j];
                    if (i >= size) calc -= dx[i-size][j];
                    if (i >= size-1) {
                        int cy = i-h;
                        int cx = j;
                        int f = calc;
                        f -= -h * (a[cy-h+1][cx-h+1] + a[cy+h][cx-h+1]) + 
                              h * (a[cy-h+1][cx+h] + a[cy+h][cx+h]);                      
                        Res[cy][cx] = (f == 0);
                    }
                }
            }
            
            FOR (i, h-1, n-h) {
                int calc = 0;
                REP (j, m) {
                    calc += dy[i][j];
                    if (j >= size) calc -= dy[i][j-size];
                    if (j >= size-1) {
                        int cy = i;
                        int cx = j-h;
                        int f = calc;
                        f -= -h * (a[cy-h+1][cx-h+1] + a[cy-h+1][cx+h]) + 
                              h * (a[cy+h][cx-h+1] + a[cy+h][cx+h]);                      
                        if (f != 0)
                            Res[cy][cx] = false;
                    }
                }
            }            
            if (size == 2) continue;
            REP (i, n) 
                REP (j, m)
                    if (Res[i][j]) {
                        ans = max(ans, size);
                    }
        }
        cout << "Case #" << ntest << ": ";
        if (ans == 0)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << endl;
    }
	return 0;
}
