#include <cstdio>
#include <cstring>

char rp[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g',
              'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char s[110];
int l, T;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("solve.out", "w", stdout);
    scanf("%d\n", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        gets(s);
        l = strlen(s);
        printf("Case #%d: ", cas);
        for (int i = 0; i < l; i++)
            if (s[i] == ' ') printf("%c", s[i]);
            else printf("%c", rp[s[i] - 'a']);
        printf("\n");
    }
    return 0;
}
