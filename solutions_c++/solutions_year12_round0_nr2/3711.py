#include <cstdio>

int main() {
    int t, n, s, d, v, a, b, c = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d%d", &n, &s, &d);
        a = b = 0;
        for(int i = 0; i < n; i++) {
            scanf("%d", &v);
            if(v >= 3 * d - 2)
                a++;
            else if(v >= 3 * d - 4 && v >= d)
                b++;
        }
        printf("Case #%d: %d\n", ++c, a + ((b>s)?s:b));
    }
}
