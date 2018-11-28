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
const int infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

int cases, cas = 1;
int n;
char str[1024], tmp[1024];

int calc(int len, char* str) {
    int ret = 0;
    for (int i = 1; i < len; ++i) if (str[i] != str[i - 1]) {
        ret++;
    }
    return ret + 1;
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%s", &n, str);
        int a[16], len = strlen(str);
        tmp[len] = 0;
        for (int i = 0; i < n; ++i) {
            a[i] = i;
        }
        int ans = inf;
        do {
            for (int start = 0; start < len; start += n) {
                for (int i = 0; i < n; ++i) {
                    tmp[start + i] = str[start + a[i]];
                }
            }
            ans = min(ans, calc(len, tmp));
        } while (next_permutation(a, a + n));
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
