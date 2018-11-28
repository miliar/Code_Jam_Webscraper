#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int INF = 1000000000;

int n, num[1000];
int dp[2][1<<20];
int SVIXOR;
int SUMSVI;

int main(void) {
 int test; scanf("%d", &test);

 for (int cs = 0; cs < test; ++cs) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d", num+i);

    SVIXOR = 0;
    SUMSVI = 0;
    int UPPER = 0;
    for (int i = 0; i < n; ++i) {
        SUMSVI += num[i];
        SVIXOR ^= num[i];
        UPPER |= num[i];
    }
    ++UPPER;

    int sol = 0;

    int curr = 0, next = 1;

    for (int i = 1; i < UPPER; ++i) {
        dp[curr][i] = -INF;
    }
    dp[curr][0] = 0;

    // printf("%d %d\n", SVIXOR, SUMSVI);

    for (int i = 0; i < n; ++i) {
        // memset(dp[next], 0, sizeof dp[next]);
        for (int maska = 0; maska < UPPER; ++maska) {
                dp[next][maska] = -INF;
        }

        for (int maska = 0; maska < UPPER; ++maska) {
            dp[next][maska] = max(dp[next][maska], dp[curr][maska]);
            if (dp[curr][maska] + num[i] < SUMSVI) {
                dp[next][maska^num[i]] = max(dp[next][maska^num[i]], dp[curr][maska]+num[i]);
            }
        }
        for (int maska = 0; maska < UPPER; ++maska) {
            //if (dp[next][maska]>0) {
            //    printf("-- i %d -- maska %d\n", i, maska);
            //}
            if ((maska ^ maska) == SVIXOR) {
                sol = max(sol, dp[next][maska]);
            }
        }

        swap(curr, next);
    }

    printf("Case #%d: ", cs+1);
    if (sol > 0) {
        printf("%d\n", sol);
    } else {
        puts("NO");
    }
 }
 return 0;
}
