#include <cstdio>
#include <cstring>

char *S="welcome to code jam";

void go(char *s) {
    int dp[100];
    int i;
    int n=strlen(S);
    for(i = 0; i<=n; i++) dp[i] = 0;
    dp[0]=1;
    while(*s) {
        for(i = n; i; i--) {
            if(*s == S[i-1]) {
                dp[i] += dp[i-1];
                dp[i] %= 10000;
            }
        }
        s++;
    }
    printf("%04d\n", dp[n]);
}

int main() {
    int n,i;
    scanf("%d\n",&n);
    char buf[1000];
    for(i =1;i<=n;i++) {
        scanf("%[^\n]\n",buf);
        printf("Case #%d: ", i);
        go(buf);
    }
    return 0;
}
