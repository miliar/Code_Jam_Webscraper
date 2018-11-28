#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef long long LL;
#define SZ(c) int((c).size())
const LL INF = 1LL << 60;

LL calc(const VI &x, const VI &y){
    int n = SZ(x);
    LL ans = 0;
    for(int i = 0; i < n; ++i) ans += x[i] * y[i];
    return ans;
}


int main(){
    int nCase;
    scanf("%d", &nCase);
    for(int ca = 1; ca <= nCase; ++ca){
        int n;
        scanf("%d", &n);
        VI x, y;
        for(int i = 0, val; i < n; ++i){
            scanf("%d", &val);
            x.push_back(val);
        }
        for(int i = 0, val; i < n; ++i){
            scanf("%d", &val);
            y.push_back(val);
        }
        sort(x.begin(), x.end());
        LL best = INF;
        do{
            best <?= calc(x, y);
        }while(next_permutation(x.begin(), x.end()));
        printf("Case #%d: %I64d\n", ca, best);
    }
    return 0;
}
