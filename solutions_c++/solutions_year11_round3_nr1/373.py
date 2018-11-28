////////////////////////////////////////////////////////////////////////////////
// ProblemA.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Implements the <+PROBLEM_NAME+> problem
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  05/22/2011 04:55:55
//  Revision History:
//      05/22/2011  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, char *argv[])
{
    int numTests;
    cin >> numTests;
    for (int t = 1; t <= numTests; ++t)  {
        int numRows, numCols;
        cin >> numRows >> numCols;
        char pic[numRows][numCols];
        for (int r = 0; r < numRows; ++r)   {
            for (int c = 0; c < numCols; ++c)   {
                cin >> pic[r][c];
                assert(pic[r][c] == '#' || pic[r][c] == '.');
            }
        }

        // Try to convert the picture in scanline order (we must be able to
        // convert the top left without conflict)
        
        bool fail = false;
        for (int r = 0; !fail && (r < numRows); ++r)   {
            for (int c = 0; !fail && (c < numCols); ++c)   {
                if (pic[r][c] == '#')   {
                    fail = ((r + 1 >= numRows) || (c + 1 >= numCols)) ||
                            (pic[r    ][c + 1] != '#') ||
                            (pic[r + 1][c    ] != '#') || 
                            (pic[r + 1][c + 1] != '#');
                    if (!fail)  {
                        pic[r    ][c    ] = '/';
                        pic[r    ][c + 1] = '\\';
                        pic[r + 1][c    ] = '\\';
                        pic[r + 1][c + 1] = '/';
                    }
                }
            }
        }
        cout << "Case #" << t << ":" << endl;
        if (fail)
            cout << "Impossible" << endl;
        else    {
            for (int r = 0; r < numRows; ++r)   {
                for (int c = 0; c < numCols; ++c)
                    cout << pic[r][c];
                cout << endl;
            }
        }
    }
    
    return 0;
}
