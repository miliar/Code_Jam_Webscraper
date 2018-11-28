#include<cstdio>
#include<cstring>

using namespace std;

typedef long long lint;

const int MAXN = 510;
const lint MOD = 100003;

lint F[MAXN][MAXN],c[MAXN][MAXN],ans[MAXN];

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    memset(c, 0, sizeof(c));
    memset(F, 0, sizeof(F));
    memset(ans, 0, sizeof(ans));
    
   c[0][0] = 1; 
    for (int i = 1; i < MAXN; ++i){
        c[i][0] = c[i][i] = 1; 
        for (int j = 1; j < i; ++j){
            c[i][j] = c[i-1][j-1] + c[i-1][j];
            c[i][j] %= MOD;
        }
    }
    
    F[1][0] =  F[2][1] = 1;
    ans[1] = ans[2] = 1;
    for (int i = 3; i < MAXN; ++i){
        F[i][1] = 1;
        for (int j = 1; j < i; ++j)  {
            
            for (int k = 1; k < j; ++k){
                F[i][j] += F[j][k] * c[i - j - 1][j - k - 1];
                F[i][j] %= MOD;
            }
            
            ans[i] += F[i][j];
            ans[i] %= MOD;
        }
    }
    
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        int N;
        scanf("%d",&N);
        printf("Case #%d: %lld\n",t + 1,ans[N]);
    }
}

