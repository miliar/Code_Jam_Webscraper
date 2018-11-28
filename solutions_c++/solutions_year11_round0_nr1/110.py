#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int n, p1, p2;

struct node
{
    int pp, t;
} p[2][101];

int main()
{
    freopen("in.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int T, pos, ans;
    char name[5];
    scanf("%d", &T);
    for (int cases = 1; cases <= T; ++cases)
    {
        ans = 0;
        p1 = p2 = 0;
        int POS[] = {1, 1};
        int last[] = {0, 0};
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
        {
            scanf("%s%d", name, &pos);
            if (name[0] == 'B')
            {
                p[0][++p1].pp = pos;
                p[0][p1].t = i;
            }
            else
            {
                p[1][++p2].pp = pos;
                p[1][p2].t = i;
            }
        }
        p[0][p1 + 1].t = 999999;
        p[1][p2 + 1].t = 999999;
        int i1 = 1, i2 = 1;
        for (int i = 1; i <= n; ++i)
        {
            int cost;
            if (p[0][i1].t < p[1][i2].t)
            {
                cost = abs(POS[0] - p[0][i1].pp);
                POS[0] = p[0][i1].pp;
                ++i1;
                if (ans - last[0] < cost)
                    ans = last[0] + cost;
                ++ans;
                last[0] = ans;
            }
            else if (p[0][i1].t > p[1][i2].t)
            {
                cost = abs(POS[1] - p[1][i2].pp);
                POS[1] = p[1][i2].pp;
                ++i2;
                if (ans - last[1] < cost)
                    ans = last[1] + cost;
                ++ans;
                last[1] = ans;
            }
        }
        printf("Case #%d: %d\n", cases, ans);
    }
    return 0;
}