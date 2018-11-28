#include <cstdio>
#include <algorithm>

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define FORE(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FORED(i,c) for(__typeof((c).begin()) i=(c).end();i!=(c).begin();--i)
#define ITER(c) __typeof((c).begin())
#define SZ(a) (int)(a).size()

#define MAXN 1337

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w+", stdout);
    int n;
    scanf("%d", &n);
    REP(i, n) {
        int nb, nums[MAXN], sorted[MAXN], dis = 0;
        scanf("%d", &nb);
        REP(j, nb) scanf("%d", &nums[j]);
        copy(nums, nums + nb, sorted);
        sort(sorted, sorted + nb);
        REP(j, nb)
            if (nums[j] != sorted[j]) dis++;

        printf("Case #%d: %0.6f\n", i + 1, (float) dis);
    }
    fclose(stdin);
    fclose(stdout);
}
