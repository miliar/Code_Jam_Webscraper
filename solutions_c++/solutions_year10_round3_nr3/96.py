/*
 * Sun May 23 17:40:04 CST 2010
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
using namespace std;
const int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

const int maxn = 1024;
int cases, cas = 1;
int n, m;
bool mat[maxn][maxn];
bool v[maxn][maxn];

int toInt(char ch) {
    if (isdigit(ch)) {
        return ch - '0';
    } else {
        return ch - 'A' + 10;
    }
}

bool check(int x, int y, int len) {
    if (x + len > n || y + len > m) {
        return false;
    }
    for (int i = x; i < x + len; ++i) for (int j = y; j < y + len; ++j) if (v[i][j]) {
        return false;
    }
    for (int i = x; i < x + len; ++i) for (int j = y; j < y + len; ++j) {
        if (i - 1 >= x && mat[i][j] == mat[i - 1][j]) {
            return false;
        }
        if (j - 1 >= y && mat[i][j] == mat[i][j - 1]) {
            return false;
        }
    }
    return true;
}

void erase(int x, int y, int len) {
    for (int i = x; i < x + len; ++i) for (int j = y; j < y + len; ++j) {
        v[i][j] = true;
    }
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            int index = 0;
            for (int j = 0; j < m / 4; ++j) {
                char ch; cin >> ch; int num = toInt(ch);
                for (int k = 3; k >= 0; --k) {
                    if ((num & (1 << k)) == 0) {
                        mat[i][index++] = false;
                    } else {
                        mat[i][index++] = true;
                    }
                }
            }
        }
//for (int i = 0; i < n; ++i) {
//    for (int j = 0; j < m; ++j) {
//        cout << (mat[i][j] ? 1 : 0) << " ";
//    }
//    cout << endl;
//}
        int mini = min(n, m);
        memset(v, false, sizeof(v));
        map<int, int> ans;
        while (true) {
            int x, y, maxi = -1; bool repeat = false;
            for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) for (int k = mini; k > 0; --k) if (check(i, j, k) && k > maxi) {
                maxi = k; x = i; y = j;
                repeat = true;
            }
            if (!repeat) {
                break;
            }
//see(x); see(y); see(maxi);
            erase(x, y, maxi);
            ans[maxi]++;
        }
        printf("Case #%d: %d\n", cas++, (int) ans.size());
        for (map<int, int>::reverse_iterator it = ans.rbegin(); it != ans.rend(); ++it) {
            printf("%d %d\n", it->first, it->second);
        }
    }
    return 0;
}
