#include <cstdio>
#include <algorithm>

using namespace std;

bool isNorm(int val, int p)
{
    int mx = val / 3;

    if(val % 3 > 0)
    {
        mx++;
    }

    return (mx >= p);
}

bool isStrange(int val, int p)
{
    int mx = val / 3;

    if(val % 3 > 0)
    {
        mx++;
    }

    if(val % 3 == 0 || val % 3 == 2)
    {
        mx++;
    }

    return (mx >= p);
}

int main()
{
    int t, kase = 1;
    int n, strange, pt;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);

    while(t--)
    {
        scanf("%d %d %d", &n, &strange, &pt);

        int cnt = 0, stcnt = 0;

        for(int i = 0; i < n; i++)
        {
            int score;
            scanf("%d", &score);

            if(score == 0)
            {
                if(pt == 0)
                {
                    cnt++;
                }

                continue;
            }

            if(isNorm(score, pt) == true)
            {
                cnt++;
            }
            else if(stcnt < strange && isStrange(score, pt) == true)
            {
                cnt++;
                stcnt++;
            }
        }

        printf("Case #%d: %d\n", kase++, cnt);
    }

    return 0;
}
