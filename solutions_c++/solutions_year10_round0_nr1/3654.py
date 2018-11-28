#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    FILE* in = fopen("A-large.in", "r");
    FILE* out = fopen("A-large.out", "w");
    //freopen("1snapdeb.txt", "w", stdout);

    int t, n, k, cstate, powers2, nolight;

    fscanf(in, "%d", &t);

    for (int i=0; i<t; ++i) {
        fscanf(in, "%d %d", &n, &k);
        powers2 = 1;
        nolight = 0;
        for (int j=0; j<n; ++j) {
            cstate = (k/powers2)%2;
            if (cstate == 0) {
                nolight = 1;
                break;
            }
            powers2 *= 2;
        }

        if (nolight == 1) {
            fprintf(out, "Case #%d: OFF\n", i+1);
        }
        else {
            fprintf(out, "Case #%d: ON\n", i+1);
        }

        //printf("Case #%d: %d | powers2 = %d, n = %d,  k = %d\n", i+1, cstate, powers2, n, k);
    }

    return 0;
}
