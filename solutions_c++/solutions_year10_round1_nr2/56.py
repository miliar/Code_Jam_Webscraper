#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdio>
#define pb push_back
#define sz size()
#define all(v) v.begin(), v.end()
#define VI vector<int>
#define U unsigned int
#define LL long long
#define cont(l, x) ((l).find(x) != (l).end())
#define memclr(x) memset((x), 0, sizeof(x))
#define vcont(v, x) (find((v).begin(), (v).end(), x) != (v).end())
#define REP(i, N) for(unsigned int i=0;i<(N);i++)
#define REPV(i, v) for(unsigned int i=0;i<(v).size();i++)
#define FOR(i, S, E) for(int i=(S);i<(E);i++)
#define FORR(i, S, E) for(int i=(S);i>(E);i--)
#define REPI(i, N) for(int i=0;i<=(N);i++)
using namespace std;


#define INF 1000000

int ninsert[256];
int nums[100];
int cheapest[101][256];
int main() {
    int T;
    scanf("%d", &T);
    REP(_t, T) {
        int D, I, M, N;
        scanf("%d %d %d %d", &D, &I, &M, &N);
        REP (i, N) {
            scanf("%d", nums+i);
        }
        ninsert[0] = 0;
        if (M == 0) {
            FOR(i, 1, 256)
                ninsert[i] = INF;
        } else {
            FOR(i, 1, 256)
                ninsert[i] = (i-1) / M;
        }

        REP(i, 101) REP(j, 256) {
            cheapest[i][j] = INF;
        }
        REP(j, 256) cheapest[0][j] = 0;

        int themin = 255;
        int themax = 0;
        REP(i, N) {
            themin = min(themin, nums[i]);
            themax = max(themax, nums[i]);
        }

        REP(i, N) {
            int n = nums[i];
            FOR(x, themin, themax+1) {
                int v = abs(x - n);
                FOR(j, themin, themax+1) {
                    int ins = ninsert[abs(x - j)];
                    if (ins && M == 0)
                        continue;
                    cheapest[i+1][x] = min(cheapest[i+1][x], cheapest[i][j] + v + I * ins);
                }
            }
            REP(j, 256) cheapest[i+1][j] = min(cheapest[i+1][j], cheapest[i][j] + D);
        }

        int best = INF;
        REP(i, 256)
            best = min(best, cheapest[N][i]);
        printf("Case #%d: %d\n", _t+1, best);
        fflush(stdout);
    }
    return 0;
}
