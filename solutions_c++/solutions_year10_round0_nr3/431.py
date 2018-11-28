#include <stdlib.h>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <algorithm>
#include <cmath>
using namespace std;


int main()
{
//    freopen("a.in", "r", stdin);
//    freopen("a.out", "w", stdout);
    int test_case;
    scanf("%d", &test_case);
    int num[1024];
    int add[1024], next[1024];
    long long sum = 0;
    long long result = 0;

    for (int test = 1; test <= test_case; ++test)
    {
        int R, k, n;
        scanf( "%d %d %d", &R, &k, &n);
        sum = 0;
        for (int i = 0; i < n; ++i)
            scanf( "%d", &num[i] ), sum += num[i];
        if (sum <= k) result = R * (long long)sum;
        else
        {
            result = 0;
            memset(add, 0, sizeof(add));
            for (int i = 0; i < n; ++i)
            {
                for (int j = i; ; j = (j+1) % n)
                {
                    if (add[i] + num[j] > k)
                    {
                        next[i] = j;
                        break;
                    }
                    else add[i] += num[j];
                }
            }
            int now = 0;
            for (int i = 0; i < R; ++i)
            {
                result += add[now];
                now = next[now];
            }
        }
        printf( "Case #%d: ", test );
        cout << result << endl;
    }

    return 0;
}