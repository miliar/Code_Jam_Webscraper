#include <cstdio>
#include <cstdlib>
#include <cstring>

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define FOREACH(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ITER(c) __typeof((c).begin())
#define SZ(a) (int)(a).size()
#define MAXN 1000

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w+", stdout);
    int n;
    scanf("%d", &n);
    REP(i, n) {
        char line[MAXN], com[40][4], des[30][3], mag[200], token[10], end[200] = "";
        int p = 0, nc, nd, nl;

        scanf("%s", token);
        nc = atoi(token);
        REP(j, nc) {
            scanf("%s", com[j]);
            // printf("%s\n", com[j]);
        }

        scanf("%s", token);
        nd = atoi(token);
        REP(j, nd) {
            scanf("%s", des[j]);
            //printf("%s\n", des[j]);
        }

        scanf("%s", token);
        nl = atoi(token);
        scanf("%s", mag);
        //printf("%s\n", mag);
        
        strncat(end, mag, 1);
        FOR(j, 1, nl - 1) {
            strncat(end, (mag + j), 1);
            int le = strlen(end);
            //printf("%s %d\n", end, j);
            if (le == 1) continue;

            int wh = -1;    // combining
            REP(k, nc)
                if((com[k][0] == end[le - 1] && com[k][1] == end[le - 2]) ||
                    (com[k][1] == end[le - 1] && com[k][0] == end[le - 2])) {
                    wh = k;
                    break;
                }
            if (wh != -1) {
                end[le - 2] = com[wh][2];
                end[le - 1] = '\0';
                continue;
            }

            //printf("%d", le);
            FOR(k, 0, le - 2) {
                bool st = false;
                REP(l, nd)
                    if((des[l][0] == end[le - 1] && des[l][1] == end[k]) ||
                        (des[l][0] == end[k] && des[l][1] == end[le - 1])) {
                        end[0] = '\0';
                        st = true;
                        break;
                    }
                if (st) break;
            }
        }

        int le = strlen(end);
        printf("Case #%d: [", i + 1);
        if (le == 0) {
            printf("]\n");
            continue;
        } else if (le == 1) {
            printf("%s]\n", end);
        } else {
            printf("%c", end[0]);
            FOR(j, 1, le - 1)
                printf(", %c", end[j]);
            printf("]\n");
        }
    }

    fclose(stdin);
    fclose(stdout);
}
