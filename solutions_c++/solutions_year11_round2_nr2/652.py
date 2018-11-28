/*
    2011 Round 1B -
    Revenge of the Hot Dogs
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std ;

    int T, C, D;
    int P[200], V[200];

bool canbeans(double t) {
    //printf("\nt %lf\n", t);
    int tP[200], tV[200], tC = C;
    memcpy(tP, P, sizeof(tP));
    memcpy(tV, V, sizeof(tV));
    double left_point = tP[0] - t;
    for(int i=0; i<tC; ++i) {
        while(tV[i]>0) {
            if(fabs(tP[i]-left_point)<=t) {
                left_point += D;
            }
            else {
                if(tP[i]>left_point) {
                    left_point = tP[i] - t + D;
                }
                else {
                    return false;
                }
            }
            //printf("lp %lf  tP[i] %lf\n", left_point, (double)tP[i]);
            --tV[i];
        }
    }
    return true;
}

int main() {
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        scanf("%d %d", &C, &D);
        for(int i=0; i<C; ++i) {
            scanf("%d %d", &P[i], &V[i]);
        }
        double L = 0.0, R = 1.0E13;
        while(R-L>1E-12) {
            double mid = (R+L) / 2.0;
            //printf("---");
            if(canbeans(mid)) {
                //printf("T");
                R = mid;
            }
            else {
                //printf("F");
                L = mid;
            }
            //system("pause");
        }
        printf("Case #%d: %.10lf\n", z, R);
    }
    return 0;
}
