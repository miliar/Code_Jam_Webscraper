#include <cstdio>
#include <string.h>
using namespace std;

int T, R, k, N;
int next [1005];
int groups[1005];
int money[1005];
int already[1005];
int prevsteps[1005];
int main() {
    scanf("%d", &T);
    for (int t=0;t<T;++t) {
        scanf("%d %d %d", &R, &k, &N);
        memset(already,0,sizeof(already)/sizeof(already[0]));
        for (int i=0;i<N;++i) scanf("%d", &groups[i]);

        int j=0; //end
        int s=groups[0]; //sum
        int l=1; //length
        for (int i=0;i<N;++i) { //start
            if (i) {
                --l;
                s-=groups[i-1];
            }
            while (s<=k && l<=N) {
                ++j;
                if (j>=N) j%=N;
                s+=groups[j];
                ++l;
            }
            next[i]=j;
            money[i]=s-groups[j];
            //printf("Next[%d]=%d (%d %d) -> %d\n",i,j,s,l,money[i]);
        }
        int cur=0;
        int total=0;
        int steps=0;
        while (steps<R) {
            already[cur]=total;
            prevsteps[cur]=steps;
            total+=money[cur];
            ++steps;
            cur=next[cur];
            if (already[cur]) {
                int m = int((R-steps)/(steps-prevsteps[cur]));
                total+=(total-already[cur])*m;
                steps+=(steps-prevsteps[cur])*m;
            }
        }
        printf("Case #%d: %d\n", t+1, total);
    }

    return 0;
}
