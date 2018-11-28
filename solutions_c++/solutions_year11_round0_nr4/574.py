#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;
int n,t;
int a[1005],b[1005];
int main(int argc, char** argv) {
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&t);
    for(int v = 1;v <= t; ++v){
        scanf("%d",&n);
        for(int i = 0;i < n; ++i){
            scanf("%d",&a[i]);
            b[i] = a[i];
        }
        sort(a,a+n);
        int ans = 0;
        for(int i = 0;i < n; ++i)
            if(b[i] != a[i]) ans ++;
        printf("Case #%d: %f\n",v,(double)ans);
    }
    return 0;
}

