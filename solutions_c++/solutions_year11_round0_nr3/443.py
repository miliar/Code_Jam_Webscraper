/*
    Qualification Round 2011 -
    Candy Splitting
    by Dave Chang
*/
#include <cstdio>

using namespace std ;

    int T, N, C, minC, allsum, allxor;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        allsum = allxor = 0;
        minC = 10000000;
        scanf("%d", &N);
        for(int i=0; i<N; ++i) {
            scanf("%d", &C);
            if(C<minC) minC = C;
            allsum += C;
            allxor ^= C;
        }
        if(allxor!=0) {
            printf("Case #%d: NO\n", z);
        }
        else {
            printf("Case #%d: %d\n", z, allsum - minC);
        }
    }
    return 0;
}
