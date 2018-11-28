#include <cstdio>
#include <cstdlib>

int main()
{
    int T, tIdx;
    scanf("%d", &T);
    int minCandy;
    int N, nIdx;
    int i, j, sum;
    for (tIdx = 0; tIdx < T; ++tIdx)
    {
        minCandy = 10000000;
        sum = -minCandy;
        j = 0;
        scanf("%d", &N);
        for (nIdx = 0; nIdx < N; ++nIdx)
        {
            scanf("%d", &i);
            if (i < minCandy)
            {
                sum += minCandy;
                minCandy = i;
            }
            else
                sum += i;
            j = i ^ j;
        }
        if (j == 0)
            printf("Case #%d: %d\n", tIdx + 1, sum);
        else
            printf("Case #%d: NO\n", tIdx + 1);
    }
    return 0;
}
