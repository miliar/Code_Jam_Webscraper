#include <stdio.h>
#include <string.h>

#define MAX_N 1000

int F[MAX_N], A[MAX_N];

int main(void)
{
    int T, tests;

    freopen("a0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (T = 1; T <= tests; T++)
    {
        int P, K, L, i, cnt = 0, pressed = 0;
    
        scanf("%d%d%d", &P, &K, &L);
        for (i = 0; i < L; i++)
            scanf("%d", F + i), cnt += F[i] ? 1 : 0;
            
        if (cnt > P * K)
        {
           printf("Case #%d: Impossible\n", T);
           continue;
        }
            
        memset(A, 0, sizeof(A));
        
        for (i = 0; i < L; i++)
        {
            int max = -1, min = MAX_N + 1, pos, j, kpos;
            
            for (j = 0; j < L; j++)
                if (F[j] > max)
                   max = F[j], pos = j;
            if (max <= 0)
               break;
            for (j = 0; j < K; j++)
                if (A[j] < min)
                   min = A[j], kpos = j;
            pressed += max * (min + 1);
            A[kpos]++, F[pos] = -1;
        }
        
        printf("Case #%d: %d\n", T, pressed);
    }
    
    return 0;
}
