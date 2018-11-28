#include <stdio.h>

#define MAXN 1100
long long arr[MAXN * 2];
long long sum[MAXN];
int next[2 * MAXN];
int visited[MAXN];
int main()
{
    long long R,k,ans;
    int i,j,cas,tt,amt,N;
    freopen("C-small-attempt5.in","r",stdin);
    freopen("C-small2.out","w",stdout);
    scanf("%d",&cas);
    for (tt = 1; tt <= cas; tt ++)
    {
        scanf("%lld%lld%d",&R,&k,&N);
        for (i = 0; i < 2 * N; i ++)
        {
            sum[i] = 0;
            next[i] = i;
        }
        for (i = 0; i < N; i ++)
        {
            scanf("%lld",&arr[i]);
            arr[i + N] = arr[i];
            visited[i] = 0;
        }

        for (i = 0; i < N; i ++)
        {
            sum[i] = 0;
            for (j = i; j < i + N; j ++)
            {
                if (sum[i] + arr[j] <= k)
                {
                    sum[i] += arr[j];
                    next[i] = j;
                }
                else
                    break;
            }
        }

        ans = 0;
        amt = 0;
        for (i = 0; amt < R; i = (next[i] + 1) % N)
        {
            ans += sum[i];
            amt ++;
        }

        printf("Case #%d: ",tt);
        printf("%lld\n",ans);

    }
    return 0;
}
