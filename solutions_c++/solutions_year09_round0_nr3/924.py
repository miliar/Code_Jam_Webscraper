#include <cstdio>
using namespace std;

const int L = 19;
const int N = 512;
const int M = 10000;
char w[]="welcome to code jam";
char s[N];
int dp[2][L];

int main() {
    int j; scanf("%d\n",&j);
    for(int cn=1;cn<=j;cn++) {
        int n=0;
        for(;;) {
            char tmp; scanf("%c",&tmp);
            if (tmp!='\n') s[n++]=tmp; else break;
        }
        for(int i=0;i<L;i++) dp[1][i]=0;
        for(int i=0;i<n;i++) {
            dp[i&1][0] = (dp[!(i&1)][0] + (s[i]==w[0]))%M;
            for(int j=1;j<L;j++) 
                dp[i&1][j] = (dp[!(i&1)][j] + (s[i]==w[j])*dp[!(i&1)][j-1])%M;
        }
        printf("Case #%d: %04d\n",cn,dp[(n-1)&1][L-1]);
    }
    return 0;
}

