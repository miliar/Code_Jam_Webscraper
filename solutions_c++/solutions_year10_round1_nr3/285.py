#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>

const double rate = (sqrt(5.0) + 1.0) / 2;
const double eps = 1e-8;

using namespace std;

bool check(int a, int b);

int main()
{
    freopen("C-small.in", "r", stdin);
   freopen("C-small.out", "w", stdout);
    int C = 0, T;

    scanf("%d", &T);
    while (T--)
    {
        int a1, a2, b1, b2;
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
        int res = 0;
        for(int i = a1; i <= a2; i++)
            for(int j = b1; j <= b2; j++)
                res += check(i, j);
        printf("Case #%d: %d\n", ++C, res);
    }

    return 0;
}

bool check(int a, int b)
{
    if(a < b)swap(a, b);
    return 1.0 * a / b > rate;
}
