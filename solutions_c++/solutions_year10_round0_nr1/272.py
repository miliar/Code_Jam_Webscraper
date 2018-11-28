/*
 * Sat May  8 14:00:29 KST 2010
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

int cases, cas = 1;

int main() {
    long long n, k;
    for (scanf("%d", &cases); cases--; ) {
        scanf("%lld%lld", &n, &k);
        long long cnt = (1LL << n);
        if (k % cnt == cnt - 1) {
            printf("Case #%d: ON\n", cas++);
        } else {
            printf("Case #%d: OFF\n", cas++);
        }
    }
    return 0;
}
