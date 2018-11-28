#include<cstdio>
#include<cstring>
#include<vector>

using namespace std;

typedef long long lint;

const int MAXN = 1000 + 50;

vector<lint> make;
int g[MAXN],N;
lint key,round;
bool isCircle[MAXN];

int next(int i) {
    if (i == N - 1) return 0;
    return i + 1;
}

int main() {
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        scanf("%lld%lld%d",&round,&key,&N);
        for(int i = 0 ; i < N ; i++) {
            scanf("%d",g + i);
        }
        int pos = 0,sta = 0;
        lint rou = 0LL,ans = 0LL,val = 0LL;
        while(rou < round) {
            val = 0LL;
            while(val + g[pos] <= key) {
                val += g[pos];
                pos = next(pos);
                if (sta == pos) break;
            }
            sta = pos;
            ans += val;
            rou++;
        }
        printf("Case #%d: %lld\n",t + 1,ans);
    }
    
    return 0;
}
