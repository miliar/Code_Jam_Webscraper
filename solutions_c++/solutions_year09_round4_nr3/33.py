#include <stdio.h>
#include <string.h>

int n, m;
int num[200][200];
int data[200][200];
int used[200], op[200];

int dfs (int x)
{
    used[x] = 1;
    for (int i = 0; i < n; i ++)
        if (data[x][i] && op[i] == -1)
        {
            op[i] = x;
            return 1;
        }
    for (int i = 0; i < n; i ++)
        if (data[x][i] && !used[op[i]] && dfs(op[i]))
        {
            op[i] = x;
            return 1;
        }
    
    return 0;
}

int main ()
{
    int t, ct = 0;
    
    for (scanf("%d", &t); t > 0; t --)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                scanf("%d", num[i] + j);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < n; j ++)
            {
                data[i][j] = 1;
                for (int k = 0; k < m; k ++)
                    if (num[i][k] <= num[j][k])
                        data[i][j] = 0;
            }
        
        int ans = n;
        memset(op, -1, sizeof(op));
        for (int i = 0; i < n; i ++)
        {
            memset(used, 0, sizeof(used));
            ans -= dfs (i);
        }
        
        printf("Case #%d: %d\n", ++ct, ans);
    }
    
    return 0;
}
