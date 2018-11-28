#include <cstdio>
using namespace std;

int main() {
    int t, n, s, p, ts[110], a, b;
    
    scanf("%d ", &t);
    for (int x = 1; x <= t; x++) {
        scanf("%d %d %d", &n, &s, &p);
        int y = 0;
        for (int i = 1; i <= n; i++) {
            scanf("%d", &ts[i]);
            if (ts[i] % 3 == 0) {
                a = b = ts[i]/3;
            } else if (ts[i] % 3 == 1) {
                a = ts[i]/3 + 1;
                b = ts[i]/3;
            } else {
                a = b = ts[i]/3 + 1;
            }
            
            if (a >= p) {
                y++;
            } else if (s && (a > 0) && (a == b) && (a + 1) >= p) {
                y++;
                s--;
            }
        }
        printf("Case #%d: %d\n", x, y);
    }
}
