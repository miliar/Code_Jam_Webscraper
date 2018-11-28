#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#include <map>
#include <set>
#include <list>


int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cout << "Case #" << t << ": ";
        int res = 0;
        {
            int n,k,b,t;
            std::cin >> n >> k >> b >> t;
            std::vector<int> x(n), v(n);
            std::vector<double> tt(n);
            std::vector<bool> yes(n);
            for (int i = 0 ; i < n ; ++i)
                std::cin >> x[i];
            for (int i = 0 ; i < n ; ++i)
            {
                std::cin >> v[i];
                tt[i] = (double)(b - x[i]) / v[i];
                if (t * v[i] >= b - x[i])
                    yes[i] = true;
            }
            int count = 0;
            for (int i = n - 1 ; i >= 0 && count < k ; --i)
            {
                if (yes[i])
                {
                    for (int j = i + 1 ; j < n ; ++j)
                        if (!yes[j])
                            ++res;
                    ++count;
                }
            }
            if (count < k)
                res = -1;
        }
        if (res == -1)
            std::cout << "IMPOSSIBLE\n";
        else
            std::cout << res << "\n";
    }
    return 0;
}
