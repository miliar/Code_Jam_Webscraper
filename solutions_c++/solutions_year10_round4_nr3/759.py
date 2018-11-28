#include <cstdio>
#include <cstring>

const int w = 150;
const int m = 400;
int r;
bool b[510][510], c[510][510];

int main()
{
    FILE *fin = fopen("Csmall.in","r");
    FILE *fout = fopen("Csmall.out", "w");
    int t, ca = 0, i, j, k, ans;
    int x1, y1, x2, y2;
    bool q;
    fscanf(fin, "%d", &t);
    while (t-- > 0)
    {
        fscanf(fin, "%d", &r);
        memset(b, false, sizeof(b));
        for (i = 1; i <= r; i++)
        {
            fscanf(fin, "%d%d%d%d", &x1, &y1, &x2, &y2);
            for (j = x1; j <= x2; j++)
            {
                for (k = y1; k <= y2; k++) b[j + w][k + w] = true;
            }
        }
        ans = 0;
        while (true)
        {
            q = false;
            for (j = 1; j <= m; j++)
            {
                for (k = 1; k <= m; k++) q = q || b[j][k];
            }
            if (q)
            {
                ans++;
                for (j = 2; j <= m; j++)
                {
                    for (k = 2; k <= m; k++)  if (b[j][k])
                    {
                        c[j][k] = b[j - 1][k] || b[j][k - 1];
                    } else c[j][k] = b[j - 1][k] && b[j][k - 1];
                }
                for (j = 1; j <= m; j++)
                {
                    for (k = 1; k <= m; k++) b[j][k] = c[j][k];
                }
            } else break;
        }
        fprintf(fout, "Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}
