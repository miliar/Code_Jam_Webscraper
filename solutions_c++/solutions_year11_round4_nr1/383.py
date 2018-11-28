/*
    2011 Round 2 -
    Airport Walkways
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

    int T;
    int X, S, R, t, N;
    int B[1000], E[1000], W[1000];
    int spd[1000000];
    double ans;

int main() {
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
        for(int i=0; i<1000000; ++i)
            spd[i] = S;
        for(int i=0; i<N; ++i)
        {
            scanf("%d %d %d", &B[i], &E[i], &W[i]);
            for(int j=B[i]; j<E[i]; ++j)
            {
                spd[j] += W[i];
            }
        }
        sort(spd, spd+X);
        /*for(int i=0;i<X;++i)
            printf("S: %d\n", spd[i]);*/
        ans = 0.0;
        double dt = t;
        for(int i=0; i<X; ++i)
        {
            int ns = spd[i]+R-S;
            double nt = 1.0/ns;
            if(dt>0.0)
            {
                if(dt>=nt)
                {
                    spd[i] = ns;
                    dt -= nt;
                    ans += 1.0/spd[i];
                }
                else{
                    ans += dt + (1.0-dt*ns)/spd[i];
                    dt = 0.0;
                }
            }
            else
            {
                ans += 1.0/spd[i];
            }
        }
        //printf("T: %lf\n", t);
        printf("Case #%d: %.10lf\n", z, ans);
    }
    return 0;
}
