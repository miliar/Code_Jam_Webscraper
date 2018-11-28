#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

int x[32];
int y[32];
int r[32];

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d: ", nc);
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d%d%d", &x[i], &y[i], &r[i]);
        }
        if (n == 1)
        {
            double min = r[0];
            printf("%lf\n", min);
        }
        else if (n == 2)
        {
            double min = r[0] > r[1] ? r[0] : r[1];
            printf("%lf\n", min);
        }
        else
        {
            double min = -1;
            for (int i = 0; i < 3; i++)
            {
                for (int j = i + 1; j < 3; j++)
                {
                    double dx = x[i] - x[j], dy = y[i] - y[j];
                    double r1 = (r[i] + r[j] + sqrt(dx * dx + dy * dy)) / 2.0;
                    double r2 = r[3 - i - j];
                    if (r1 < r2)
                    {
                        r1 = r2;
                    }
                    if (min < 0 || min > r1)
                    {
                        min = r1;
                    }
                }
            }
            printf("%lf\n", min);
        }
    }
    return 0;
}
