#include <iostream>
#include <vector>
#include <algorithm>

#include <math.h>

int main()
{
    int numCases;

    std::cin >> numCases;

    for (int i = 0; i < numCases; i++)
    {
        std::cout << "Case #" << (i+1) << ": ";

        std::vector<int> values;
        std::vector<int> sorted;

        int numValues;
        std::cin >> numValues;

        for (int n = 0; n < numValues; n++)
        {
            int value;
            std::cin >> value;

            values.push_back(value);
            sorted.push_back(value);
        }

        std::sort(sorted.begin(), sorted.end());

        int numPounds = 0;
        double numSorted = 0;

        for (int n = 0; n < numValues; n++)
        {
            if (values.at(n) == sorted.at(n))
            {
                numSorted += 1.0;
            }
        }

        while (fabs(numValues - numSorted) > 0.000001)
        {
            numPounds++;

            double unsorted = numValues - numSorted;
            double unsortedGamma = tgamma(unsorted) * unsorted;
            double percSorted = (unsortedGamma/(unsorted*unsortedGamma));

            numSorted += unsorted * percSorted;
        }

        std::cout << numPounds << ".000000" << std::endl;
    }
}
