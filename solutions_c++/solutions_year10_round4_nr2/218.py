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

        int p;
        std::cin >> p;
        int num = 1 << p;
        std::vector<int> m(num);
        for (int i = 0 ; i < num ; ++i)
            std::cin >> m[i];
        for (int k = num / 2 ; k > 0 ; k /= 2)
        {
            int price;
            for (int i = 0 ; i < k ; ++i)
                std::cin >> price;
        }

        std::vector<int> z(num * 2);
        for (int i = 0 ; i < num ; ++i)
        {
            int visit = p - m[i];
            int shift = p;
            int curr = 1;
            while (visit--)
            {
                z[curr] = 1;
                --shift;
                curr = curr * 2 + ((i >> shift) & 1);
            }
        }

        int sum = 0;
        for (int i = 0 ; i < 2 * num ; ++i)
            sum += z[i];

        std::cout << sum << "\n";
    }
    return 0;
}
