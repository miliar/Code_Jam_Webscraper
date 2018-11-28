#include <cstdio>
#include <algorithm>
using namespace std;

void solve() {
    int n;
    int a[1005] = {};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        a[i]--;
    }

    int hits = n;
    for (int i = 0; i < n; i++) {
        if (a[i] == i) {
            hits--;
        }
    }

    printf("%d.000000\n", hits);
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
