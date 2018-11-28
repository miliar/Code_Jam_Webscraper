////////////////////////////////////////////////////////////////////////////////
// ProblemC.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Implements the "Candy Splitting" problem (Problem C)
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  05/07/2011 18:34:19
//  Revision History:
//      05/07/2011  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <climits>

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
    for (int t = 1; t <= numTests; ++t) {
        int numCandies;
        cin >> numCandies;

        unsigned long int candySum = 0, candyHash = 0;
        unsigned long int minCandy = UINT_MAX;
        for (int candy = 0; candy < numCandies; ++candy)    {
            unsigned long int value;
            cin >> value;
            if (value < minCandy)
                minCandy = value;

            candyHash ^= value;
            candySum  += value;
        }

        if (candyHash == 0)
            cout << "Case #" << t << ": " << candySum - minCandy << endl;
        else
            cout << "Case #" << t << ": NO" << endl;
    }
    unsigned long int hash = 0;
    return 0;
}
