#include<cstdio>

using namespace std;

const int MAXN = 100 + 10;

int V[MAXN],X[MAXN];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        int N,K,B,Time;
        scanf("%d%d%d%d",&N,&K,&B,&Time);
        for(int i = 0 ; i < N ; i++) {
            scanf("%d",X + i);
        }
        for(int i = 0 ; i < N ; i++) {
            scanf("%d",V + i);
        }
        int ans = 0,PassThro = 0;
        for(int i = N - 1 ; i >= 0 ; i--) {
            if (X[i] + V[i] * Time >= B) {
                K--;
                ans += PassThro;
            }
            else {
                PassThro++;
            }
            if (K == 0) break;
        }
        if (K == 0) {
            printf("Case #%d: %d\n",t + 1,ans);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n",t + 1);
        }
    }
    
    return 0;
}
