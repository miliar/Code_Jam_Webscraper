#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "r", stdin);
        freopen("out", "w", stdout);
    #endif

    int countTest;
    scanf("%d", &countTest);
    for (int test = 1; test <= countTest; test++)
    {
        printf("Case #%d: ", test);

        int n;
        scanf("%d", &n);
        int last[2] = {1, 1};
        int time[2] = {0, 0};
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            char c;
            int x, t;
            scanf(" %c %d", &c, &x);
            t = c == 'O';
            time[t] = max(ans, abs(x - last[t]) + time[t]) + 1;
            last[t] = x;
            ans = time[t];
        }
        printf("%d\n", ans);
    }
    return 0;
}
