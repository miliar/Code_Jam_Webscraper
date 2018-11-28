#include <cstdio>

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, N, K;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d", &N, &K);
        N = (1<<N);
        K %= N;
        if(K == N-1) printf("Case #%d: ON\n", t);
        else      printf("Case #%d: OFF\n", t);
    }
    return 0;
}
