#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>

#include <cassert>
#include <cmath>
#include <ctime>

#include <map>
#include <set>
#include <bitset>
#include <queue>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()

const int INF = INT_MAX >> 1;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1E-8;

#define N 505

int n, m;
int a[N][N];
int sx[N][N], sy[N][N];

char buf[N];

inline void addOdd(int x, int y, int px, int py) {
    sx[px][py] += a[x][y] * (x - px);
    sy[px][py] += a[x][y] * (y - py);
}

inline void addEven(int x, int y, int px, int py) {
    sx[px][py] += a[x][y] * (2 * (x - px) + 1);
    sy[px][py] += a[x][y] * (2 * (y - py) + 1);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);
    int trash;
    for (int tc = 1; tc <= tk; ++tc) {
        scanf("%d %d %d\n", &n, &m, &trash);

        forn(i, n) {
            gets(buf);
            forn(j, m) a[i][j] = buf[j] - '0';
        }

        int ans = 0;

        memset(sx, 0, sizeof sx);
        memset(sy, 0, sizeof sy);

        for(int k = 1; 2 * k + 1 <= n && 2 * k + 1 <= m; ++k) {
            for(int i = k; i + k < n; ++i)
                for(int j = k; j + k < m; ++j) {
                    for (int s = -k + 1; s <= k - 1; ++s) {
                        addOdd(i - k, j + s, i, j);
                        addOdd(i + k, j + s, i, j);
                        addOdd(i + s, j - k, i, j);
                        addOdd(i + s, j + k, i, j);
                    }
                    addOdd(i - k + 1, j - k + 1, i, j);
                    addOdd(i - k + 1, j + k - 1, i, j);
                    addOdd(i + k - 1, j - k + 1, i, j);
                    addOdd(i + k - 1, j + k - 1, i, j);

                    if (sx[i][j] == 0 && sy[i][j] == 0) ans = max(ans, 2 * k + 1);
                }
        }

        memset(sx, 0, sizeof sx);
        memset(sy, 0, sizeof sy);
        for(int i = 1; i <= n - 1; ++i)
                for(int j = 1; j <= m - 1; ++j) {
                    addEven(i - 1, j - 1, i, j);
                    addEven(i - 1, j, i, j);
                    addEven(i, j - 1, i, j);
                    addEven(i, j, i, j);
                }

        for(int k = 2; 2 * k <= n && 2 * k <= m; ++k) {
            for(int i = k; i <= n - k; ++i)
                for(int j = k; j <= m - k; ++j) {
                    for(int s = -k + 1; s <= k - 2; ++s) {
                        addEven(i - k, j + s, i, j);
                        addEven(i + k - 1, j + s, i, j);
                        addEven(i + s, j - k, i, j);
                        addEven(i + s, j + k - 1, i, j);    
                    }
                    if (k > 2) {
                        addEven(i - k + 1, j - k + 1, i, j);
                        addEven(i - k + 1, j + k - 2, i, j);
                        addEven(i + k - 2, j - k + 1, i, j);
                        addEven(i + k - 2, j + k - 2, i, j);
                    }

                    if (sx[i][j] == 0 && sy[i][j] == 0) ans = max(ans, 2 * k);
                }
        }


        printf("Case #%d: ", tc);
        if (ans == 0) puts("IMPOSSIBLE");
        else printf("%d\n", ans);



        cerr << "Solved: " << tc << endl;
    }
    
    return 0;
}
