#include <stdio.h>
#include <algorithm>

#define AL_NUM 128

int main()
{
    long N, P, K, L;
    int i, j, k, l;
    long Fre[AL_NUM];

    scanf("%d", &N);
    for (i = 1; i <= N; i++)
    {
        scanf("%d%d%d", &P, &K, &L);
        for (j = 0; j < L; j++)
        {
            scanf("%d", &Fre[j]);
        }
        std::sort(Fre, Fre + L);
        long Sum = 0;
        j = L - 1;
        k = 0;
        while (j >= 0)
        {
            for (l = 0; l < K && j >= 0; l++)
            {
                Sum += Fre[j--] * (k + 1);
            }
            k++;
        }
        printf("Case #%d: %d\n", i, Sum);
    }
}