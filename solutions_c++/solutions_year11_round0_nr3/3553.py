#include <stdio.h>
#include <limits.h>
#include <algorithm>

using namespace std;

int main()
{
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int numt;
    scanf("%d", &numt);
    for(int it=0;it<numt;++it) {
        int n=0;
        scanf("%d", &n);
        int xsum = 0;
        long long sum = 0;
        int minnum = INT_MAX;
        for(int i=0;i<n;++i) {
            int cur = 0;
            scanf("%d", &cur);
            xsum ^= cur;
            sum += cur;
            minnum = std::min(cur, minnum);
        }
        if( xsum==0 ) {
            printf("Case #%d: %lld\n", it+1, sum-minnum);
        }
        else {
            printf("Case #%d: NO\n", it+1);
        }
    }
    return 0;
}
