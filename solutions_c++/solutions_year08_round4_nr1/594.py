#include <stdio.h>
#include <iostream>
#define INF 0x3f3f3f3f
#define MAX 10005
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)

int t[MAX], c[MAX], f[MAX], g[MAX];

int main() {
    FILE *fin = fopen("cheat.in", "r"), *fout = fopen("cheat.out", "w");
    int N; fscanf(fin, "%d", &N); REP(n, N) {
        memset(f, INF, sizeof(f)); memset(g, INF, sizeof(g));
        int M, V; fscanf(fin, "%d %d", &M, &V);
        FOR(i, 1, (M-1)/2) fscanf(fin, "%d %d", &t[i], &c[i]);
        FOR(i, (M-1)/2+1, M) {
            int v; fscanf(fin, "%d", &v);
            if (v) f[i] = 0; else g[i] = 0;
        }

        FORD(i, (M-1)/2, 1) {
            if (t[i]) f[i] = min(INF, f[2*i]+f[2*i+1]), g[i] = min(g[2*i], g[2*i+1]);
            else f[i] = min(f[2*i], f[2*i+1]), g[i] = min(INF, g[2*i]+g[2*i+1]);

            if (c[i]) {
                if (t[i]) f[i] <?= min(f[2*i], f[2*i+1])+1;
                else g[i] <?= min(g[2*i], g[2*i+1])+1;
            }
        }

        int res; if (V) res = f[1]; else res = g[1];
        fprintf(fout, "Case #%d: ", n+1);
        if (res >= INF) fprintf(fout, "IMPOSSIBLE\n"); else fprintf(fout, "%d\n", res);
    }
    return 0;
}
