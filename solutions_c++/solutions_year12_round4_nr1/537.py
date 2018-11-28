#include <cstdio>
#include <cstring>
#include <cstdlib>

const int Max = 10000;

int d[Max], l[Max], dp[Max], D, n;

void input() {
    scanf("%d", &n);
    for(int i = 0;i < n;i ++) scanf("%d%d", &d[i], &l[i]);
    scanf("%d", &D);
}

int solve() {
    for(int i = 0;i < n;i ++) dp[i] = 0;
    
    dp[0] = d[0];
    
    for(int i = 0;i < n;i ++) {
        if(d[i] + dp[i] >= D) return 1;
        
        for(int j = i+1;j < n&&d[i] + dp[i] >= d[j];j ++) {
            int tmp = l[j];
            if(d[j] - d[i] < tmp) tmp = d[j] - d[i];
            if(tmp > dp[j]) dp[j] = tmp;
        }
    }
    
    return 0;
}

int main() {
    freopen("A-large.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d: ", cas);
        if(solve()) printf("YES\n");
        else printf("NO\n");
    }
    
    return 0;
}
