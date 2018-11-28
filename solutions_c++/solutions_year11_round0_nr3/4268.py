#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

typedef long long ll;

using namespace std;

#define LARGE 1

int main()
{
#if LARGE
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
#endif

    int T, N, candy[1100], xsum, sum;
    scanf("%d", &T);
    FOR(t,1,T+1) {
        scanf("%d", &N);
        xsum = sum = 0;
        REP(i,N) {
            scanf("%d", &candy[i]);
            xsum ^= candy[i];
            sum += candy[i];
        }
        printf("Case #%d: ", t);
        if (xsum || N < 2)
            printf("NO\n");
        else {
            sort(candy,candy+N);
            printf("%d\n", sum-candy[0]);
        }
    }
    return 0;
}
