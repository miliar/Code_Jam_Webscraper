#include <cstdio>
using namespace std;

int N, K, B, T;
int vs[64];
int xs[64];

int main()
{
    int C;
    scanf("%d", &C);

    for(int t = 1; t <= C; t++)
    {
        printf("Case #%d: ", t);

        scanf("%d%d%d%d", &N, &K, &B, &T);
        for(int i = 0; i < N; i++)
            scanf("%d", xs + i);
        for(int i = 0; i < N; i++)
            scanf("%d", vs + i);

        
        int total = 0;
        int ans = 0;
        for(int i = N - 1, alc = 0; i >= 0; i--)
            if((B - xs[i]) > T * vs[i])
                alc++;
            else
            {
                ans += alc;
                if(++total >= K)
                    break;
            }


        if(total >= K)
            printf("%d\n", ans);
        else
            printf("IMPOSSIBLE\n");

    }

    return 0;
}
