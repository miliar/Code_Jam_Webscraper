#include <iostream>
using namespace std;
const int MaxN = 110;
int dp[MaxN][256];
int a[MaxN];
int costd, costi, maxc, n, quesnum;
void inputint()
{
    scanf ( "%d%d%d%d", &costd, &costi, &maxc, &n );
    for (int i=0;i<n;i++) 
        scanf ( "%d", &a[i] );
}
void work()
{
    int i,j,t,ans,tmp;
    memset (dp, 0, sizeof(dp));
    for (j=0;j<256;j++) {
        dp[0][j] = abs(j-a[0]);
    }
    for (i=1;i<n;i++) {
        for (j=0;j<256;j++) {
            dp[i][j] = dp[i-1][j]+costd;
            for (t=0;t<256;t++) {
                tmp = abs(a[i]-j)+dp[i-1][t];
                if (abs(j-t)>0) 
                    if (maxc>0)
                        tmp += (abs(j-t)-1)/maxc*costi;
                    else
                        continue;
                if (tmp<dp[i][j]) {
                    dp[i][j] = tmp;
                }
            }
        }
    }
    ans = dp[n-1][0];
    for (j=1;j<256;j++) {
        if (dp[n-1][j]<ans)
            ans = dp[n-1][j];
    }
    printf ( "%d\n", ans );
}
int main()
{
    freopen ( "smooth.in", "r", stdin );
    freopen ( "smooth.out", "w", stdout );
    scanf ( "%d", &quesnum );
    for (int i=1;i<=quesnum;i++) {    
        printf ( "Case #%d: ", i );
        inputint();
        work();
    }
//    system ( "pause" );
    return 0;
}
