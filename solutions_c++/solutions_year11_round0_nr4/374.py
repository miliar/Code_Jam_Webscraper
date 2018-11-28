#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    //freopen("D2.in", "r", stdin);
    //freopen("D2.out", "w", stdout);

    int cas;

    scanf("%d", &cas);
    for(int cc = 0;cc < cas;cc++)
    {
        int N, val, cnt = 0;

        scanf("%d", &N);
        for(int i = 0;i < N;i++)
        {
            scanf("%d", &val);
            if(val != i + 1) cnt++;
        }
        printf("Case #%d: %lf\n", cc + 1, 1.0 * cnt);
    }
    return 0;
}
