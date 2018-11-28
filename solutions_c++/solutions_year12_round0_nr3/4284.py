#include <stdio.h>
#include <string.h>

bool good(int a, int b)
{
    char s[100], t[100];
    sprintf(s, "%d", a);
    sprintf(t, "%d", b);
    int n = strlen(s);
    for (int i = 0; i < n; i++)
        s[i + n] = s[i];
    for (int l = 1; l < n; l++) {
        for (int i = 0; i < n; i++)
            if (t[i] != s[i + l])
                goto next;
        return true;
next:
        ;
    }
    return false;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        int a, b, ans = 0;
        scanf("%d%d", &a, &b);
        for (int x = a; x < b; x++)
            for (int y = x + 1; y <= b; y++)
                if (good(x, y))
                    ans++;
        printf("Case #%d: %d\n", i, ans);
    }
}
