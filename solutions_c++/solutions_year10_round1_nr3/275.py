#include <cstdio>
#include <algorithm>
using namespace std;

bool dfs(int a, int b) {
    if (a < b) swap(a, b);
    if (b == a) return 0;
    int k = a / b;
    if (k > 1)
        return 1;
    k = dfs(b, a - b);
    return 1 - k;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t, a1, a2, a, b1, b2, b, cnt, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
        cnt = 0;
        for (a = a1; a <= a2; ++a)
            for (b = b1; b <= b2; ++b)
                if (dfs(a, b))
                    ++cnt;
        printf("Case #%d: %d\n", ++cas, cnt);
    }
    return 0;
}
