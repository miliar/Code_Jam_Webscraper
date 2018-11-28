#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int list[1010];

int main()
{
    int aa, nn, n, t, i, ans, m;
    scanf("%d",&nn);
    for ( aa = 1; aa <= nn; ++aa ) {
        scanf("%d",&n);
        m = 0x7fffffff; ans = 0; t = 0;
        for ( i = 0; i < n; ++i ) {
            scanf("%d",&list[i]);
            t ^= list[i];
            m = min(m,list[i]);
            ans += list[i];
        }
        if ( t ) {
            printf("Case #%d: NO\n",aa);
            continue;
        }
        ans -= m;
        printf("Case #%d: %d\n",aa,ans);
    }
    return 0;
}
