#include <iostream>
#include <cstring>
#include <queue>

#define N 128
using namespace std;

int main()
{
    int t, test = 1;
    int n, a, b;
    int i, j;
    int x[N];

    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    scanf("%d", &t);
    while (t--)
    {
        scanf("%d%d%d", &n, &a, &b);
        for (i=0; i<n; i++)
            scanf("%d", &x[i]);

        for (i=a; i<=b; i++)
        {
            for (j=0; j<n; j++)
                if (x[j]%i != 0 && i%x[j] != 0)
                    break;
            if (j == n)
                break;
        }

        printf("Case #%d: ", test++);
        if (i <= b)
            printf("%d\n", i);
        else
            printf("NO\n");
    }

    return 0;
}
