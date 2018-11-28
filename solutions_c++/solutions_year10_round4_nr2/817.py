#include <cstdio>
#include <cstring>

int p;
int m[1200];

int main()
{
    FILE *fin = fopen("Bsmall.in","r");
    FILE *fout = fopen("Bsmall.out","w");
    int t, i, j, k, ans, a, ca = 0, n, mm;
    bool b;
    fscanf(fin,"%d", &t);
    while (t-- > 0)
    {
        fscanf(fin,"%d", &p);
        for (i = 1; i <= (1 << p); i++) fscanf(fin,"%d", &m[i]);
        for (i = 1; i <= (1 << p) - 1; i++) fscanf(fin,"%d", &a);
        ans = 0;
        n = 1 << p;
        for (i = 1; i <= p; i++)
        {
            mm = 1 << i;
            for (j = 1; j <= n; j+=mm)
            {
                b = true;
                for (k = j; k <= (j + mm - 1); k++) b = b && (m[k] > 0);
                if (b)
                {
                    for (k = j; k <= (j + mm - 1); k++) m[k]--;
                    ans++;
                }
            }
        }
        fprintf(fout,"Case #%d: %d\n", ++ca, (n - 1 - ans));
    }
    return 0;
}
