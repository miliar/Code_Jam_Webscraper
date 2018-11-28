#include <cstdio>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum <= T; testnum++)
    {
        printf("Case #%d: ", testnum);
        int N;
        scanf("%d", &N);
        int ans = 0;
        for(int i = 1; i <= N; i++)
        {
            int v;
            scanf("%d", &v);
            
            ans += v != i;
        }

        printf("%d\n", ans);
    }
    return 0;
}
