#include <stdio.h>

int main() {
    int t,i,j,point,start_point,midsum;
    long long R,k,N;
    long long g[1000];
    long long sum;

    scanf("%d",&t);
    for (i=1;i<=t;i++) {
        scanf("%lld %lld %lld",&R,&k,&N);
        for (j=0;j<N;j++)
            scanf("%lld",&g[j]);
        sum = 0;
        point = 0;
        while (R--) {
            midsum = 0;
            start_point = point;
            while (midsum+g[point]<=k) {
                midsum += g[point];
                point++;
                if (point==N)
                    point = 0;
                if (point == start_point)
                    break;
            }
            sum += midsum;
        }
        printf("Case #%d: %lld\n",i,sum);
    }
}
