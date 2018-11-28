#include <stdio.h>
#include <string.h>

const char st[] = "welcome to code jam";
const int maxl = 500 + 10;

char s[maxl];
int cnt[30];

void print(int x)
{
    if (x < 1000) printf("0");
    if (x < 100) printf("0");
    if (x < 10) printf("0");
    printf("%d\n", x);
}

int main(void)
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int lst = strlen(st);
    
    int tot;
    scanf("%d", &tot);
    for (int cas = 1; cas <= tot; ++cas) {
        do {
            gets(s);
        } while (strlen(s) == 0);

        int ls = strlen(s);
        memset(cnt, 0, sizeof cnt);
        for (int i = 0; i < ls; ++i)
        for (int j = lst-1; j >= 0; --j)
            if (s[i] == st[j]) {
                if (j == 0) cnt[j] = (cnt[j]+1) % 10000;
                else cnt[j] = (cnt[j]+cnt[j-1]) % 10000;
            }
        printf("Case #%d: ", cas);
        print(cnt[lst-1]);
    }
    return 0;
}
