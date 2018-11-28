#include <stdio.h>

int main()
{
    int T, R, k, N, g[1001];
    long long result = 0;
    int order[1001];
    long long number[1001];

    scanf("%d", &T);

    for(int i = 1; i <= T; i++)
    {
        scanf("%d %d %d", &R, &k, &N);
        
        for(int j = 0; j < N; j++)
        {
            scanf("%d", g+j);
        }

        for(int j = 0; j < 1001; j++)
        {
            order[j] = -1;
            number[j] = 0;
        }

        int pregIdx = 0;
        int gIdx = 0;
        int idx = 0;
        for(;order[idx] == -1;)
        {
            pregIdx = gIdx;
            while(number[idx]+g[gIdx] <= k)
            {
                number[idx] += g[gIdx];
                gIdx++;
                if(gIdx >= N) gIdx = 0;
                if(gIdx == pregIdx) break;
            }

            order[idx] = gIdx;
            idx = gIdx;
        }

        result = 0;
        idx = 0;
        for(int j = 0; j < R; j++)
        {
            result += number[idx];
            idx = order[idx];
        }
        
        printf("Case #%d: %lld\n", i, result);
    }
}
