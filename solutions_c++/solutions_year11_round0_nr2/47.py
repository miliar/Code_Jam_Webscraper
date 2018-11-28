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
        map<char, map<char, char> > combos;
        int numCombos;
        cin >> numCombos;
        
        for (int combo = 0; combo < numCombos; combo++)
        {
            char combo1, combo2, combo3;
            cin >> combo1 >> combo2 >> combo3;

            combos[combo1][combo2] = combo3;
            combos[combo2][combo1] = combo3;
        }

        map<char, set<char> > destroyers;
        int numDestroyers;
        cin >> numDestroyers;

        for (int destroyer = 0; destroyer < numDestroyers; destroyer++)
        {
            char dest1, dest2;
            cin >> dest1 >> dest2;

            destroyers[dest1].insert(dest2);
            destroyers[dest2].insert(dest1);
        }

        int numChars;
        cin >> numChars;

        vector<char> finalString;
        for (int a = 0; a < numChars; a++)
        {
            char c;
            cin >> c;

            if (!finalString.empty())
            {
                char d = finalString.back();
                if (combos[c].find(d) != combos[c].end())
                {
                    finalString.back() = combos[c][d];
                }
                else
                {
                    bool cleared = false;
                    for (int x = 0; x < finalString.size(); x++)
                    {
                        if (destroyers[c].find(finalString[x]) != destroyers[c].end())
                        {
                            finalString.clear();
                            cleared = true;
                            break;
                        }
                    }

                    if (!cleared)
                    {
                        finalString.push_back(c);
                    }
                }
            }
            else
                finalString.push_back(c);
        }

        
        outfile << "Case #" << i << ": [";

        int sizer = finalString.size() - 1;
        for (int z = 0; z <= sizer; z++)
        {
            outfile << finalString[z];
            if (z < sizer)
                outfile << ", ";
        }
        
        outfile << ']' << endl;
    }

    outfile.close();
    return 0;
}

