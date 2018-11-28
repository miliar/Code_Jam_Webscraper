// Mike Terranova
// Compiled with MS Visual Studio 2010
// May 6, 2011

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

// ttmath Library: Available under BSD license: ttmath.org
/* #include <ttmath/ttmath.h> 
typedef ttmath::Int<TTMATH_BITS(128)> int128;
typedef ttmath::Int<TTMATH_BITS(256)> int256;
typedef ttmath::Int<TTMATH_BITS(512)> int512;
typedef ttmath::Int<TTMATH_BITS(1024)> int1024;
typedef ttmath::Int<TTMATH_BITS(2048)> int2048;
typedef ttmath::Int<TTMATH_BITS(4096)> int4096;
typedef ttmath::Int<TTMATH_BITS(8192)> int8192;

typedef ttmath::Big<TTMATH_BITS(32), TTMATH_BITS(96)> quadruple;
typedef ttmath::Big<TTMATH_BITS(64), TTMATH_BITS(192)> octuple;
typedef ttmath::Big<TTMATH_BITS(64), TTMATH_BITS(512)> kilofloat;
typedef ttmath::Big<TTMATH_BITS(128), TTMATH_BITS(1024)> megafloat;
typedef ttmath::Big<TTMATH_BITS(256), TTMATH_BITS(2048)> gigafloat; */

using namespace std;

int main()
{
    ofstream outfile("out.txt");

    int numCases;
    cin >> numCases;

    for (int i = 1; i <= numCases; i++)
    {
        int numCandies;
        cin >> numCandies;

        multiset<int> candies;
        __int64 total = 0;
        __int64 xorTotal = 0;
        for (int j = 0; j < numCandies; j++)
        {
            int newCandy;
            cin >> newCandy;
            xorTotal ^= newCandy;
            total += newCandy;
            candies.insert(newCandy);
        }

        // For all x, x ^ x == 0.
        // There must be two groups that XOR to 0.
        if (xorTotal != 0)
            outfile << "Case #" << i << ": NO" << endl;
        else
        {
            // Otherwise
            // !!!!!!!!!!!!!!!!!!!
            // What!!!!
            // How did I not see this!!!!!!
            // If the total XOR == 0
            // Then let the smallest number = a
            // (a ^ (total - a)) == 0 !!!!!!!!

            int minimum = *(candies.begin());

            outfile << "Case #" << i << ": " << total - minimum << endl;
        }
    }

    outfile.close();
    return 0;
}

