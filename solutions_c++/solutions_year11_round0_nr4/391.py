#include <cstdio>
#include <cstdlib>
#include <cstring>

void init()
{
    int cas;
    scanf("%d", &cas);
    for (int i = 1; i <= cas; ++i)
    {
        int N;
        float cnt = 0;
        scanf("%d", &N);
        for (int j = 1; j <= N; ++j)
        {
            int tt;
            scanf("%d", &tt);
            cnt += (tt != j);
        }
        printf("Case #%d: %f\n", i, cnt);
    }
}

int main()
{
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    init();
    fclose(stdin);
    fclose(stdout);
    return 0;
}