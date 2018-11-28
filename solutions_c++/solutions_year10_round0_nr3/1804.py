#include <stdio.h>
#include <stdlib.h>
__int64 g[1010], next[1010], num[1010];
int main()
{
    __int64 t, r, k, n, count = 1, i, j, sum;
    FILE *finp = fopen("C-large.in","r");
	FILE *foutp = fopen("C.out","w");
    fscanf(finp, "%I64d", &t);
    //scanf("%d", &t);
    while (t--)
    {
        fscanf(finp, "%I64d %I64d %I64d", &r, &k, &n);
        //scanf("%d %d %d", &r, &k, &n);
        sum = 0;
        for (i = 0; i < n; i++) 
        {
            fscanf(finp, "%I64d", &g[i]);
            //scanf("%d", &g[i]);
            sum += g[i];
        }
        fprintf(foutp, "Case #%I64d: ", count++);
        //printf("Case #%d: ", count++);
        if (sum <= k)
        {
            fprintf(foutp, "%I64d\n", r*sum);
            //printf("%d\n", r*sum);
            continue;
        }
        else
        {
            for (i = 0; i < n; i++)
            {
                num[i] = g[i];
                j = (i+1) % n;
                while (num[i] + g[j] <= k)
                {
                    num[i] += g[j];
                    j = (j+1) % n;
                }
                next[i] = j;
            }
            sum = 0;j = 0;
            for (i = 0; i < r; i++)
            {
                sum += num[j];
                j = next[j];
            }
            fprintf(foutp, "%I64d\n", sum);
            //printf("%d\n", sum);
        }
    }
    return 0;
}
