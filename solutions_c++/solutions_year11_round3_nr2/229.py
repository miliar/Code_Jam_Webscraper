#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <cstdlib>


using namespace std;

__int64 l, t, n, c;
__int64 num[1000005];


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int ti = 0; ti < T; ++ti)
    {
        scanf("%I64d %I64d %I64d %I64d", &l, &t, &n, &c);
        for(int i = 0; i < c; ++i)
            scanf("%I64d", &num[i]);
        for(int i = c; i < n; ++i)
            num[i] = num[i % c];
        int i = 0;
        __int64 add = 0;

        while(i < n && add + num[i] * 2 < t)
        {
            add += num[i] * 2;
            ++i;
        }

        if(i == n)
            printf("Case #%d: %I64d\n", ti + 1, add);
        else
        {
            num[i] -= ((t - add) + 1) / 2;
            sort(num + i, num + n);
            __int64 an = t;
            for(int j = n - 1; j >= i; --j)
            {
                if(l)
                {
                    an += num[j];
                    -- l;
                }
                else
                    an += num[j] * 2;
            }
            printf("Case #%d: %I64d\n", ti + 1, an);
        }
    }

    return 0;
}
