/*
    2011 Round 1A -
    FreeCell Statistics
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

    int T;
    long long N;
    int PD, PG;

int main() {
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        scanf("%I64d %d %d", &N, &PD, &PG);
        bool be = false;
        if(PG==100) {
            if(PD==100) {
                be = true;
            }
            else {
                be = false;
            }
        }
        else if(PG==0) {
            if(PD==0) {
                be = true;
            }
            else {
                be = false;
            }
        }
        else {
            for(int D=1; D<=(int)min(100LL, N); ++D) {
                int winD = D*PD;
                if(winD%100==0) {
                    be = true;
                    break;
                }
            }
        }
        if(be) {
            printf("Case #%d: Possible\n", z);
        }
        else {
            printf("Case #%d: Broken\n", z);
        }
    }
    return 0;
}
