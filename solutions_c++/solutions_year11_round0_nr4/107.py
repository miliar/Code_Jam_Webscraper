#include <cstdio>
#include <algorithm>
using namespace std;

int T, N;
int num[1001], oth[1001];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    for (int cases = 1; cases <= T; ++cases)
    {
        scanf("%d", &N);
        for (int i = 1; i <= N; ++i)
        {
            scanf("%d", num + i);
            oth[i] = num[i];
        }
        sort(oth + 1, oth + N + 1);
        double ans = 0;
        for (int i = 1; i <= N; ++i)
            ans += ((oth[i] == num[i]) ? 0 : 1);
        printf("Case #%d: %.6lf\n", cases, ans);
    }
    return 0;
}