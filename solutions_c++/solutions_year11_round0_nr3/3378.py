#include <stdio.h>
#include <limits.h>
int main()
{
    int i,n,m,j,val,teste;
    long long int sum,first;
    scanf("%d ",&n);

    for (i = 1; i<=n;i++)
    {
        teste = 0;
        sum = 0;
        first = LLONG_MAX;
        scanf("%d ",&m);
        for (j = 1; j <= m;j++)
        {
              scanf("%d ",&val);
              teste ^=val;
              if (val < first)
                first = val;
              sum +=val;
        }
        if (teste != 0)
            printf("Case #%d: NO\n",i);
        else
            printf("Case #%d: %lld\n",i, sum-first);
    }
}
