#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef long long hugeint;
const hugeint MAXN = 1100;

hugeint solve(void)
{
    hugeint G[MAXN], money[MAXN], to[MAXN];
    hugeint sum[MAXN];
    hugeint i, j, R, K, N, c, k, mid;
    bool flag[MAXN];

    scanf("%lld%lld%lld", &R, &K, &N);

    sum[0] = 0;
    for(i=0; i<N; i++){
        scanf("%lld", &G[i]);
        sum[0] += G[i];
    }

    if(sum[0]<=K){
        return (sum[0]*R);
    }

    for(i=0; i<N; i++){
        money[i] = G[i];
        for(j=(i+1)%N; j!=i; j=(j+1)%N){
            if(money[i]+G[j]<=K){
                money[i] += G[j];
            }
            else break;
        }
        to[i] = j;
    }

    for(i=0; i<N; i++)
        flag[i] = false;

    sum[0] = 0;
    for(i=c=0; !flag[i]; i=to[i]){
        flag[i] = true;
        ++c;
        if(c>R) return sum[0];
        sum[0] += money[i];
    }
    mid = sum[0];
    R -= c;
    j = i;
    c=0; sum[0]=0;
    do{
        c++;
        sum[c]=sum[c-1]+money[i];
        i = to[i];
    }while(i!=j);

    i = (R/c)*sum[c]+mid;
    i = i+sum[R%c];
    return i;
}

int main()
{
    int T, i;

    //freopen("C-small.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    //freopen("C-small.out", "w", stdout);
    freopen("C-big.out", "w", stdout);

    scanf("%d", &T);
    for(i=1; i<=T; i++){
        printf("Case #%d: %lld\n", i, solve());
    }
    return 0;
}


