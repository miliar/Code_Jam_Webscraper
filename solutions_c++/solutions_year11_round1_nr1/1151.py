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

using namespace std::placeholders;

// ttmath Library: Available under BSD license: ttmath.org
#include <ttmath/ttmath.h> 
typedef ttmath::Int<TTMATH_BITS(128)> int128;
/* typedef ttmath::Int<TTMATH_BITS(256)> int256;
typedef ttmath::Int<TTMATH_BITS(512)> int512;
typedef ttmath::Int<TTMATH_BITS(1024)> int1024;
typedef ttmath::Int<TTMATH_BITS(2048)> int2048;
typedef ttmath::Int<TTMATH_BITS(4096)> int4096;
typedef ttmath::Int<TTMATH_BITS(8192)> int8192; */

// typedef ttmath::Big<TTMATH_BITS(32), TTMATH_BITS(96)> quadruple;
/* typedef ttmath::Big<TTMATH_BITS(64), TTMATH_BITS(192)> octuple;
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
        int128 maxGamesToday;
        int percentToday;
        int percentAll;

        cin >> maxGamesToday >> percentToday >> percentAll;

        if ((percentAll == 0 && percentToday != 0) ||
            (percentAll == 100 && percentToday != 100))
        {
            outfile << "Case #" << i << ": " << "Broken" << endl;
            continue;
        }

        // Otherwise, as long as there is a number x <= maxGamesToday
        // Where (x * percentToday) % 100 == 0
        // If x == 100: Then it's always possible!

        if (maxGamesToday >= int128(100))
        {
            outfile << "Case #" << i << ": " << "Possible" << endl;
            continue;
        }

        bool broken = true;
        for (int128 x = 1; x <= maxGamesToday; x++)
        {
            if (((x * percentToday) % int128(100)) == int128(0))
            {
                broken = false;
                break;
            }
        }

        outfile << "Case #" << i << ": " << (broken ? "Broken" : "Possible") << endl;
    }

    outfile.close();
    return 0;
}

