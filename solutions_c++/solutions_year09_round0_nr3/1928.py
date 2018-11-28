#include <cstdio>
#include <cstring>

const char *s_w = "welcome to code jam";
const int l_w = 19; //strlen(s_w);
const int M = 10000;
const int max_l_i = 500;
const int max_l_w = l_w;

char s_i[max_l_i + 2];
int l_i;

int dyn[max_l_i][max_l_w];

int cntw(int p_i, int p_w)
{
    if (p_w < 0)
        return 1;
    if (p_i < 0)
        return 0;
    int &r = dyn[p_i][p_w];
    if (r >= 0)
        return r;
    r = 0;
    r += cntw(p_i - 1, p_w);
    if (s_i[p_i] == s_w[p_w])
        r += cntw(p_i - 1, p_w - 1);
    r %= M;
    return r;
}

int main(void)
{
    int T;
    scanf("%d\n", &T);

    for (int t = 1 ; t <= T ; t++)
        {
            fgets(s_i, max_l_i + 1, stdin);
            l_i = strlen(s_i);
            for (int i = 0 ; i < l_i ; i++)
                for (int w = 0 ; w < l_w ; w++)
                    dyn[i][w] = -1;
            printf("Case #%d: %04d\n", t, cntw(l_i - 1, l_w - 1));
        }

    return 0;
}
