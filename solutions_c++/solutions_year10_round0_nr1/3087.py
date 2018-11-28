#include <cstdio>
#include <cstring>

using namespace std;

struct snap {
    bool power;
    bool on;
} snapper [32];

int main (void) {

    int t, tt;
    int n, k;
    int i, j;
    int caso=1;

    scanf("%d", &t);

    for (tt=0; tt<t; ++tt) {

        scanf("%d %d", &n, &k);

        memset(snapper, 0, sizeof snapper);
        snapper[0].power=1;

        for (j=0; j<k; ++j) {
            for (i=0; i<n; ++i) {
                if (snapper[i].power)
                    snapper[i].on = 1 - snapper[i].on;

                if (i) {
                    if (snapper[i-1].power and snapper[i-1].on)
                        snapper[i].power = 1;
                    else
                        snapper[i].power = 0;
                }
            }
        }

        if (snapper[n-1].on and snapper[n-1].power)
            printf("Case #%d: ON\n", caso++);
        else
            printf("Case #%d: OFF\n", caso++);
    }

    return 0;
}
