/*
 * Sat May  7 12:21:06 CST 2011
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
#include <numeric>
using namespace std;
const int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

int cases, cas = 1;
const int maxn = 1024;
const int maxm = 1 << 20;
int n, nums[maxn], sum, xsum;
int mem[2][maxm];

int main() {
    for (scanf("%d", &cases); cases--; ++cas) {
        scanf("%d", &n); sum = 0; xsum = 0; for (int i = 0; i < n; ++i) {
            scanf("%d", &nums[i]); sum += nums[i]; xsum ^= nums[i];
        }
        int now = 0, next = 1; memset(mem[now], 0xff, sizeof(mem[now])); mem[now][0] = 0;
        for (int k = 0; k < n; ++k) {
            memcpy(mem[next], mem[now], sizeof(mem[next]));
            for (int i = 0; i < maxm; ++i) if (mem[now][i] >= 0) {
                int& val = mem[next][i ^ nums[k]]; if (mem[now][i] + nums[k] < sum && mem[now][i] + nums[k] > val) {
                    val = mem[now][i] + nums[k];
                }
            }
            now = next; next ^= 1;
        }
        int ans = -1; for (int i = 0; i < maxm; ++i) if ((xsum ^ i) == i) {
            ans = max(ans, mem[now][i]);
        }
        if (ans >= 0) {
            printf("Case #%d: %d\n", cas, ans);
        } else {
            printf("Case #%d: NO\n", cas);
        }
    }
    return 0;
}
