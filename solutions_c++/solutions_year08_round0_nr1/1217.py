#include <cstdio>
#include <map>
#include <string>

#define INF 100000

#define REP(a, b) for(int a=0; a<(b); a++)

using namespace std;

int ile[1001][100];
char buf[1000];

int main() {
    int d;
    scanf("%d", &d);
    REP(z, d) {
        map<string, int> mapa;
        int q;
        scanf("%d\n", &q);
        REP(i, q) {
            fgets(buf, 1000, stdin);
            mapa[string(buf)] = i;
        }
        int p;
        scanf("%d\n", &p);
        REP(i, p) {
            fgets(buf, 1000, stdin);
            int ind = mapa[string(buf)];
            if (i==0) {
                REP(j, q) ile[i][j] = 0;
                ile[i][ind] = INF;
            } else
                REP(j, q) {
                    ile[i][j] = INF;
                    if (j != ind) REP(k, q) ile[i][j] = min(ile[i][j], ile[i-1][k] + (k!=j ? 1 : 0));
                }
        }
        int ret = INF;
        REP(i, q) ret = min(ret, ile[p-1][i]);
        printf("Case #%d: %d\n", z+1, ret);
    }
    return 0;
}
