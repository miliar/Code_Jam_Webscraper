#include <cstdio>
#include <algorithm>
#include <climits>
using namespace std;

void solve() {
    int xortotal = 0;
    int total = 0;
    int n;
    int candy[1005] = {};
    int m = INT_MAX;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &candy[i]);
        xortotal ^= candy[i];
        total += candy[i];
        m = min(m, candy[i]);
    }

    if (xortotal != 0) {
        printf("NO\n");
        return;
    }

    printf("%d\n", total - m);
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d: ", i+1);
        solve();
    }
    return 0;
}
