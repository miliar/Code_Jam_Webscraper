#include <iostream>
#include <cmath>
using namespace std;

int T,P,N,tmp;
long long int dp[5000][20];
long long int match[2000];
long long int price[4000];

long long int best(int a, int b, int x, int d){
    if(dp[x][d] != -1) return dp[x][d];
    if(a == b){
        if(P-d<=match[a]) dp[x][d] = 0;
        else dp[x][d] = -1;
    }
    else{ 
        if(best(a,(a+b)/2,2*x,d)!= -1 && best((a+b)/2+1,b,2*x+1,d)!=-1)
            dp[x][d] = best(a,(a+b)/2,2*x,d) + best((a+b)/2+1,b,2*x+1,d);
        if(best(a,(a+b)/2,2*x,d+1)!=-1 && best((a+b)/2+1,b,2*x+1,d+1)!=-1){
            if(dp[x][d] == -1) dp[x][d] = best(a,(a+b)/2,2*x,d+1) + best((a+b)/2+1,b,2*x+1,d+1) + price[x];
            else dp[x][d] <?= best(a,(a+b)/2,2*x,d+1) + best((a+b)/2+1,b,2*x+1,d+1) + price[x];
        }
    }
  //  printf("dp[%d][%d] from %d to %d = %d\n", x, d, a,b,dp[x][d]);
    return dp[x][d];
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    scanf("%d", &T);
    for(int cn = 1;cn<=T;++cn){
        memset(dp,-1,sizeof(dp));
        memset(price,-1,sizeof(price));
        scanf("%d", &P);
        N = 1;
        for(int i=0;i<P;++i) N*=2;
        for(int i=1;i<=N;++i) scanf("%lld", &match[i]);
        for(int i=P-1;i>=0;--i){
            tmp = 1;
            for(int j=1;j<=i;++j) tmp*=2;
            for(int j=tmp;j<tmp*2;++j) scanf("%lld", &price[j]);
        }
        printf("Case #%d: %lld\n", cn, best(1,N,1,0));
    }
 //   system("pause");
}
