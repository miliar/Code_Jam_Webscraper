#include <iostream>
#include <cstring>

#define N 1024
using namespace std;

int main()
{
    int t, test = 1, n;
    int i;
    int x[1024];
    int temp, sum, small;

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &n);
        temp = sum = 0;
        small = INT_MAX;
        for (i=0; i<n; i++)
        {
            scanf("%d", &x[i]);
            temp ^= x[i];
            sum += x[i];
            small = min(small, x[i]);
        }

        if (temp)
            printf("Case #%d: NO\n", test++);
        else
            printf("Case #%d: %d\n", test++, sum - small);
    }

    return 0;
}
