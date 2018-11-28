#include <stdlib.h>

#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int numCases;
    std::cin >> numCases;

    std::vector<int> values;

    for (int i = 0; i < numCases; i++)
    {
        std::cout << "Case #" << (i + 1) << ": ";

        uint64_t n, pd, pg;
        std::cin >> n >> pd >> pg;

        bool valid = false;

        if (n >= 100 || pd == 100 || pd == 0) { valid = true; }
        else if (pd % 50 == 0) { valid = n >= 2; }
        else if (pd % 25 == 0) { valid = n >= 4; }
        else if (pd % 20 == 0) { valid = n >= 5; }
        else if (pd % 10 == 0) { valid = n >= 10; }
        else if (pd % 5 == 0) { valid = n >= 20; }
        else if (pd % 4 == 0) { valid = n >= 25; }
        else if (pd % 2 == 0) { valid = n >= 50; }

        valid = valid && (pd == 100 || pg != 100) && (pd == 0 || pg != 0);

        if (valid) { std::cout << "Possible"; }
        else { std::cout << "Broken"; }

        std::cout << std::endl;
    }
}
