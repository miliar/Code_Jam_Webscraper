#include <cstdio>
#include <algorithm>
using namespace std;

void solve() {
    int n;
    long long d[10005] = {}, len[10005] = {};
    long long r[10005] = {};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", d+i, len+i);
    }
    scanf("%lld", d+n);

    len[0] = d[0];
    r[0] = d[0];

    for (int i = 0; i < n; i++) {
        long long reach = r[i];
        int next = i+1;

        if (reach + d[i] >= d[n]) {
            printf("YES\n");
            return;
        }

        while (next < n && d[i] + reach >= d[next]) {
            long long test_reach = min(len[next], d[next] - d[i]);
            if (r[next] < test_reach) {
                r[next] = test_reach;
            }

            next++;
        }
    }

    printf("NO\n");
}

int main() {
    int nt;
    scanf("%d", &nt);
    for (int i = 0; i < nt; i++) {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}