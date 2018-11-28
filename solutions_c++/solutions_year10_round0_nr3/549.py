#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_N = 1010;

long long R, k, N;
long long g[MAX_N];
pair<long long, int> used[MAX_N];

void fun(int cs) {
    scanf("%lld %lld %lld", &R, &k, &N);

    REP(i, N) {
        scanf("%lld", &g[i]);
        used[i] = make_pair(-1, -1);
    }

    long long res = 0;

    long long on = 0;
    int cur = 0;
    int s = 1;
    REP(i, R) {
        if ( used[cur].first != -1 and s ) {
//            printf("cur = %d, res = %lld, R = %lld, i = %d, s = %d %lld %d\n", cur, res, R, i, s, used[cur].first, used[cur].second);
            int len = i - used[cur].second;
    
            R -= i;

            res += (R / len) * (res - used[cur].first);
            R %= len;
            i = -1;
            s = 0;
            continue;
        }

        used[cur] = make_pair(res, i);

        int stop = cur;
        while ( on + g[cur] <= k ) {
            on += g[cur];
            cur = (cur + 1) % N;
            if ( cur == stop ) break;
        }

        res += on;
        on = 0;

    }

    printf("Case #%d: %lld\n", cs, res);
}

int main() {
    int T;
    scanf("%d", &T);
    REP(i, T) fun(i+1);

    return 0;
}
