#include <stdio.h>
#include <stdlib.h>

int tree[10001];
int change[10001];
int dp[10001][2]; 
const int INF = 1000000;

int main() {
    int i, j,T,t, m,v;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T); 
    for (t=1;t<=T;t++)
    {
        scanf("%d%d",&m,&v);
        for (i = 1; i <= (m-1)/2; i++)
        {
            scanf("%d%d", tree+i, change+i);
        }    
        for (; i <= m; i++)
        {
            scanf("%d", tree+i);
            dp[i][0] = dp[i][1] = INF;
            dp[i][tree[i]] = 0;
        }    
        for (i = (m-1)/2; i >= 1; i--)
        {
            dp[i][0] = dp[i][1] = INF;
            if (change[i] == 0)
            {
                if (tree[i] == 1)
                {
                    dp[i][0] <?= dp[2*i][1] + dp[2*i+1][0];
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][0];
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][1];
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][1];
                }
                else
                {
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][0];
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][0];
                    dp[i][1] <?= dp[2*i][0] + dp[2*i+1][1];
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][1];
                }         
            }  
            else
            {
                if (tree[i] == 1)
                {
                    dp[i][0] <?= dp[2*i][1] + dp[2*i+1][0];
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][0];
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][1];
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][1];
                    
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][0] + 1;
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][0] + 1;
                    dp[i][1] <?= dp[2*i][0] + dp[2*i+1][1] + 1;
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][1] + 1;
                    
                }
                else
                {
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][0];
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][0];
                    dp[i][1] <?= dp[2*i][0] + dp[2*i+1][1];
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][1];
                    
                    dp[i][0] <?= dp[2*i][1] + dp[2*i+1][0] + 1;
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][0] + 1;
                    dp[i][0] <?= dp[2*i][0] + dp[2*i+1][1] + 1;
                    dp[i][1] <?= dp[2*i][1] + dp[2*i+1][1] + 1;
                }   
            }      
        }    
        if (dp[1][v] < INF)
            printf("Case #%d: %d\n",t,dp[1][v] );
        else
            printf("Case #%d: IMPOSSIBLE\n",t);
    }     
    
    
    //system("pause");
    return 0; 
}

