#include <stdio.h>
#include <string.h>

#define MAX_N 1024
#define INF 0x3f3f3f3f
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int K, st[16], u[16], min = INF, N;
char S[MAX_N], C[MAX_N];

void back(int lev)
{
     int i, j, comps = 0;

     if (lev == K)
     {
        for (i = 0; i < N; i += K)
            for (j = 0; j < K; j++)
                C[i + st[j]] = S[i + j];
        
        for (i = 0; i < N; i = j)
        {
            for (j = i + 1; j < N && C[j] == C[j - 1]; j++) ;
            comps++;
        }
        
        min = MIN(min, comps);
             
        return;
     }
     
     for (i = 0; i < K; i++)
         if (!u[i])
         {
            st[lev] = i;
            u[i] = 1;
            back(lev + 1);
            u[i] = 0;
         }
}

int main(void)
{
    int test, tests;

    freopen("d-small.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
    {
        scanf("%d\n%s", &K, S);
        N = strlen(S);
        min = INF;
        back(0);
        printf("Case #%d: %d\n", test, min);
    }
    
    return 0;
}
