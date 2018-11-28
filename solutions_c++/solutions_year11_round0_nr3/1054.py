#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

#define MaxN 1010
#define ll long long

int T;
int n;
int a[MaxN];
int mi;
ll sum;
int tr;

int main()
{
    freopen("test3.in","r",stdin);
    freopen("test3.out","w",stdout);

    scanf("%d",&T);
    for (int t = 0; t < T; ++t) {
        scanf("%d",&n);
        for (int i = 0; i < n; ++i)
            scanf("%d",&a[i]);

        sum = (ll)a[0];
        mi = 0;
        tr = a[0];
        for (int i = 1; i < n; ++i) {
            sum += (ll)a[i];

            tr ^= a[i];
            if ( a[mi] > a[i] ) mi = i;
        }

        printf("Case #%d: ",t+1);
        if ( tr == 0 ) {
            printf("%lld\n",sum-(ll)a[mi]);
        }
        else {
            printf("NO\n");
        }

    }

    return 0;
}
