#include <cstdio>
#include <algorithm>
using namespace std;

int T, N, E, d[10000], l[10000];
int reach_len[10000];

int main()
{
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        bool ans = false;
        scanf("%d", &N);
        for(int i=0; i<N; ++i) {
            reach_len[i] = -1;
        }
        for(int i=0; i<N; ++i) {
            scanf("%d %d", &d[i], &l[i]);
        }
        scanf("%d", &E);
        reach_len[0] = d[0];
        for(int i=0; i<N; ++i) {
            //printf("rl %d\n", reach_len[i]);
            if(reach_len[i]!=-1) {
                int r = d[i] + reach_len[i];
                for(int j=i+1; j<N && d[j]<=r; ++j) {
                    int t = min(d[j]-d[i], l[j]);
                    if(reach_len[j]==-1 || t>reach_len[j]) {
                        reach_len[j] = t;
                    }
                }
                //printf("IER   %d   %d %d\n", i, E, r);
                if(E<=r) {
                    ans = true;
                    break;
                }
            }
        }
        if(ans) {
            printf("Case #%d: YES\n", z);
        }
        else {
            printf("Case #%d: NO\n", z);
        }
    }
    return 0;
}
