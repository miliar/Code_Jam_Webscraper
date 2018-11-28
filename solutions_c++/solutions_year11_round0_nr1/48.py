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
        int numPushes;
        cin >> numPushes;

        vector<int> pushes(numPushes);
        queue<int> bluePushes;
        queue<int> orangePushes;
        for (int p = 0; p < numPushes; p++)
        {
            string c;
            cin >> c;
            
            cin >> pushes[p];
            if (c == "O")
            {
                pushes[p] *= -1;
                orangePushes.push(pushes[p]);
            }
            else
                bluePushes.push(pushes[p]);
        }

        int bluePos = 1;
        int orangePos = -1;
        int curPush = 0;
        int t;
        for (t = 0; curPush < numPushes; t++)
        {
            bool bluePushed = false;
            bool orangePushed = false;

            // First, check pushes
            if (bluePos == pushes[curPush])
            {
                bluePushes.pop();
                curPush++;
                bluePushed = true;
            }
            else if (orangePos == pushes[curPush])
            {
                orangePushes.pop();
                curPush++;
                orangePushed = true;
            }

            // Now move
            if (!bluePushed && !bluePushes.empty())
            {
                if (bluePos < bluePushes.front())
                    bluePos++;
                else if (bluePos > bluePushes.front())
                    bluePos--;
            }

            if (!orangePushed && !orangePushes.empty())
            {
                if (orangePos < orangePushes.front())
                    orangePos++;
                else if (orangePos > orangePushes.front())
                    orangePos--;
            }
        }

        outfile << "Case #" << i << ": " << t << endl;
    }

    outfile.close();
    return 0;
}

