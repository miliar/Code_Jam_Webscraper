#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int b[512][512];
int c[512][512];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);

    for (int i0 = 1; i0 <= T; i0++)
    {
        int n, m;
        scanf("%d%d ", &m, &n);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n / 4; j++)
            {
                int w;
                scanf("%1X", &w);
                int st = 8;
                for (int g = 0; g < 4; g++)
                {
                    b[i][j * 4 + g] = w % (st * 2) / st;
                    st /= 2;
                }
            }
        for (int i = 0; i < m; i++)
        {
            int j = 0;
            while (j < n)
            {
                int w = 1;
                while ((j < n - 1)&&(b[i][j] != b[i][j + 1]))
                {
                    j++;w++;
                }
                for (int g = j - w + 1; g <= j; g++)
                    c[i][g] = j - g + 1;
                j++;
            }
        }
        int s[513];
        for (int i = 0; i <= min(n, m); i++)
            s[i] = 0;
        for (int r = min(n, m); r > 0; r--)
        {
            for (int i = 0; i < m - r + 1; i++)
                for (int j = 0; j < n - r + 1; j++)
                    if ((c[i][j] >= r)&&(b[i][j] != -1))
                    {
                        bool ind = true;
                        for (int g = i + 1; g < i + r; g++)
                            if ((b[g - 1][j] == b[g][j])||(c[g][j] < r)||(b[g][j] == -1)) { ind = false; break;}
                        if (ind)
                        {
                            s[r]++;
                            for (int x = i; x < i + r; x++)
                                for (int y = j; y < j + r; y++)
                                    b[x][y] = -1;
                            for (int x = i; x < i + r; x++)
                            {
                                int y = j - 1;
                                if (b[x][y] == -1) continue;
                                while (y >= 0)
                                {
                                    c[x][y] = j - y;
                                    if ((y == 0)||(b[x][y] == b[x][y - 1])||(b[x][y - 1] == -1)) break;
                                    y--;
                                }
                            }
                        }
                    }

        }
        int w = 0;
        for (int i = min(n, m); i > 0; i--)
            if (s[i] != 0) w++;
        printf("Case #%d: %d\n", i0, w);
        for (int i = min(n, m); i > 0; i--)
            if (s[i] != 0) printf("%d %d\n", i, s[i]);
    }
    return 0;
}
