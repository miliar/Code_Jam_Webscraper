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
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 1

int digits(int n)
{
    int ret = 0;
    while (n > 0) {
        n /= 10;
        ++ret;
    }
    return ret;
}

int main()
{
#if SMALL
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
#else
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
#endif

    int T, A, B, ans, N;
    scanf("%d", &T);
    set<pair<int, int> > S;

    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d", &A, &B);
        S.clear();
        for (int x = A; x <= B; ++x) {
            N = digits(A);

            for (int n = 1; n < N; ++n) {
                int nx, p1 = pow(10,n), p2 = pow(10,N-n);
                nx = x%p1*p2+x/p1;

                if (digits(x) == digits(nx) && nx >= A && nx <= B && nx > x) {
                    if (S.find(make_pair(x,nx)) == S.end()) {
                        S.insert(make_pair(x,nx));
                    }

                    //cout << n << " " << x << " " << nx << endl;
                }
            }
        }
        printf("Case #%d: %d\n", tc, SZ(S));
    }
    return 0;
}
