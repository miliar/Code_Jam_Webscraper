// Mike Terranova
// Compiled with MS Visual Studio 2010
// April 13, 2012

#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>

using namespace std;
using namespace std::placeholders;

typedef __int64 int64;

map<char, char> charMap;

int main()
{
    ofstream outfile("out.txt");

    int numCases;
    cin >> numCases;

    for (int i = 1; i <= numCases; i++)
    {
        int numPeople;
        cin >> numPeople;

        int numSurprises;
        cin >> numSurprises;

        int bestAtLeast;
        cin >> bestAtLeast;

        int minWithoutASurprise = 3 * bestAtLeast - 2;
        int minWithASurprise = 3 * bestAtLeast - 4;

        int total = 0;

        for (int j = 0; j < numPeople; j++)
        {
            int point;
            cin >> point;

            // can you do it without a surprise?
            if (point >= minWithoutASurprise)
            {
                total++;
                continue;
            }

            // can you do it with a surprise?
            if (point > 0 && point >= minWithASurprise && numSurprises > 0)
            {
                total++;
                numSurprises--;
            }
        }

        outfile << "Case #" << i << ": " << total << endl;
    }

    outfile.close();
    return 0;
}

