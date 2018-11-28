#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <set>

using namespace std;

typedef pair<int,int> PII;

int d[10010], len[10010], n, D;
int melhor[10010];

int main() {
    int cases, cn=0;
    scanf("%d",&cases);
    while (cases--) {
        scanf("%d",&n);
        for (int i=0; i < n; ++i) {
            scanf("%d%d",&d[i],&len[i]);
        }
        scanf("%d",&D);
        memset(melhor,-1,sizeof(melhor));
        melhor[0] = d[0];
        for (int i=1; i < n; ++i) {
            for (int j=i-1; j >= 0; --j) {
                if (d[j] + melhor[j] >= d[i]) {
                    melhor[i] = max(melhor[i], min(d[i]-d[j], len[i]));
                }
            }
        }
        bool ok = false;
        for (int i=0; i < n; ++i) {
            if (melhor[i] == -1) continue;
            if (d[i] + melhor[i] >= D) {
                ok=true;
                break;
            }
        }
        
        
        /*
        int at = 0, x = 0, r, nr, nx, aux, best;
        
        while (at < (n-1)) {
            r = d[at] - x;
            //printf("at %d raio %d\n",at,r);
            best = -1;
            for (int next = at+1; next < n; ++next) {
                if (d[next] - d[at] <= r) {
                    // I can reach.
                    //printf("next %d is reachable (dist %d len %d) D=%d\n",next,d[next]-d[at],len[next],D);
                    aux = min(d[next] - d[at], len[next]);
                    //if (best == -1) {
                        // I can climb and hold.
                        //printf("I can climb and hold it\n");
                        best = next;
                        nx = d[next]-aux;
                    //}
                } else {
                    break;
                }
            }
            //printf("I can reach %d\n", best);
            if (best == -1) break;
            else {
                x = nx;
                at = best;
            }
        }
        r = d[at] - x;
        //printf("final raio %d\n",r);
        */
        //if (d[at] + r >= D) printf("Case #%d: YES\n",++cn);
        if (ok) printf("Case #%d: YES\n",++cn);
        else printf("Case #%d: NO\n", ++cn);
        fflush(stdout);
    }

    return 0;
}
