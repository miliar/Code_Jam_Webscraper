#include <cstdio>
#include <cstdlib>
using namespace std;

const int MAXN = 55;

int C, TC = 1, N, K, B, T, X [MAXN], V [MAXN];

int main ()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    
    for (scanf ("%d", &C); TC <= C; TC++)
    {
        scanf ("%d %d %d %d", &N, &K, &B, &T);
        
        for (int i = 0; i < N; i++)
            scanf ("%d", X + i);
        
        for (int i = 0; i < N; i++)
            scanf ("%d", V + i);
        
        int arrive = 0, swaps = 0;
        
        for (int i = N - 1; i >= 0 && arrive < K; i--)
            if (V [i] * T >= B - X [i])
            {
                swaps += N - 1 - i - arrive;
                arrive++;
            }
        
        if (arrive == K)
            printf ("Case #%d: %d\n", TC, swaps);
        else
            printf ("Case #%d: IMPOSSIBLE\n", TC);
    }
    
    //system ("pause");
}
