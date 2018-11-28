#include <cstdio>
#include <cstring>

using namespace std;

int dp[1024][128];

const char * const g = "welcome to code jam";
char buf[1024];

int main()
{
    int nCase;
    scanf("%d\n", &nCase);
    
    for (int iCase = 1; iCase <= nCase; ++iCase) {

        gets(buf);
        //puts(buf);
        //buf[strlen(buf) - 1] = 0;
        int l = strlen(buf);
        int lg = strlen(g);

        //printf("l = %d, lg = %d\n", l, lg);

        memset(dp, 0, sizeof(dp));
        for (int i = 0; i <= l; ++i) {
            dp[i][0] = 1;            
        }
        
        for (int i = 1; i <= l; ++i) {
            for (int j = 1; j <= lg; ++j) {
                dp[i][j] = dp[i-1][j];
                if (buf[i-1] == g[j-1]) {
                    dp[i][j] += dp[i-1][j-1];
                }
                dp[i][j] %= 1000000;
                //printf("%d %d %d\n", i, j, dp[i][j]);
            }
        }
        
        printf("Case #%d: %04d\n", iCase, dp[l][lg] % 10000);
    }
        
    return 0;
}
