#include <iostream>


int main()
{
    int T, n, k;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cin >> n >> k;
        k = k & ((1 << n) - 1);
        std::cout << "Case #" << t << ": ";
        if (k == ((1 << n) - 1))
            std::cout << "ON\n";
        else
            std::cout << "OFF\n";
    }
	return 0;
}

