#include <stdio.h>
#include <string.h>

#define FOR(i,n) for((i)=0;(i)<(n);(i)++)
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define _FORIT(it, b, e) for (__typeof(b) it = (b); it != (e); it++)
#define FORIT(x...) _FORIT(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define CLR(a,v) memset((a),(v),sizeof(a)) 
#define TLE while(1);
#define RTE printf("%d", 1/0);


int n;
char A[1000], B[50];
int dp[1000][50];
int na, nb;



int main() {
    
    int c, i, j, k;
    strcpy(&B[1], "welcome to code jam"); nb = 19;
    scanf("%d ", &n);
    for (c = 1; c <= n; c++) {
        printf("Case #%d: ", c);
        gets(&A[1]); na = strlen(&A[1]);
        for (j = 1; j <= na; j++) dp[1][j]=dp[1][j-1]+((A[j]=='w')?1:0);
        for (i = 2; i <= nb; i++) for(j = 1; j <= na; j++) {
            dp[i][j] = dp[i][j-1];
            if (B[i]==A[j]) dp[i][j] = (dp[i][j]+dp[i-1][j])%10000;
        }
        printf("%04d\n", dp[nb][na]);
    }
    
    return 0;
}
