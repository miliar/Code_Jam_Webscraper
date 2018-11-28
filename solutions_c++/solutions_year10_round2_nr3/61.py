#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#include <map>
#include <set>
#include <list>

long long a[1000][1000];
int c[1000][1000];

int main()
{
    c[0][0] = 1;
    for (int n = 1 ; n <= 500 ; ++n)
    {
        c[n][0] = 1;
        for (int k = 1 ; k <= n ; ++k)
            c[n][k] = (c[n-1][k] + c[n-1][k-1]) % 100003;
    }
    for (int i = 2 ; i <= 500 ; ++i)
        a[i][1] = 1;
    for (int sz = 2 ; sz <= 500 ; ++sz)
    {
        for (int n = 2 ; n <= 500 ; ++n)
        {
            if (n > sz)
            {
                for (int k = 1 ; k <= sz-1 ; ++k)
                {
                    a[n][sz] = (a[n][sz] + a[sz][sz - k] * c[n-sz-1][k-1]) % 100003;
                }
            }
        }
    }

    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cout << "Case #" << t << ": ";
        int n;
        std::cin >> n;
        long long res = 0;
        for (int i = 1 ; i < n ; ++i)
            res = (res + a[n][i]) % 100003;
        std::cout << res << "\n";
    }
    return 0;
}
