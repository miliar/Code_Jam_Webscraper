#include <cstdio>
#include <cmath>
#include <algorithm>

#define LL long long

using namespace std;

int tab[1000];
LL A;
LL val;
LL mn;

int main()
{
    int T, N, k;
    scanf("%d", &T);
    
    for (int C = 1; C <= T; C++)
    {
        scanf("%d", &N);
        A = 0;
        val = 0;
        mn = 1000001;
        
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &k);
            tab[i] = k;
            A ^= k;
            val += k;
            if (k < mn) { mn = k; }
        }
        
        if (A != 0)
        {
            printf("Case #%d: NO\n", C);
        }
        else
        {
            printf("Case #%d: %lld\n", C, val-mn);
        }
    }
    
    return 0;
}