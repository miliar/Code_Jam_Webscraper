#include <cstdio>
#include<algorithm>
using namespace std;

int main() {
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t, tt, n, c;
    scanf("%d", &t);
    for (tt = 1; tt <= t; ++tt) {
        int Min = 100000000, sum = 0, ans = 0;
        scanf("%d", &n);
        while (n--) {
            scanf("%d", &c);
            ans+=c;
            Min=min(Min,c);
            sum^=c;
        }
        printf("Case #%d: ",tt);
        if(sum) printf("NO\n");
        else    printf("%d\n",ans-Min);
    }
    return 0;
}