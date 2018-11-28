#include <stdio.h>
#include <string.h>

char buf[50000+10];
int n, m, len, num[16][16], be[16][16];
int dp[1<<15][15];

void input() {
    scanf("%d %s", &len, buf);
    n = strlen(buf);
    m = n/len;
}

void init() {
    for(int i = 0;i < len;i ++) for(int j = 0;j < len;j ++) if(i != j) {
        num[i][j] = 0;
        for(int k = 0;k < m;k ++) if(buf[k*len+i] == buf[k*len+j]) ++ num[i][j];
        be[i][j] = 0;
        for(int k = 1;k < m;k ++) if(buf[k*len+i] == buf[(k-1)*len+j]) ++ be[i][j];
    }
}

int search(int v) {
    memset(dp, 0, sizeof(dp));
    int res = 0;
    for(int state = 1;state < (1<<(len-1));state ++) for(int i = 0;i < len-1;i ++) if((1<<i)&state) {
        if((state&(state-1)) == 0) {
            int j = i;
            if(j >= v) ++ j;
            dp[state][i] = num[v][j];
            if(state == (1<<(len-1))-1) dp[state][i] += be[v][j];
        }
        else {
            for(int j = 0;j < len-1;j ++) if(j != i&&((1<<j)&state)) {
                int tmp = dp[state^(1<<i)][j];
                int tb = j, te = i;
                if(tb >= v) tb ++;
                if(te >= v) te ++;
                tmp += num[tb][te];
                if(state == (1<<(len-1))-1) tmp += be[v][te];
                if(tmp > dp[state][i]) dp[state][i] = tmp;
            }
        }
        if(dp[state][i] > res) res = dp[state][i];
    }
    return res;
}

void solve() {
    init();
    int res = 0;
    for(int i = 0;i < len;i ++) {
        int tmp = search(i);
        if(tmp > res) res = tmp;
    }
    printf("%d\n", n - res);
}

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d: ", cas);
        solve();
    }
    getchar(); getchar();
    return 0;
}
