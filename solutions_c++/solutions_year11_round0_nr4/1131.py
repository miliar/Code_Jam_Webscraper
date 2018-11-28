/*
 * Sat May  7 10:39:09 CST 2011
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
const double eps = 1e-7;
const double pi = acos(-1.0);

const int maxn = 1024;
int cases, cas = 1;
double per[maxn], pAllNot[maxn];

void init() {
    per[0] = 1.0; per[1] = 1.0; for (int i = 2; i < maxn; ++i) {
        per[i] = per[i - 1] / i;
    }
    pAllNot[0] = 0.0; pAllNot[1] = 0.0; for (int n = 2; n < maxn; ++n) {
        pAllNot[n] = 1.0; for (int k = 1; k <= n - 1; ++k) {
            pAllNot[n] -= pAllNot[n - k] * per[k];
        }
        pAllNot[n] -= per[n];
    }
}

int n;
int perm[maxn];
bool used[2][maxn];
double mem[2][maxn];

int main() {
    init();
    for (scanf("%d", &cases); cases--; ++cas) {
cerr << "case " << cas << endl;
        scanf("%d", &n); for (int i = 0; i < n; ++i) {
            scanf("%d", &perm[i]);
        }
        int ready = 0; for (int i = 0; i < n; ++i) if (perm[i] - 1 == i) {
            ready++;
        }
        int now = 0, next = 1; for (int i = 0; i <= n; ++i) {
            used[now][i] = false; mem[now][i] = 0.0;
        }
        used[now][ready] = true; mem[now][ready] = 1.0; double ans = 0.0; while (true) {
            double sum = 0.0; for (int i = 0; i < n; ++i) if (used[now][i]) {
                sum += mem[now][i];
            }
            ans += sum;
            if (sum < eps) {
                break;
            }
            for (int i = 0; i <= n; ++i) {
                used[next][i] = false; mem[next][i] = 0.0;
            }
            for (int i = 0; i < n; ++i) if (used[now][i]) {
                int dispos = n - i;
                used[next][i] = true; mem[next][i] += mem[now][i] * pAllNot[dispos];
                used[next][n] = true; mem[next][n] += mem[now][i] * per[dispos];
                for (int k = 1; k < dispos; ++k) {
                    used[next][i + k] = true; mem[next][i + k] += mem[now][i] * per[k] * pAllNot[dispos - k];
                }
            }
            now = next; next ^= 1;
        }
        printf("Case #%d: %lf\n", cas, ans);
    }
    return 0;
}
