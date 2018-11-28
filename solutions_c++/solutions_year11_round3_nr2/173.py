#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <queue>

using namespace std;

int l, n, c;
long long t, tt;
int list[1000010];
int dist[1000010];
priority_queue<int> que;

int main()
{
    int aa, nn, i, j;
    long long ans;
    scanf("%d",&nn);
    for ( aa = 1; aa <= nn; ++aa ) {
        scanf("%d %lld %d %d",&l,&t,&n,&c);
        for ( i = 0 ; i < c; i++ )
            scanf("%d",&list[i]);
        for ( i = 0, j = 0; i < n; i++, j = (j+1)%c ) {
            dist[i] = list[j];
        }
        ans = 0;
        for ( i = 0, tt = 0; i < n; i++ ) {
            if ( tt + (dist[i] << 1) <= t )
                tt += (dist[i] << 1 );
            else {
                ans = t;
                tt = tt + (dist[i] << 1) - t;
                tt >>= 1;
                que.push((int)tt);
                break;
            }
        }
        if ( i == n ) {
            ans = tt;
        } else {
            for ( ++i; i < n; i++ ) {
                que.push(dist[i]);
            }
            for ( j = 0; j < l && !que.empty(); j++ ) {
                ans += que.top();
                que.pop();
            }
            while ( !que.empty() ) {
                ans += (que.top()<<1);
                que.pop();
            }
        }
        printf("Case #%d: %lld\n",aa,ans);
    }
    return 0;
}
