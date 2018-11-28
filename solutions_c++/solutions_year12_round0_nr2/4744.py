
#include<stdio.h>
#include<string.h>

int t[128];
int dp[128][128];
int possible(int tp, int p, bool sur){
    int a = tp / 3;
    if(p <= a) return 1;
    if(tp % 3 == 0){
        if(sur && p <= a + 1) return 1;
    }
    else if(tp % 3 == 1){
        if(p <= a + 1) return 1;
    }
    else if(tp % 3 == 2){
        if(p <= a + 1) return 1;
        if(sur && p <= a + 2) return 1;
    }
    return 0;
}
int count(int i, int s, int p, int n){
    if(s > n-i) return 0;
    if(i == n) return 0;
    int &res = dp[i][s];
    if(res != -1) return res;
    if(s == 0){
        return res = possible(t[i], p, false) + count(i+1, s, p, n);
    }else{
        if(2 <= t[i] && t[i] <= 28){
            int surp =  possible(t[i], p, true) + count(i+1, s-1, p, n);
            int nsurp = possible(t[i], p, false) + count(i+1, s, p, n);
            if(surp > nsurp) return res = surp;
            else return res = nsurp;
        }else{
            return res = possible(t[i], p, false) + count(i+1, s, p, n);
        }
    }
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc, n, s, p, i, kase = 0;
    scanf("%d", &tc);
    while(tc--){
        memset(dp, -1, sizeof(dp));
        scanf("%d%d%d", &n, &s, &p);
        for(i = 0; i < n; i++)
            scanf("%d", &t[i]);
        printf("Case #%d: %d\n", ++kase, count(0, s, p, n));
    }
    return 0;
}
