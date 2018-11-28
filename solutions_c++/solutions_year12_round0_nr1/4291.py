#include <cstdio>
#include <cstring>

char to[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
    'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int T;
char str[110];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    getchar();
    for (int cas = 1; cas <= T; ++cas)
    {
        gets(str);
        printf("Case #%d: ", cas);
        for (int j = 0; str[j]; ++j)
        {
            if (str[j] >= 'a' && str[j] <= 'z')
                printf("%c", to[str[j] - 'a']);
            else printf("%c", str[j]);
        }
        puts("");
    }
    return 0;
}