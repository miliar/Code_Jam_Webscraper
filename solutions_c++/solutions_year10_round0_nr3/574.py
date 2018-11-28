#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

#define REP(i,n) for (int i = 0; i < (int)n; ++i)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

const long long MAXN = 1005;

long long a[MAXN];
long long g_in_coaster[MAXN];
long long next[MAXN];

int main(void)
{
    int nCase;
    long long R, K, N;

    scanf("%d", &nCase);

    REP(c, nCase) {
        scanf("%lld %lld %lld", &R, &K, &N);
        REP(i, N) {
            scanf("%lld", &a[i]);
        }

        //precompute
        REP(i, N) {
            long long sum = 0;
            long long cnt = 0;
            int j;
            for (j = i; cnt < N; j = (j+1) % N) {
                cnt += 1;
                if (sum + a[j] <= K) {
                    sum += a[j]; 
                } else {
                    break;
                }
            }

            g_in_coaster[i] = sum;
            next[i] = j;
        }

        long long ans = 0;
        int curr = 0;
        REP(i, R) {
            ans += g_in_coaster[curr];
            curr = next[curr];
        }

        printf("Case #%d: %lld\n", c+1, ans);
    }

    return 0;
}
