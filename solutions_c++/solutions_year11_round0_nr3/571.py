#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>

using namespace std;

int t,n;
int a[1005];
int main(int argc, char** argv) {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&t);
    for(int v = 1;v <= t; ++v){
        scanf("%d",&n);
        for(int i = 0;i < n; ++i) scanf("%d",&a[i]);
        sort(a,a+n);
        int x = a[0],ans = 0;
        for(int i = 1;i < n; ++i){
            x ^= a[i];ans += a[i];
        }
        printf("Case #%d: ",v);
        if(!x) printf("%d\n", ans);
        else printf("NO\n");
    }
    return 0;
}

