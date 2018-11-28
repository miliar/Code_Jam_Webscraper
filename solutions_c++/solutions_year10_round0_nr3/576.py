#include<cstdio>

long long groups[1100];
long long value[1100];
long long next[1100];

int main()
{
    int t, teste;
    scanf("%d", &teste);
    for (t=1; t<=teste; t++)
    {
        int n;
        long long r, k;
        scanf("%I64d %I64d %d", &r, &k, &n);
        int i, j;
        long long sum = 0;
        for (i=0; i<n; i++)
        {
            scanf("%I64d\n", &groups[i]);
            sum += groups[i];
        }
        printf("Case #%d: ", t);
        if (sum <= k)
        {
            printf("%I64d\n", sum * r);
        }
        else
        {
            for (i=0; i<n; i++)
            {
                j = i;
                long long tempsum = 0;
                while(tempsum + groups[j] <= k)
                {
                    tempsum += groups[j];
                    j = (j + 1) % n;
                }
                value[i] = tempsum;
                next[i] = j;
            }
            long long resp = 0;
            j = 0;
            for (i=0; i<r; i++)
            {
                resp += value[j];
                j = next[j];
            }
            printf("%I64d\n", resp);
        }
    }
    return 0;    
}
