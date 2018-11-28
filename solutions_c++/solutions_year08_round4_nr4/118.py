#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

char buf[64000];
int K;
int C[64000];

void read_one()
{
    cin >> K >> buf;
}

char seen[255];
int N;
int dif[32][32];
int difleg[32][32];
int memo[16][16][1 << 16];

int dp(int start, int stop, int bitmask)
{
    int i;

    if (memo[start][stop][bitmask] > 0) {
        return memo[start][stop][bitmask] - 1;
    }

    if (start == stop && bitmask == 0) {
        memo[start][stop][bitmask] = N / K + 1;
        return N / K;
    }

    int cur = N + 1;
    
    for (i = 0; i < K; i++)
        if ((bitmask & (1 << i))) {
            int prev = dp(start, i, bitmask ^ (1 << i));

            if (prev + dif[i][stop] < cur) {
                cur = prev + dif[i][stop];
            }
        }

    memo[start][stop][bitmask] = cur + 1;

    return cur;
}

void solve_one()
{
    int i, j, k;

    memset(C, 0, sizeof(C));
    for (i = 0; buf[i]; i++);
    int best = 9999999;
    N = i;

    memset(memo, 0, sizeof(memo));
    memset(dif, 0, sizeof(dif));
    memset(difleg, 0, sizeof(dif));
    for (i = 0; i < K; i++)
    for (j = 0; j < K; j++)
        if (i != j) {
            for (k = 0; k < N / K; k++) {
                if (buf[k*K + i] != buf[k*K + j]) {
                    dif[i][j] ++;
                }
                if (k >= 1 && buf[(k-1)*K + j] == buf[k*K + i]) {
                    difleg[i][j] ++;
                }
            }
        }
    
    for (i = 0; i < K; i++)
    for (j = 0; j < K; j++)
        if (i != j) {
            int bitmask = ((1 << K) - 1) ^ (1 << j);
            best = min(best, -difleg[i][j] + dp(i, j, bitmask));
        }

    cout << best;
}

int main(void)
{
    int T, i;

    for(scanf("%d\n", &T), i = 1; i <= T; i++) {
        read_one();
        printf ("Case #%d: ", i);
        solve_one();
        printf ("\n");
    }
}

