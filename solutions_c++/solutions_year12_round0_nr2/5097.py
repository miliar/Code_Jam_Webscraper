#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int oo = (1 << 28);
const int N = 1024;

int dat[N];
int nsup[N], sup[N];
int dp[N][N];

int main()
{
    freopen("ans.txt", "w", stdout);
    int tcas, cas = 0;
    scanf("%d", &tcas);
    while(tcas --)
    {
        int ans = 0, n, s, p;
        scanf("%d %d %d", &n, &s, &p);
        for(int i = 0; i < n; i++)
            scanf("%d", &dat[i]);
        for(int i = 0; i < n; i++)
        {
            int supval = -1, nsupval = -1;
            for(int j = 0; j <= dat[i]; j++)
            {
                for(int k = 0; k <= dat[i]; k++)
                {
                    for(int l = 0; l <= dat[i]; l++ )
                    {
                        if(j + k + l == dat[i] && abs(j - k) <= 2 && abs(j - l) <= 2 && abs(k - l) <= 2)
                        {
                            int tmp = max(max(j, k), l);
                            bool issup = false;
                            if(abs(j - k) == 2 || abs(j - l) == 2 || abs(k - l) == 2)
                                issup = true;
                            if(issup) supval = max(supval, tmp);
                            else nsupval = max(nsupval, tmp);
                        }
                    }
                }
            }
            nsup[i] = nsupval;
            sup[i] = supval;
        }
        memset(dp, -1, sizeof(dp));
        dp[0][0] = 0;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j <= s && j <= i; j++)
            {
                if(dp[i][j] == -1) continue;
                if(nsup[i] >= p)
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1);
                else
                    dp[i + 1][j] = max(dp[i + 1][j] , dp[i][j]);
                if(sup[i] >= p)
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1);
                else
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j]);
            }
        }
        ans = dp[n][s];
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
