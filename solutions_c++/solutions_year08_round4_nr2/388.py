#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int cases;
int n, m, A;

int main()
{
    scanf("%d", &cases);

    for (int index = 1; index <= cases; ++index)
    {
        scanf("%d %d %d", &n, &m, &A);
        swap(n, m);

        if (A > n*m)
        {
            printf("Case #%d: IMPOSSIBLE\n", index);
        }
        else
        {
            bool flag = false;
            int x, y;
            int a, b;

            for (x = 0; x <= n; ++x)
            {
                for (y = 0; y <= n; ++y)
                {
                    for (a = 0; a <= m; ++a)
                    {
                        for (b = 0; a+b <= m; ++b)
                        {
                            if (x*b + a*y == A)
                            {
                                flag = true;
                                break;
                            }
                        }
                        if (flag)
                            break;
                    }
                    if (flag)
                        break;
                }
                if (flag)
                    break;
            }

            if (flag)
            {
                printf("Case #%d: %d %d %d %d %d %d\n", index,
                    0, x, a, 0, a+b, y);
            }
            else
            {
                printf("Case #%d: IMPOSSIBLE\n", index);
            }
        }

    }

    return 0;
}
