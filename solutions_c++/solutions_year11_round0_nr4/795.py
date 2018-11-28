#include <iostream>
#include <list>


int main()
{
    std::cout.setf(std::ios::fixed);
    std::cout.precision(6);

    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int n;
        std::cin >> n;
        int r = 0;
        for (int i = 1 ; i <= n ; ++i)
        {
            int z;
            std::cin >> z;
            if (z != i)
                ++r;
        }
        std::cout << "Case #" << t << ": ";
        std::cout << (double)r << "\n";
    }
}
