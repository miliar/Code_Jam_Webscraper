#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;

LL cache[103][103];

LL best(int a[102], int first,int last) {
    if(first+1>=last) return 0;
    LL& ca = cache[first][last];
    if(ca==-1) {
        ca=(1LL << 62);
        for(int i=first+1;i<last;i++) {
            ca = min(ca,
                    best(a,first,i) + best(a,i,last) +
                    a[last] - a[first] - 2);
        }
    }
    return ca;
}

LL go() {
    int n,range;
    memset(cache,-1,sizeof(cache));
    int a[102];
    scanf("%d %d",&range, &n);
    a[0]=0;
    a[n+1]=range+1;
    for(int i=1;i<=n;i++) {
        scanf("%d", &a[i]);
    }
    sort(a+1,a+n+1);
    return best(a,0,n+1);
}

int main() {
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        printf("Case #%d: %lld\n", i, go());
    }
}
