#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
#include "set"
#include "utility"
using namespace std;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sof(x) sizeof(x)
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define maxn 15
const double eps = 1e-7;
int a[maxn], n;
double w, l;
double x[maxn], y[maxn], r[maxn];

bool isOK() {
    double xx = 0, yy = 0, yyy = r[a[0]];
    x[a[0]] = y[a[0]] = 0;
    for(int i = 1; i < n; i++) {
        if(xx + r[a[i]] + r[a[i-1]] > w + eps) {
            yy = yyy;
            xx = 0;
            x[a[i]] = 0;
            y[a[i]] = yyy + r[a[i]];
        } else {
            xx = x[a[i]] = xx + r[a[i]] + r[a[i-1]];
            if(yy > eps) y[a[i]] = yy + r[a[i]];
            else y[a[i]] = 0;
        }
        yyy = max(yyy, y[a[i]] + r[a[i]]);
        if(y[a[i]] > l) return false;
    }
    return true;
}

void solve() {
    do{
        if(isOK()) {
            for(int i = 0; i < n; i++) {
                printf("%.1f %.1f", x[i], y[i]);
                printf("%c", i + 1 < n ? ' ' : '\n');
            }
            break;
        }
    } while(next_permutation(a, a + n));
}
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("bout.txt", "w", stdout);
    int T, Case = 1;
    scanf("%d", &T);
    while(T--) {
        for(int i = 0; i < maxn; i++) a[i] = i;
        scanf("%d", &n);
        scanf("%lf%lf", &w, &l);
        for(int i = 0; i < n; i++) scanf("%lf", &r[i]);
        printf("Case #%d: ", Case++);
        solve();
    }
    return 0;
}
