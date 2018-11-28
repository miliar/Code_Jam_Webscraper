#include <stdio.h>
#include <string.h>

void input();
void solve();

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    
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

const int Max = 16;
char map[Max][Max];
int dp[Max][1<<11], n, m;

void input() {
    scanf("%d%d%d", &n, &m);
    for(int i = 0;i < n;i ++) scanf("%s", map[i]);
}

int cnt(int stat) {
    int res = 0;
    while(stat) {
        if(stat&1) ++ res;
        stat >>= 1;
    }
    return res;
}

int ok(int stat) {
    for(int j = 1;j < m;j ++) if((stat&(1<<j))&&(stat&(1<<(j-1)))) return 0;
    return 1;
}

int search(int r,int stat) {
    if(dp[r][stat] != -1) return dp[r][stat];
    int &res = dp[r][stat];
    
    res = 0;
    if(r == 0) {
        int use = 0;
        for(int j = 0;j < m;j ++) {
            if(!use&&(stat&(1<<j)) == 0) {
                ++ res;
                use = 1;
            }
            else use = 0;
        }
    }
    else {
        int newstat = 0;
        for(int j = 0;j < m;j ++) if(map[r-1][j] == 'x') newstat |= (1<<j);
        res = search(r-1, newstat);
        
        stat = stat^((1<<m)-1);
        for(int s = stat;s != 0;s = stat&(s-1)) if(ok(s)) {
            int newstat = 0;
            for(int j = 0;j < m;j ++) if(map[r-1][j] == 'x') newstat |= (1<<j);
            for(int j = 0;j < m;j ++) if(s&(1<<j)) {
                if(j > 0) newstat |= (1<<(j-1));
                if(j < m-1) newstat |= (1<<(j+1));
            }
            int tmp = cnt(s) + search(r-1, newstat);
            if(tmp > res) res = tmp;
        }
    }
    return res;
}

void solve() {
    memset(dp, -1, sizeof(dp));
    int stat = 0;
    for(int j = 0;j < m;j ++) if(map[n-1][j] == 'x') stat |= (1<<j);
    printf("%d\n", search(n-1, stat));
}
