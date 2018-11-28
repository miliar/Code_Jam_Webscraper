#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>


using namespace std;


int gcd(int a, int b)
{
    if(b == 0)
        return a;
    return gcd(b, a % b);
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        __int64 n;
        int d, g;
        cin >> n >> d >> g;
        if((g == 100 && d != 100) || (g == 0 && d != 0))
            printf("Case #%d: Broken\n", i);
        else
        {
            int yue = gcd(100, d);
            __int64 small = 100 / yue;
            if(small <= n)
                printf("Case #%d: Possible\n", i);
            else
                printf("Case #%d: Broken\n", i);
        }
    }

    return 0;
}
