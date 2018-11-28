////////////////////////////////////////////////////////////////////////////////
// ProblemB.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//        Solves Google Code Jam 2012 Qualifying Round Problem B
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//  Created:  04/14/2012 17:05:47
////////////////////////////////////////////////////////////////////////////////
#include <iostream>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, const char *argv[])
{
    int T; cin >> T;
    for (int test = 1; test <= T; ++test)  {
        int N, S, p;
        cin >> N >> S >> p;
        int goodEnough = 0;
        for (int g = 0; g < N; ++g) {
            int t; cin >> t;
            int t_mod3 = t % 3;
            int base_score = (t / 3) + (min(t_mod3, 1));
            // Handle best score 'upgrades' using up the surprising ratings
            // whenever it can help push a googler up to p.
            // Note: surprising scores can only happen if the total >= 2.
            if ((S > 0) && (t >= 2) && ((t_mod3 == 0) || (t_mod3 == 2))) {
                if (base_score + 1 == p) {
                    ++goodEnough;
                    --S;
                }
            }

            // Handle googlers whose un-upgraded best score is already good
            // enough.
            if (base_score >= p)
                ++goodEnough;
        }

        cout << "Case #" << test << ": " << goodEnough << endl;
    }
    return 0;
}
