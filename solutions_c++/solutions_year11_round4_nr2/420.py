#include "stdio.h"
int r, c, d;
char input[1000];
long myans[100][100];
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.txt","w",stdout);
    int t;scanf("%d", &t); int cnt = 1;
    while(t--)
    {
        scanf("%d%d%d", &r, &c, &d);
        for(int i = 0; i < r; i++)
        {
            scanf("%s", input);
            for(int j = 0; j < strlen(input); j++)
                myans[i][j] = d + input[j] - '0';
        }
        int flag = -1;
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
            {
                int k = 3;
                while(i + k <= r && j + k <= c)
                {
                    double xx = i + k * 0.5 - 0.5, yy = j + k * 0.5 - 0.5;
                    double sumx = 0, sumy = 0;
                    for(int ii = i; ii < i + k; ii++)
                        for(int jj = j; jj < j + k; jj++)
                        {
                            if (ii == i && jj == j
                            ||ii == i + k - 1 && jj == j
                            ||ii == i && jj == j + k - 1
                            ||ii == i + k - 1 && jj == j + k - 1) continue;
                            sumx += myans[ii][jj] * (ii * 1.0 - xx);
                            sumy += myans[ii][jj] * (jj * 1.0 - yy);
                        }
                    if (sumx == 0 && sumy == 0 && k > flag) flag = k;
                    k++;
                }
            }
        printf("Case #%d: ", cnt++);
        if (flag == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", flag);
    }
}
