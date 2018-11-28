#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T, n, s, p, w, res;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca)
    {
        scanf("%d%d%d", &n, &s, &p);
        int a = p * 3 - 2;
        int b = p * 3 - 4;
        if (b < 0) b = p;
        res = 0;
        while (n--)
        {
            scanf("%d", &w);
            if (w >= a) ++res;
            else if ((w >= b) && (s > 0))
            {
                ++res;
                --s;
            }
        }
        printf("Case #%d: %d\n", ca, res);

    }
}


