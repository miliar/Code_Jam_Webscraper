// Mike Terranova
// Compiled with MS Visual Studio 2010
// May 6, 2011

#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <map>
#include <vector>
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
        int numNumbers;
        cin >> numNumbers;

        int numInRightPlaceAlready = 0;
        for (int j = 1; j <= numNumbers; j++)
        {
            int curNum;
            cin >> curNum;
            if (curNum == j)
                numInRightPlaceAlready++;
        }

        double x = numNumbers - numInRightPlaceAlready;

        // I spent about an hour trying to do the math on this
        // because I couldn't possibly believe it.
        outfile << fixed << setprecision(6) << "Case #" << i << ": " << x << endl;
    }

    outfile.close(); 
    return 0;
}
