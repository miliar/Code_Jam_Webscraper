#include <stdio.h>
#include <string.h>
#include <stdlib.h>

long long list[1010];
int next[1010];
long long sum[1010];

int main() {
    int aa, nn;
    int r, n, i, j;
    long long k;
    long long ans;

    scanf("%d",&nn);
    for ( aa =1 ;aa <= nn; aa++ ) {
        scanf("%d %lld %d",&r,&k,&n);
        for ( i = 0; i < n; i++ ) {
            scanf("%lld",&list[i]);
        }
        // compute next and sum
        for ( i = 0; i < n; i++ ) {
            sum[i] = list[i];
            for ( j=(i+1)%n; j != i; j = (j+1)%n ) {
                if ( sum[i] + list[j] <= k )
                    sum[i] += list[j];
                else
                    break;
            }
            next[i] = j;
            if ( i == j ) next[i] = (j+1)%n;
        }
        ans = j = 0;
        for ( i = 0; i < r; i++ ) {
            ans += sum[j];
            j = next[j];
        }
        printf("Case #%d: %lld\n",aa,ans);
    }
    
    return 0;
}

