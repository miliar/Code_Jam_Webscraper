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

        int numCandies;
        std::cin >> numCandies;

        values.clear();
        values.reserve(numCandies);

        for (int n = 0; n < numCandies; n++)
        {
            int candyValue;
            std::cin >> candyValue;
            values.push_back(candyValue);
        }

        std::sort(values.begin(), values.end());
        std::reverse(values.begin(), values.end());

        int maxEqual = 0;
        int bitsAvailable[32];
        for(int j = 0; j < 32; j++)
        {
            bitsAvailable[j] = 0;
        }

        for (int n = 0; n < numCandies; n++)
        {
            int value = values.at(n);
            int bitInNumber = 0;
            for(int j = 0; j < 32; j++)
            {
                if (value & (1 << j))
                {
                    bitsAvailable[j]++;
                }
            }
        }

        for(int j = 0; j < 32; j++)
        {
            if (bitsAvailable[j] % 2 != 0) { maxEqual = -1; break; }
        }

        if (maxEqual == -1)
        {
            std::cout << "NO" << std::endl;
            continue;
        }

        maxEqual = 0;
        for (int n = 0; n < numCandies - 1; n++)
        {
            maxEqual += values.at(n);
        }

        std::cout << maxEqual << std::endl;
    }
}
