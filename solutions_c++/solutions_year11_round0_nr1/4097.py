////////////////////////////////////////////////////////////////////////////////
// ProblemA.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Implements the Bot Trust Problem
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  05/07/2011 18:10:34
//  Revision History:
//      05/07/2011  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <list>

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
        list<int> ODestinations;
        list<int> BDestinations;
        list<char> events;
        
        int numEvents;
        cin >> numEvents;
        for (int e = 0; e < numEvents; ++e) {
            char robot;
            int button;
            cin >> robot;
            cin >> button;
            switch(robot)   {
                case 'O':
                    ODestinations.push_back(button);
                    break;
                case 'B':
                    BDestinations.push_back(button);
                    break;
                default:
                    cerr << "Bad robot: " << robot << endl;
            }
            events.push_back(robot);
        }

        int OLoc = 1;
        int BLoc = 1;
        int seconds = 0;
        while (!events.empty()) {
            bool Omoved = false, Bmoved = false;
            // Move robots
            if (ODestinations.size() && (OLoc != ODestinations.front()))  {
                OLoc += (OLoc < ODestinations.front()) ? 1 : -1;
                Omoved = true;
            }

            if (BDestinations.size() && (BLoc != BDestinations.front()))  {
                BLoc += (BLoc < BDestinations.front()) ? 1 : -1;
                Bmoved = true;
            }

            switch (events.front()) {
                case 'O':
                    if (!Omoved)    { // If we didn't move, we must be there!
                        ODestinations.pop_front();
                        events.pop_front();
                    }
                    break;
                case 'B':
                    if (!Bmoved)    { // If we didn't move, we must be there!
                        BDestinations.pop_front();
                        events.pop_front();
                    }
                    break;
                default:
                    cerr << "Bad robot: " << events.front() << endl;
            }

            ++seconds;
        }

        cout << "Case #" << t << ": " << seconds << endl;
    }
    

    return 0;
}
