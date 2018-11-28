#include <stdio.h>
#include <iostream>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define CLEAR(t) memset(t, 0, sizeof(t))

int M, N;
bool ok[15][15];
int dp[15][1<<15];

int pop(int n) {
    int res = 0; while(n) res += n%2, n /= 2;
    return res;
}

bool works(int r, int mask) {
    int prev = 0;
    FORD(loc, N-1, 0) {
        int b = mask%2; mask /= 2;
        if (b && (prev || !ok[r][loc])) return false;
        prev = b;
    }
    return true;
}

bool valid(int p, int c) {
    if ((p & (c >> 1)) || ((p >> 1) & c)) return false;
    return true;
}

int main() {
    FILE *fin = fopen("cheating.in", "r"), *fout = fopen("cheating.out", "w");
    int C; fscanf(fin, "%d", &C); REP(t, C) {
        fscanf(fin, "%d %d\n", &M, &N);
        REP(r, M) {
            REP(c, N) {
                char ch; fscanf(fin, "%c", &ch);
                ok[r][c] = (ch == '.');
            }
            fscanf(fin, "\n");
        }

        CLEAR(dp);
        REP(r, M) REP(mask, 1<<N) if (works(r, mask)) {
            if (!r) {
                dp[r][mask] = pop(mask);
                continue;
            }
            REP(prev, 1<<N) if (valid(prev, mask)) 
                dp[r][mask] >?= dp[r-1][prev]+pop(mask);
        }

        int res = 0; REP(mask, 1<<N) res >?= dp[M-1][mask];
        fprintf(fout, "Case #%d: %d\n", t+1, res);
    }
}
