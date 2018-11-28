#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

typedef long long ll;

ll L, n, C, t;
ll c[1000005];
ll y[1000005];

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        cin >> L >> t >> n >> C;
        rep(i, C) cin >> c[i];

        long double res = -1;
        long double time = 0;

        rep(i, n) {
            
            ll d = c[i % C];
            long double ntime = time + 2 * d;

            if(ntime > t) {

                // either take current one and then greedy
                // or don't and then greedy

                long double time1 = time + d + (t - time) / 2.0;
                long double time2 = time + 2.0 * d;

                ll m = 0;
                for(int j = i + 1; j < n; j++)
                    y[m++] = c[j % C];

                sort(y, y + m);
                reverse(y, y + m);

                long double best = 0;
                long double extra = 0;

                rep(j, min(L, m)) {
                    best += y[j];
                    if(j == L - 1) extra = y[j];
                }

                long double left = 0;
                for(int j = min(L, m); j < m; j++)
                    left += y[j];

                time2 += best + left * 2.0;
                time1 += best - extra + (left + extra) * 2.0;

                if(L == 0) res = time2;
                else res = min(time1, time2);
                break;

            }
            else time = ntime;
        }
        if(res < 0) res = time;

        cout << ll(res + .55) << endl;

    }
}
