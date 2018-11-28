/*
Author: Ahyangyi
Using Dev-Cpp with MinGW
*/

#include <stdio.h>
#include <string.h>

char names[100][200];
char q[1000][200];
int data[1001];
int dp[1001][100];

int main () {
    int t, n, m, i, j, k, ct;
    
    ct = 0;
    for (scanf("%d", &t); t > 0; t --) {
        scanf("%d", &n);
        fgets(names[0], 200, stdin);
        
        for (i = 0; i < n; i ++)
            fgets(names[i], 200, stdin);
        
        scanf("%d", &m);

        fgets(q[0], 200, stdin);
        for (i = 0; i < m; i ++)
            fgets(q[i], 200, stdin);

        for (i = 0; i < m; i ++) {
            for (j = 0; j < n; j ++)
                if (strcmp(names[j], q[i]) == 0)
                    break;
            data[i] = j;
            }
        data[m] = -1;
        
        for (i = 0; i <= m; i ++)
            for (j = 0; j < n; j ++)
                dp[i][j] = (i == 0 && data[0] != j) ? 0 : 1000000000;
        
        for (i = 0; i < m; i ++)
            for (j = 0; j < n; j ++)
                for (k = 0; k < n; k ++)
                    if (k != data[i + 1])
                        dp[i + 1][k] <?= dp[i][j] + (j != k);
        
        k = 1000000000;
        for (i = 0; i < n; i ++)
            k <?= dp[m][i];
        
        printf("Case #%d: %d\n", ++ct, k);
        }
    
    return 0;
    }
