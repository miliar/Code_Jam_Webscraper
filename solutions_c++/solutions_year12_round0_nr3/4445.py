#include <stdio.h>

int base[10];

bool recy(int n, int m)
{
    int i, len;
    for(len = 1; ; ++len) {
        if(m / base[len] == 0)
            break;
    }
    for(i = 1; i < len; ++i) {
        if(m / base[len - i] == n % base[i] && m % base[len - i] == n / base[i])
            return true;
    }
    return false;
}

int main()
{
    int T, a, b, i, j, k, ans;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out.txt", "w", stdout);
    scanf("%d", &T);
    base[1] = 10;
    for(i = 2; i < 5; ++i)
        base[i] = base[i - 1] * 10;
    for(k = 0; k < T; ++k) {
        scanf("%d%d", &a, &b);
        ans = 0;
        for(i = a + 1; i <= b; ++i) {
            for(j = a; j < i; ++j) {
                if(recy(i, j))
                    ++ans;
            }
        }
        printf("Case #%d: %d\n", k + 1, ans);
    }
    return 0;
}
