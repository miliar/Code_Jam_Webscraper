#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int tmp[201],num[201],pos[201];
int n, d;

bool check(double x)
{
    memcpy(tmp, num, sizeof(num));
    double last = pos[0] - x;
    tmp[0]--;
    for (int i = 0; i < n; i++)
    {
        while(tmp[i] > 0)
        {
            if (pos[i] + x - last < d) return 0;
            else
            {
                last = pos[i] - x -last >= d ?  pos[i] - x : last + d;
                tmp[i]--;
            }
        }
    }
    return 1;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int tt;
    scanf("%d", &tt);
    for (int t = 0; t < tt; t++)
    {
        printf("Case #%d: ", t + 1);
        cin >>n >>d;
        for (int i = 0; i < n; i++)
        {
            scanf("%d%d", &pos[i], &num[i]);
        }
        double st = 0, ed = 2000000000;
        while (ed - st > 1e-8)
        {
            double mid = (double)(st + ed) / 2;
            if (!check(mid)) st = mid;
            else ed = mid;
        }
        cout <<st <<endl;

    }

    return 0;
}
