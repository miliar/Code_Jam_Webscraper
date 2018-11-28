#include <stdio.h>
#include <iostream>
#include <vector>
#define MAX 1000
#define INF LLONG_MAX
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define ALL(t) t.begin(), t.end()
#define SIZE(t) t.size()
typedef long long LL;

int T, N; int zeroes[2]; vector<LL> num[2][2];
vector<LL> unused[2];

int main() {
    FILE *fin = fopen("scalar.in", "r"), *fout = fopen("scalarfast.out", "w");
    fscanf(fin, "%d", &T); REP(t, T) {
        fscanf(fin, "%d", &N);
        zeroes[0] = zeroes[1] = 0;
        REP(k, 2) {
            num[k][0].clear(); num[k][1].clear();
            REP(i, N) {
                LL v; fscanf(fin, "%lld", &v);
                if (v < 0) num[k][0].push_back(-v);
                else if (v > 0) num[k][1].push_back(v);
                else zeroes[k]++;
            }
        }
        REP(k, 2) REP(i, 2) sort(ALL(num[k][i]));

        LL res = 0; unused[0].clear(); unused[1].clear();

        int take = min(SIZE(num[0][0]), SIZE(num[1][1]));
        int a = SIZE(num[0][0]), b = SIZE(num[1][1]); REP(i, take) {
            res += num[0][0][a-1]*num[1][1][b-1];
            a--, b--;
        }
        while(a) unused[0].push_back(num[0][0][a-1]), a--;
        while(b) unused[1].push_back(num[1][1][b-1]), b--;

        take = min(SIZE(num[0][1]), SIZE(num[1][0]));
        a = SIZE(num[0][1]), b = SIZE(num[1][0]); REP(i, take) {
            res += num[0][1][a-1]*num[1][0][b-1];
            a--, b--;
        }
        while(a) unused[0].push_back(num[0][1][a-1]), a--;
        while(b) unused[1].push_back(num[1][0][b-1]), b--;

        sort(ALL(unused[0])); sort(ALL(unused[1]));
        REP(k, 2) unused[k].resize(max(0, (int)SIZE(unused[k])-zeroes[1-k]));
        reverse(ALL(unused[0]));
        REP(i, min(SIZE(unused[0]), SIZE(unused[1]))) res -= unused[0][i]*unused[1][i];
        fprintf(fout, "Case #%d: %lld\n", t+1, -res);
    }
    return 0;
}
