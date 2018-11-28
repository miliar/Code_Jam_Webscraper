#include <iostream>
#include <cstring>
#include <queue>

#define N 64
using namespace std;

int main()
{
    int t, test = 1;
    int n, m;
    int i, j;
    char map[N][N];
    bool flag, tag;

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    scanf("%d", &t);
    while (t--)
    {
        scanf("%d%d", &n, &m);
        for (i=0; i<n; i++)
            scanf("%s", map[i]);

        flag = 1;
        tag = 1;
        while (flag)
        {
            flag = 0;
            for (i=0; i<n && tag && !flag; i++)
                for (j=0; j<m; j++)
                {
                    if (map[i][j] == '#')
                    {
                        if (i == n - 1 || j == m - 1)
                        {
                            tag = 0;
                            break;
                        }
                        if (map[i+1][j] != '#' || map[i][j+1] != '#' || map[i+1][j+1] != '#')
                        {
                            tag = 0;
                            break;
                        }
                        map[i][j] = '/';
                        map[i][j+1] = '\\';
                        map[i+1][j+1] = '/';
                        map[i+1][j] = '\\';
                        flag = 1;
                        break;
                    }
                }
        }

        printf("Case #%d:\n", test++);
        if (!tag)
            printf("Impossible\n");
        else
        {
            for (i=0; i<n; i++)
                printf("%s\n", map[i]);
        }
    }

    return 0;
}
