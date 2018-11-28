#include <stdio.h>
#include <stdlib.h>

double loc[60];
double arr[60][3];

int cmp(const void * a, const void *b)
{
    return *((double*)(a)) > * ((double*)(b)) ? 1 : -1;
}

int main()
{
    int c,tt;
    int n,k,b,t;
    int i,j;
    int ans,ct;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&c);
    for (tt = 1; tt <= c; tt ++)
    {
        scanf("%d%d%d%d",&n,&k,&b,&t);
        for (i = 0; i < n; i ++)
            scanf("%lf",&arr[i][0]);
        for (i = 0; i < n; i ++)
            scanf("%lf",&arr[i][1]);

        for (i = 0; i < n; i ++)
        {
            arr[i][2] = (1.0 * b - arr[i][0]) / arr[i][1];
        }
        qsort(arr,n,sizeof(arr[0]),cmp);
        ans = 0;
        ct = 0;
        for (i = n - 1; i >= 0; i --)
        {
            if (arr[i][2] <= t)
            {
                ct ++;
                if (ct > k)
                    break;
                for (j = i + 1; j < n; j ++)
                {
                    if (arr[j][2] > t)
                        ans ++;
                }
            }
        }
        printf("Case #%d: ",tt);
        if (ct < k)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",ans);
    }
    return 0;
}
