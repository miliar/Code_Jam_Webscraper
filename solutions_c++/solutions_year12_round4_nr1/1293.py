#include <cstdio>
#include <cstring>
#include <vector>
#include <map>

#define min(a, b) (a < b ? a : b)

using namespace std;

typedef pair<int,int> ii;
int T, n, D, C=1;
int dist[128], tam[128];
map<ii,bool> PD;

bool da(int u, int l) {
    if (dist[u] + l >= D) return true;
    map<ii,bool>::iterator PDi;
    PDi = PD.find(ii(u,l));
    if (PDi != PD.end())
        return PDi->second;
    for (int i=u+1;i<n;i++) {
        if (dist[i] > dist[u]+l) break;
        int nl = dist[i]-dist[u];
        nl = min(nl,tam[i]);
        if (da(i,nl)) return PD[ii(u,l)] = true;
    }
    return PD[ii(u,l)] = false;
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        PD.clear();
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%d %d",dist+i,tam+i);
        scanf("%d",&D);
        if (da(0,dist[0]))
            printf("YES\n");
        else
            printf("NO\n");

    }

    return 0;
}
