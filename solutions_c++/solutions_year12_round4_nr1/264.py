#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <stack>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
typedef long long int64;
#define REP(i,n) for(int i=0; i<(n); i++)

struct par {
    int d,le;

    par(int d=0, int le=0): d(d), le(le) {}
} v[10010];

bool cmp(par a, par b) {
    return a.d < b.d;
}

int us[10010];

int main() {
    int nt;

    scanf(" %d",&nt);
    for (int ct=1;ct<=nt;ct++) {
        int n,dm;

        scanf("%d",&n);
        REP(i,n)
            scanf("%d %d",&v[i].d,&v[i].le);

        scanf("%d",&dm);
        v[n++]=par(dm,0);
        
        sort(v,v+n,cmp);

        queue<par> f;
        f.push(par(0, v[0].d));
        memset(us,0,sizeof(us));

        bool deu=false;
        while (!f.empty()) {
            par k = f.front();
            f.pop();

            for (int i=k.d+1; i<n; i++)
                if (v[k.d].d+k.le >= v[i].d) {
                    int nl;

                    if (i==n-1) {
                        deu=true;
                        break;
                    }
                    nl=min(v[i].le,v[i].d-v[k.d].d);

                    if (us[i]<nl) {
                        us[i]=nl;
                        f.push(par(i,nl));
                    }
                }
            if (deu) break;
        }
                    
        printf("Case #%d: ",ct);
        if (deu) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
