#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>

int main()
{
    int numCases;
    std::cin >> numCases;

    for (int i = 0; i < numCases; i++)
    {
        std::cout << "Case #" << (i + 1) << ": ";

        int possible = 0;
        int definite = 0;

        int numGooglers, numSurprising, p;
        int scores[100];

        std::cin >> numGooglers >> numSurprising >> p;
        for (int n = 0; n < numGooglers; n++)
        {
            std::cin >> scores[n];

            if (scores[n] < p)
            {
                continue;
            }

            if (scores[n] >= (p*3) - 2)
            {
                definite++;
            } else if ((((scores[n] - p) / 2) >= (p-2) && (p-2) >= 0) ||
                       (((scores[n] - p) / 2) >= (p-1) && (p-1) >= 0) ||
                       (((scores[n] - p) / 2) >= (p) && (p) >= 0))
            {
                possible++;
            }
        }

        if (possible > numSurprising)
        {
            possible = numSurprising;
        }

        std::cout << (definite + possible);

        std::cout << std::endl;
    }
}
