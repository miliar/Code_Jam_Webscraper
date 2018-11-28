#include <cstdio>
#include <string>
#include <cmath>
#include <set>
#include <cstring>
using namespace std;

typedef long long LL;
set<LL> s;
LL ans;

int isq(LL a) {
    LL lo = 1, hi = 1073741830;
    while (lo <= hi) {
        LL mid = (lo + hi) / 2;
        LL tmp = mid * mid;
        if (tmp == a) return 1;
        if (tmp < a) lo = mid + 1;
        else hi = mid - 1;
    }
    return 0;
}

char buf[128], ansbuf[128];
int len;
int solve(int p, LL cur) {
    if (p == len) {
        if (isq(cur)) {
            ans = cur;
            printf("%s\n",ansbuf);
            // printf("%I64d\n",ans);
            // strcpy(ansbuf, buf);
            return 1;
        }
        return 0;
    }
    ansbuf[p] = buf[p];
    if (buf[p] == '1') {
        return solve(p+1, cur * 2 + 1);
    } else if (buf[p] == '0') {
        return solve(p+1, cur*2);
    } else {
        ansbuf[p] = '0';
        if (solve(p+1, cur*2)) return 1;
        ansbuf[p] = '1';
        return solve(p+1, cur*2+1);
    }
}

int main() {
    freopen("d-small-attempt0.in","r",stdin);
    freopen("d-small-0.out","w",stdout);
    int T, ca;
    /*
    while (scanf("%d",&T)) {
        printf("%d\n",isq(T));
    }
    */
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%s",buf);
        memset(ansbuf, 0, sizeof(ansbuf));
        len = strlen(buf);
        ans = -1;
        printf("Case #%d: ", ca);
        solve(0, 0);

    }
    return 0;
}
