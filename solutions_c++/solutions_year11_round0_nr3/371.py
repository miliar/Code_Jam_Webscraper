#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    //freopen("C2.in", "r", stdin);
    //freopen("C2.out", "w", stdout);
    int cas;

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        int N;

        scanf("%d", &N);

        int sum = 0;
        int res = 0;
        int min = (1 << 30);
        for(int i = 0; i < N; i++)
        {
            int val;

            scanf("%d", &val);
            sum += val;
            res ^= val;
            if(val < min) min = val;
        }

        printf("Case #%d: ", cc + 1);
        if(res != 0) printf("NO\n");
        else printf("%d\n", sum - min);
    }
    return 0;
}
