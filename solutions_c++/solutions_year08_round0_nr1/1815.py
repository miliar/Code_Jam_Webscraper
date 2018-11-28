#include <stdio.h>
#include <iostream>
#define INF 0x3f3f3f3f
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define CLEAR(t) memset(t, 0, sizeof(t))

int N, S, Q; char engine[105][105], query[105];
int A[1005];
int dp[1005][105];

int main() {
    FILE *fin = fopen("universe.in", "r"), *fout = fopen("universe.out", "w");
    fscanf(fin, "%d\n", &N); REP(n, N) {
        fscanf(fin, "%d\n", &S);
        REP(i, S) fscanf(fin, "%[^\n]\n", engine[i]);
        fscanf(fin, "%d\n", &Q);
        REP(i, Q) {
            fscanf(fin, "%[^\n]\n", &query);
            REP(j, S) if (strcmp(engine[j], query) == 0) A[i] = j;
        }

        CLEAR(dp); FORD(q, Q-1, 0) {
           int mini = INF; REP(s, S) mini <?= dp[q+1][s];
           REP(s, S) 
               if (A[q] == s) dp[q][s] = INF;
               else if (dp[q+1][s] == mini) dp[q][s] = mini;
               else dp[q][s] = mini+1;
        }

        int res = INF; REP(s, S) res <?= dp[0][s];
        fprintf(fout, "Case #%d: %d\n", n+1, res);
    }
    return 0;
}
