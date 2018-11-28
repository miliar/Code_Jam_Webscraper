////////////////////////////////////////////////////////////////////////////////
// ProblemC.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Implements the <+PROBLEM_NAME+> problem
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  05/22/2011 04:56:11
//  Revision History:
//      05/22/2011  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;
typedef unsigned long long int uli;

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
        uli numPlayers, lowBound, upperBound;
        cin >> numPlayers >> lowBound >> upperBound;
        uli *freqs = new uli[numPlayers];
        for (int p = 0; p < numPlayers; ++p)
            cin >> freqs[p];

        uli f;
        for (f = lowBound; f <= upperBound; ++f)    {
            bool bad = false;
            for (int p = 0; !bad && (p < numPlayers); ++p)
                bad |= (freqs[p] % f) && (f % freqs[p]);
            if (!bad)
                break;
        }

        cout << "Case #" << t << ": ";
        if (f <= upperBound)
            cout << f << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
