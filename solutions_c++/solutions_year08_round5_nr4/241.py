#include <stdio.h>
#include <iostream>
#define MOD 10007
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)

bool bad[105][105];
int ways[105][105];

int main() {
    FILE *fin = fopen("knight.in", "r"), *fout = fopen("knight.out", "w");
    int N; fscanf(fin, "%d", &N); REP(n, N) {
        int H, W, R; fscanf(fin, "%d %d %d", &H, &W, &R);
        memset(bad, false, sizeof(bad)); REP(i, R) {
            int r, c; fscanf(fin, "%d %d", &r, &c); 
            bad[r][c] = true;
        }

        memset(ways, 0, sizeof(ways)); ways[1][1] = 1; FOR(r, 1, H) FOR(c, 1, W) {
            int r2 = r+1, c2 = c+2;
            if (r2 <= H && c2 <= W && !bad[r2][c2]) ways[r2][c2] = (ways[r2][c2]+ways[r][c])%MOD;
            r2 = r+2, c2 =c+1;
            if (r2 <= H && c2 <= W && !bad[r2][c2]) ways[r2][c2] = (ways[r2][c2]+ways[r][c])%MOD;
        }

        fprintf(fout, "Case #%d: %d\n", n+1, ways[H][W]);
    }
}
