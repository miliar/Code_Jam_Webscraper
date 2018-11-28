/*
 * Sun May 22 17:13:19 CST 2011
 *
 * @Author: Xiantao Jiao
 */
#define see(n) cerr << #n << " = " << n << endl
#define seeArray(n, a) cerr << #a << " = ";\
    for (int __i__ = 0; __i__ < (int) n; ++__i__)\
        cerr << a[__i__] << " ";\
    cerr << endl;
#define seeArray2(n, m, a) cerr << #a << " = " << endl;\
    for (int __i__ = 0; __i__ < (int) n; ++__i__) {\
        for (int __j__ = 0; __j__ < (int) m; ++__j__)\
            cerr << a[__i__][__j__] << " ";\
        cerr << endl;\
    }
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <sstream>
#include <cctype>
#include <ctime>
#include <numeric>
using namespace std;
const int inf = 1000000000;
const double eps = 1e-10;

const int maxn = 64;
int cases, cas = 1;
int n, m;
char board[maxn][maxn];

int main() {
    for (scanf("%d", &cases); cases--; cas++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", board[i]);
        }
        bool ok = true;
        for (int i = 0; i < n && ok; ++i) for (int j = 0; j < m && ok; ++j) if (board[i][j] == '#') {
            if (i + 1 >= n || j + 1 >= m || board[i + 1][j] != '#' || board[i][j + 1] != '#' || board[i + 1][j + 1] != '#') {
                ok = false;
            } else {
                board[i][j] = '/'; board[i][j + 1] = '\\'; board[i + 1][j] = '\\'; board[i + 1][j + 1] = '/';
            }
        }
        printf("Case #%d:\n", cas);
        if (ok) {
            for (int i = 0; i < n; ++i) {
                printf("%s\n", board[i]);
            }
        } else {
            printf("Impossible\n");
        }
    }
    return 0;
}
