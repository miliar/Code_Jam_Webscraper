#include <stdio.h>
#include <iostream>
#define INF 0x3f3f3f3f
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define CLEAR(t) memset(t, 0, sizeof(t))
typedef pair<int, int> PII;

int N, T, num[2];
PII trip[2][105]; bool seen[2][105]; int res[2];

int tomin(char s[6]) { return (s[0]-'0')*(10*60)+(s[1]-'0')*(60)+(s[3]-'0')*(10)+(s[4]-'0'); }

int main() {
    FILE *fin = fopen("train.in", "r"), *fout = fopen("train.out", "w");
    fscanf(fin, "%d", &N); REP(n, N) {
        fscanf(fin, "%d %d %d", &T, &num[0], &num[1]);
        REP(i, 2) REP(j, num[i]) {
            char d[6], a[6]; fscanf(fin, "%s %s", &d, &a);
            trip[i][j] = PII(tomin(a)+T, tomin(d));
        }
        trip[0][num[0]] = trip[1][num[1]] = PII(INF, INF);

        CLEAR(seen); CLEAR(res);
        int done = 0; while(done < num[0]+num[1]) {
            int dir = 0, id = num[0]; REP(i, 2) REP(j, num[i])
                if (!seen[i][j] && trip[i][j] < trip[dir][id])
                    dir = i, id = j;
            res[dir]++;

            while(true) {
                done++; seen[dir][id] = true;
                int arrive = trip[dir][id].first;
                dir = 1-dir; id = num[dir]; REP(i, num[dir])
                    if (!seen[dir][i] && trip[dir][i].second >= arrive && trip[dir][i] < trip[dir][id])
                        id = i;
                if (id == num[dir]) break;
            }
        }
        fprintf(fout, "Case #%d: %d %d\n", n+1, res[0], res[1]);
    }
    return 0;
}
