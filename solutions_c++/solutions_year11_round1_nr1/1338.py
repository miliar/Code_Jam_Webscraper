#include <iostream>
#include <cstring>

#define N 15
#define M 15
using namespace std;

int main()
{
    int t, test = 1;
    int n, a, b;
    int i, j;
    bool flag;

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    scanf("%d", &t);
    while (t--)
    {
        scanf("%d%d%d", &n, &a, &b);
        flag = 1;
        for (i=1; i<=n && flag; i++)
            for (j=i; j<=n*1000; j++)
                if (j*b%100 == 0 && a*i%100 == 0 && j*b >= i*a && j - j*b/100 >= i - i*a/100)
                {
                    flag = 0;
                    //printf("!!! %d %d\n", i, j);
                    break;
                }

        if (flag)
            printf("Case #%d: Broken\n", test++);
        else
            printf("Case #%d: Possible\n", test++);
    }

    return 0;
}
