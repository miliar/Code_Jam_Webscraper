#include <cstdio>

const int max_d = 5000;
const int max_l = 15;

char s[500];

int dic[max_d][max_l];
int pat[max_l];

int main(void)
{
    int L, D, T;

    scanf("%d%d%d", &L, &D, &T);

    for (int d = D - 1 ; d >= 0 ; d--)
        {
            scanf("%s", s);
            for (int i = 0 ; i < L ; i++)
                dic[d][i] = 1 << (s[i] - 'a');
        }
    for (int t = 1 ; t <= T ; t++)
        {
            scanf("%s", s);
            int j = 0;
            for (int i = 0 ; i < L ; i++, j++)
                {
                    pat[i] = 0;
                    if (s[j] == '(')
                        while (s[++j] != ')')
                            pat[i] |= 1 << (s[j] - 'a');
                    else
                        pat[i] = 1 << (s[j] - 'a');
                }
            int n = 0;
            for (int d = D - 1 ; d >= 0 ; d--)
                {
                    int i;
                    for (i = L - 1 ; i >= 0 ; i--)
                        if (!(dic[d][i] & pat[i]))
                            break;
                    if (i < 0)
                        n++;
                }
            printf("Case #%d: %d\n", t, n);
        }

    return 0;
}
