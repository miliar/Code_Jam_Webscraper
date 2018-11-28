#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

const int INF = 2000000000;
const int MAXN = 1024;
int a[MAXN];

int main() {
    //freopen("C-small.in","r",stdin);
    //freopen("C-small.out","w",stdout);
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T, ca, i, n;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d",&n);
        int min = INF;
        int tot = 0, x = 0;
        for (i = 0 ; i < n ; i++) {
            scanf("%d",&a[i]);
            tot += a[i];
            x ^= a[i];
            if (a[i] < min) min = a[i];
        }
        printf("Case #%d: ",ca);
        if (x) {printf("NO\n"); continue;}
        printf("%d\n", tot - min);
    }
    return 0;
}
