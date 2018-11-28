#include <stdio.h>
#include <memory.h>
#define MAX 110
int map[MAX][MAX],map2[MAX][MAX];
int main()
{
    int tt,num,t,i,j,k,ct,find;
    int a,b,c,d;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    scanf("%d",&tt);
    for (t = 1; t <= tt; t ++)
    {
        memset(map,0,sizeof(map));
        memset(map2,0,sizeof(map2));
        scanf("%d",&num);
        for (i = 0; i < num; i ++)
        {
            scanf("%d%d%d%d",&a,&b,&c,&d);
            for (j = b; j <= d; j ++)
            {
                for (k = a; k <= c; k ++)
                {
                    map[j][k] = 1;
                }

            }
        }
        ct = 0;
        find = 1;
        while (find)
        {
            find = 0;
            memset(map2,0,sizeof(map2));
            for (i = 1; i < 110; i ++)
            {
                for (j = 1; j < 110; j ++)
                {
                    if (map[i][j])
                    {
                        find = 1;
                    }
                    if (map[i][j] && (map[i - 1][j] || map[i][j - 1]))
                    {
                        map2[i][j] = 1;
                    }
                    else if (map[i - 1][j] && map[i][j - 1])
                    {
                        map2[i][j] = 1;
                    }
                }
            }
            if (!find)
                break;
            ct ++;
            for (i = 1; i < 110; i ++)
            {
                for (j = 1; j < 110; j ++)
                {
                    map[i][j] = map2[i][j];
                }
            }

        }
        printf("Case #%d: %d\n",t,ct);
    }
    return 0;
}
