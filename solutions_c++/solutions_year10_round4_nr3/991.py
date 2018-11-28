#include <iostream>
#include <cstring>
using namespace std;

int mat[105][105], old[105][105], T, R, x1, x2, y1, y2, num;

void doans()
{
    /*
    for(int i = 1; i <= 6; i++)
    {
        for(int j = 1; j <= 6; j++) printf("%d", mat[i][j]);
        printf("\n");
    }
    printf("\n");
    */

    for(int i = 1; i <= 100; i++)
        for(int j = 1; j <= 100; j++)
        {
            bool u = true, l = true;
            if(i == 1 || old[i - 1][j] == 0) u = false;
            if(j == 1 || old[i][j - 1] == 0) l = false;

            if(!u && !l && old[i][j] == 1) mat[i][j] = 0, num--;
            else
            if(u && l && old[i][j] == 0) mat[i][j] = 1, num++;
        }

    //printf("%d\n", num);
}

int main()
{
    scanf("%d", &T);
    int Case = 1;
    while(T--)
    {
        memset(mat, 0, sizeof(mat));
        scanf("%d", &R);
        num = 0;

        for(int i = 1; i <= R; i++)
        {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);

            for(int j = x1; j <= x2; j++)
                for(int k = y1; k <= y2; k++)
                {
                    if(mat[k][j] == 0)
                        mat[k][j] = 1, num++;
                }
        }

        int ans = 0;
        while(num != 0)
        {
            memcpy(old, mat, sizeof(mat));
            ans++;
            doans();
        }

        printf("Case #%d: %d\n", Case, ans);
        Case++;
    }

    return 0;
}