#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int dd[600][600];
int tx[600][600];
int ty[600][600];
long long ddsumh[600][600];
long long tsumhx[600][600];
long long tsumhy[600][600];
long long ddsumt[600][600];
long long tsumtx[600][600];
long long tsumty[600][600];
int r, c, d;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int i, j;
        scanf("%d %d %d", &r, &c, &d);

        char buffer[600];
        for (i = 1; i <= r; i++)
        {
            scanf("%s", buffer);
            for (j = 1; j <= c; j++)
            {
                d = buffer[j-1] - '0';
                dd[i][j] = d;
                tx[i][j] = i * d;
                ty[i][j] = j * d;
            }
        }

        for (i = 0; i <= r; i++)
        {
            ddsumh[i][0] = 0;
            tsumhx[i][0] = 0;
            tsumhy[i][0] = 0;
        }
        for (j = 0; j <= c; j++)
        {
            ddsumh[0][j] = 0;
            tsumhx[0][j] = 0;
            tsumhy[0][j] = 0;
        }
        for (i = 1; i <= r; i++)
        {
            for (j = 1; j <= c; j++)
            {
                ddsumh[i][j] = ddsumh[i][j-1] + dd[i][j];
                tsumhx[i][j] = tsumhx[i][j-1] + tx[i][j];
                tsumhy[i][j] = tsumhy[i][j-1] + ty[i][j];
            }
        }

        for (i = 0; i <= r; i++)
        {
            ddsumt[i][0] = 0;
            tsumtx[i][0] = 0;
            tsumty[i][0] = 0;
        }
        for (j = 0; j <= c; j++)
        {
            ddsumt[0][j] = 0;
            tsumtx[0][j] = 0;
            tsumty[0][j] = 0;
        }
        for (i = 1; i <= r; i++)
        {
            for (j = 1; j <= c; j++)
            {
                ddsumt[i][j] = ddsumt[i-1][j] + ddsumh[i][j];
                tsumtx[i][j] = tsumtx[i-1][j] + tsumhx[i][j];
                tsumty[i][j] = tsumty[i-1][j] + tsumhy[i][j];
            }
        }

        int k = r;
        if (c < r) k = c;
        for (;k>=3;k--)
        {
            for (i = 0; i + k <= r; i++)
            {
                for (j = 0; j + k <= c; j++)
                {
                    long long w = (ddsumt[i+k][j+k] - ddsumt[i][j+k] - ddsumt[i+k][j] + ddsumt[i][j]) - dd[i+1][j+1] - dd[i+k][j+1] - dd[i+1][j+k] - dd[i+k][j+k];
                    if (w % 2 == 1 && k % 2 == 0) continue;
                    long long espectedx = ((i + i + k + 1) * w/ 2);
                    long long espectedy = ((j + j + k + 1) * w/ 2);
                    long long ttx = (tsumtx[i+k][j+k] - tsumtx[i][j+k] - tsumtx[i+k][j] + tsumtx[i][j]) - tx[i+1][j+1] - tx[i+k][j+1] - tx[i+1][j+k] - tx[i+k][j+k];
                    long long tty = (tsumty[i+k][j+k] - tsumty[i][j+k] - tsumty[i+k][j] + tsumty[i][j]) - ty[i+1][j+1] - ty[i+k][j+1] - ty[i+1][j+k] - ty[i+k][j+k];
                    if (espectedx == ttx && espectedy == tty)
                    {
                        break;
                    }
                }
                if (j + k <= c)
                    break;
            }
            if (i + k <= r)
                break;
        }

        if (k < 3)
        {
            printf("Case #%d: IMPOSSIBLE\n", t+1);
        }
        else
        {
            printf("Case #%d: %d\n", t+1, k);
        }
    }
    return 0;
}
