#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        scanf("%d", &N);
        int ans = 0;
        for (int i = 1; i <= N; ++i)
        {
            int num;
            scanf("%d", &num);
            if (num != i)
                ++ans;
        }
        printf("Case #%d: %d\n", testcase, ans);
    }
    return 0;
}
