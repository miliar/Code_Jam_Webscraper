#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#define sys system("pause")
using namespace std;
const double eps = 1e-15;
int a[2000010];
int n, d;

inline int sig(double k) {
    return k < -eps ? -1 : k > eps;
}

bool check(double x) {
    double cur = a[0] - x;
    for (int i = 1; i < n; ++i) {
        double pos = a[i] - x;
        if (sig(pos - cur - d) > 0) {
            cur = pos;
        } else {
            if (sig(a[i] + x - cur - d) > 0) {
                cur = cur + d;
            } else {
                return false;
            }
        }
    }
    return true;
}

int main() {
  //      freopen("b.in", "r", stdin);
  //  freopen("b.txt", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        int tot = 0, p, v;
        scanf("%d%d", &n, &d);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &p, &v);
            while (v--) {
                a[tot++] = p;
            }
        }
        n = tot;
        sort(a, a + n);
        double lf = 0, rg = 1e18, mid;
        int num = 0;
        while (sig(rg - lf) > 0 && ++num < 100) {
            mid = (lf + rg) / 2.0;
            if (check(mid)) rg = mid;
            else lf = mid;
        }
        printf("Case #%d: %.10lf\n", cas++, mid);
    }
 //   sys;
    return 0;
}
