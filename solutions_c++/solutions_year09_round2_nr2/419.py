#include <cstdio>

char s[32];
int digs[10];

inline void next_number(void)
{
    int i = 1;
    while (s[++i]);
    i--;
    for (; s[i+1] <= s[i] ; i--)
        digs[s[i] - '0']++;
    int c = s[i] - '0';
    digs[c]++;
    while (!digs[++c]);
    s[i] = '0' + c;
    digs[c]--;
    for (i++, c = 0 ; s[i] ; i++)
        {
            for (; !digs[c] ; ++c);
            s[i] = '0' + c;
            digs[c]--;
        }
}

int main(void)
{
    int T;
    scanf("%d\n", &T);

    for (int t = 1 ; t <= T ; t++)
        {
            for (int d = 9 ; d >= 0 ; d--)
                digs[d] = 0;
            s[0] = '0';
            scanf("%s", s + 1);
            next_number();
            printf("Case #%d: %s\n", t, *s == '0' ? s + 1 : s);
        }

    return 0;
}
