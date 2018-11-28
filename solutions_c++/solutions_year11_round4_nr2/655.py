#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int r, c, d;
char str[1000];
int x[1000][1000];
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.txt","w",stdout);
    int t;scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        scanf("%d%d%d", &r, &c, &d);
        for(int i = 0; i < r; i++)
        {
            scanf("%s", str);
            for(int j = 0; j < c; j++)
            {
                x[i][j] = d + str[j] - '0';
            }
        }
        int ans = -1;
        for(int i = 0; i + 3 - 1 < r; i++)
            for(int j = 0; j + 3 - 1 < c; j++)
            {
                int k = 3;
                while(i + k - 1 < r && j + k - 1 < c)
                {
                    int len = k / 2;
                    double midx = i + len, midy = j + len;
                    if (k % 2 == 0)
                    {
                        midx -= 0.5;
                        midy -= 0.5;
                    }
                    double sumx = 0, sumy = 0;
                    for(int ii = i; ii < i + k; ii++)
                        for(int jj = j; jj < j + k; jj++)
                        {
                            if (ii == i && jj == j) continue;
                            if (ii == i + k - 1 && jj == j) continue;
                            if (ii == i && jj == j + k - 1) continue;
                            if (ii == i + k - 1 && jj == j + k - 1) continue;
                            sumx += x[ii][jj] * (ii * 1.0 - midx);
                            sumy += x[ii][jj] * (jj * 1.0 - midy);
                        }
                    if (sumx == 0 && sumy == 0 && k > ans) ans = k;
                    k++;
                }
            }
        printf("Case #%d: ", tt);
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}
