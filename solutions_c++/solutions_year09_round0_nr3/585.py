#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::string welcome = "welcome to code jam";
    int N;
    std::cin >> N;
    std::string s;
    std::getline(std::cin, s);
    for (int n = 1 ; n <= N ; ++n)
    {
        std::getline(std::cin, s);
        std::vector<int> curr(welcome.size() + 1);
        curr[welcome.size()] = 1;
        for (int i = s.size() - 1 ; i >= 0 ; --i)
        {
            for (int j = 0 ; j < welcome.size() ; ++j)
                if (welcome[j] == s[i])
                    curr[j] = (curr[j] + curr[j + 1]) % 10000;
        }
        int k = curr[0];
        std::cout << "Case #" << n << ": ";
        if (k < 1000)
            std::cout << "0";
        if (k < 100)
            std::cout << "0";
        if (k < 10)
            std::cout << "0";
        std::cout << k << "\n";
    }
	return 0;
}

