#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <limits>
#include <map>
using namespace std;

#define MAXC 1000
typedef long long ll;

int a[MAXC]; 
ll  L, t, N, C;
ll  cycleL;

ll solve() {
    ll cycleN = N / C;
    ll cycle_slow = t / cycleL;
    ll result = 0;
    int total = 0;

    if (cycle_slow > cycleN) {
        return cycleL * cycleN + 
            accumulate(a, a + (N % C), 0);
    }

    if (cycle_slow > 0) {
        result += min(cycle_slow, cycleN) * cycleL;
        total += min(cycle_slow, cycleN) * C;
    }

    map<ll, ll> m; bool first = true;
    for (int i = 0; i < C && total < N; ++i, total++)
        if (result + a[i] <= t)
            result += a[i];
        else if (first) {
            m[ a[i] + result - t ]++;
            result = t;
            first = false;
        } else {
            m[ a[i] ]++;
        }

    ll k = cycleN - cycle_slow - 1;
    if (k > 0)
        for (int i = 0; i < C; ++i)
            m[ a[i] ] += k;

    for (int i = 0; i < N % C && total < N; ++i)
        m[ a[i] ]++;

    map<ll, ll>::reverse_iterator it = m.rbegin();
    for (; it != m.rend(); ++it) {
        ll val = (*it).first;
        ll cnt = (*it).second;

        ll take = min(L, cnt); L -= take;
        result += take * (val/2) + (cnt - take) * val;
    }

    return result;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        scanf("%lld%lld%lld%lld", &L, &t, &N, &C);

        cycleL = 0;
        for (int j = 0; j < C; ++j) {
            scanf("%d", &a[j]);
            a[j] <<= 1;
            cycleL += a[j];
        }

        printf("Case #%d: %lld\n", i+1, solve());
    }

    return 0;
}
