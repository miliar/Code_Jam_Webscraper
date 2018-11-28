#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int tott, n;
    scanf("%d", &tott);
    for (int curt = 1; curt <= tott; ++curt) {
        scanf("%d", &n);
        int ans = 0;
        for (int i = 1, j; i <= n; ++i) {
            scanf("%d", &j);
            ans += j != i;
        }
        printf("Case #%d: %d.000000\n", curt, ans);
    }
    return 0;
}

