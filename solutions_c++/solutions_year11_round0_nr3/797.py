#include <iostream>
#include <list>


int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int res = 0;
        int min = 10000000;
        int sum = 0;
        int n;
        std::cin >> n;
        while (n--)
        {
            int i;
            std::cin >> i;
            res ^= i;
            sum += i;
            if (min > i)
                min = i;
        }
        std::cout << "Case #" << t << ": ";
        if (res == 0)
            std::cout << sum - min;
        else
            std::cout << "NO";
        std::cout << "\n";
    }
}
