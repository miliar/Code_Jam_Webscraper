#include <cstdio>
using namespace std;

const int MAXN = 1024;
int a[MAXN];

int main() {
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T, n, ca;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d",&n);
        int ans = 0;
        for (int i = 0 ; i < n ; i++) {
            scanf("%d",&a[i]);
            if (a[i] != i + 1) ++ans;
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
