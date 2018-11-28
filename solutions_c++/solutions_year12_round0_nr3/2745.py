#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int res;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca)
    {
        int a, b, s = 1, ta;
        scanf("%d%d", &a, &b);
        ta = a;
        while (ta)
        {
            ta /= 10;
            s *= 10;
        }
        s /= 10;
        res = 0;
        for (int i = a; i <= b; ++i)
        {
            int t = i;
            do
            {
                t = (t % 10) * s + t / 10;
                if ((t <= b) && (t > i)) ++res;
            }while(t != i);
        }
        printf("Case #%d: %d\n", ca, res);
    }
}


