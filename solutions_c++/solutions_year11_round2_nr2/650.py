#include <cstdio>
#include <cstring>
#include <algorithm>
#define eps 1e-8
using namespace std;

int T, N, D, sumV;
int p[10010], cnt;
double POS[10010];

bool check(double time)
{
    POS[1] = 1.0 * p[1] - time;
    for (int i = 2; i <= sumV; ++i)
    {
        double can = POS[i - 1] + D;
        if (can < p[i])
        {
            POS[i] = max(can, 1.0 * p[i] - time);
        }
        else
        {
            if (can - p[i] - eps > time) return 0;
            else POS[i] = can;
        }
    }
    return 1;
}

int main()
{
    freopen("in.in", "r",stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d%d", &N, &D);
        sumV = 0;
        cnt = 0;
        for (int i = 1; i <= N; ++i)
        {
            int num, pos;
            scanf("%d%d", &pos, &num);
            for (int i = 1; i <= num; ++i)
                p[++cnt] = pos;
            sumV += num;
        }
        sort(p + 1, p + sumV + 1);
        double l = 0, r = double(sumV) * D, mid;
        while (l + eps < r)
        {
            mid = (l + r) / 2;
            if (check(mid)) r = mid;
            else l = mid;
        }
        printf("Case #%d: %.7f\n", cas, mid);
    }
    return 0;
}
