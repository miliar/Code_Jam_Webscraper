#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("largeout.txt", "w", stdout);
    int t, n;
    scanf("%d", &t);
    for (int k = 1; k <= t; k++)
    {
        int a, sum = 0;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &a);
            if (a != i)
                sum++;
        }
        printf("Case #%d: %.6f\n", k, 1.000000*sum);
    }
}
