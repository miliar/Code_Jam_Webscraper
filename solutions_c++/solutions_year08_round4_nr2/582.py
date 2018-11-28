#include <stdio.h>
#include <iostream>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
typedef pair<int, int> PII;

int main() {
    FILE *fin = fopen("triangle.in", "r"), *fout = fopen("triangle.out", "w");
    int C; fscanf(fin, "%d", &C); REP(c, C) {
        int N, M, A; fscanf(fin, "%d %d %d", &N, &M, &A);
        fprintf(fout, "Case #%d: ", c+1);
        bool found = false;
        FOR(x2, 0, N) FOR(y2, 0, M) FOR(x3, 0, N) FOR(y3, 0, M) {
            if (!found && abs(x2*y3-y2*x3) == A) {
                fprintf(fout, "0 0 %d %d %d %d\n", x2, y2, x3, y3);
                found = true;
            }
        }
        if (!found) fprintf(fout, "IMPOSSIBLE\n");
    }
    return 0;
}
