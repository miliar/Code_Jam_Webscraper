#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        int x = 1, y = 1;
        int tx = 0, ty = 0;
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            char s[5];
            int pos;
            scanf("%s %d", s, &pos);
            if (s[0] == 'O') {
                tx = max(ty, tx + abs(pos - x)) + 1;
                x = pos;
            } else {
                ty = max(tx, ty + abs(pos - y)) + 1;
                y = pos;
            }
        }
        printf("Case #%d: %d\n", ++cas, max(tx, ty));
    }
    return 0;
}
