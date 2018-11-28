#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T;
int N, S, p;
int t[110];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        int ans = 0;
        scanf("%d%d%d", &N, &S, &p);
        for (int i = 1; i <= N; ++i)
            scanf("%d", t + i);
        sort(t + 1, t + N + 1);
        for (int i = 1; i <= N; ++i)
        {
            if (S && t[i] >= 3)
            {
                if (t[i] % 3 == 0)
                {
                    if (t[i] / 3 + 1 >= p)
                    {
                        ans++;
                        --S;
                    }
                }
                else if (t[i] % 3 == 1)
                {
                    if (t[i] / 3 + 1 >= p)
                    {
                        ans++;
                        --S;
                    }
                }
                else
                {
                    if ((t[i] + 1) / 3 + 1 >= p)
                    {
                        ans++;
                        --S;
                    }
                }
            }
            else
            {
                if (t[i] % 3 == 0)
                {
                    if (t[i] / 3 >= p) ans++;
                }
                else if (t[i] % 3 == 1)
                {
                    if (t[i] / 3 + 1 >= p) ans++;
                }
                else
                {
                    if ((t[i] + 1) / 3 >= p) ans++;
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}