#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

vector< pair<long long int, long long int> > sorted;

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long i, j, k, v, t, test, T, ans, sval[1010], val[1010], N, C, L, times, x, y, left[1010], curans, sdist, leftL, playedwith[1010];

    scanf("%lld", &T);

    for (test=1; test<=T; test++) {
        fprintf(stderr, "%d\n", test);
        scanf("%lld %lld %lld %lld", &L, &t, &N, &C);

        sval[0] = 0;

        for (i=1; i<=C; i++) {
            scanf("%lld", &val[i]);
            sval[i] = sval[i-1] + val[i];
        }

        ans = (sval[C]*(N/C) + sval[N%C])*2;

        sorted.clear();
        for (i=1; i<=C; i++) {
            sorted.push_back( make_pair( val[i], i ) );
            left[i] = (N/C) + (N%C >= i);
            playedwith[i] = 0;
        }

        sort(sorted.begin(), sorted.end());

        /*for (i=0; i<C; i++) {
            //printf("%lld %lld\n", sorted[i].first, sorted[i].second);
        }*/

        x = 0; y = 0; v = 0;
        for (i=1; i<=N; i++) {
            v++;
            if ( v > C ) v = 1;
            //printf("--> %lld: %lld\n", i, val[v]);

            x += val[v]*2;
            //printf("START %lld: x: %lld y: %lld\n", i, x, y);
            left[ v ]--;
            if ( x <= t ) { y = x; continue; }
            if ( t-y == 0 && playedwith[v] == 1 ) { y = x; continue; }

            if ( t-y > 0 ) {
                curans = y + (t-y) + (val[v] - (t-y)/2);
            }
            else {
                curans = y + val[v];
                playedwith[v] = 1;
            }

            //printf("curans: (%lld %lld %lld) %lld left: %lld\n", y, t-y, (val[v] - (t-y)/2), curans, left[v]);

            leftL = L-1;
            for (k=C-1; k>=0; k--) {
                if ( leftL > left[ sorted[k].second ] ) {
                    curans += left[ sorted[k].second ] * sorted[k].first;
                    leftL -= left[ sorted[k].second ];
                }
                else {
                    curans += leftL * sorted[k].first + (left[ sorted[k].second ] - leftL) * sorted[k].first * 2;
                    leftL = 0;
                }
                //printf("... %lld: left[ %lld ] = %lld (%lld) %lld %lld\n", k, sorted[k].second, left[ sorted[k].second ], sorted[k].first, leftL, curans);
            }

            //printf("ANSWERED: %lld\n", curans);
            if ( curans < ans ) ans = curans;
            y = x;
        }

        printf("Case #%lld: %lld\n", test, ans);
    }

    return 0;
}

