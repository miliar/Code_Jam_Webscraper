#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

#include <string>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>

#define INFINITO 0x3f3f3f3f

using namespace std;

unsigned q[1024];
int foi[1024];
unsigned pessoas[1024];

int main (void) {    

    unsigned t, tt;
    unsigned r, k, n;
    unsigned i, j;
    unsigned casos=1;

    scanf("%d", &t);

    for (tt=0; tt<t; ++tt) {
        scanf("%d %d %d", &r, &k, &n);

        for (i=0; i<n; ++i) {
            scanf("%d", &q[i]);
        }

        unsigned inicio=0;
        memset(foi, -1, sizeof foi);
        long long unsigned sum=0;

        bool cabe_todo_mundo_junto=1;
        for (i=0; i<n; ++i) {
            sum += q[i];
            if (sum > k) {
                cabe_todo_mundo_junto=0;
                break;
            }
        }

        if (cabe_todo_mundo_junto) {
            printf("Case #%u: %llu\n", casos++, r*sum);
            continue;
        }

        sum=0;

        for (j=0; j<r; ++j) {
            i = inicio;
            if (foi[i] > -1) {
                sum += pessoas[i];
                inicio = foi[i];
            }
            else {
                unsigned g=0;
                for (; g<=k; i = (i+1)%n) {
                    g += q[i];
                }
                i = (i+n-1)%n;
                g -= q[i];
                sum += g;

                pessoas[inicio] = g;
                foi[inicio]=i;
                inicio = i;
            }
        }

        printf("Case #%u: %llu\n", casos++, sum);
    }

    return 0;
}
