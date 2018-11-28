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

struct Walkway {
    int start, end, speed;
    Walkway(int s, int e, int r)
        : start(s), end(e), speed(r) { }
    int dist() { return end - start; }
};

struct SortComparator
{
    // Returns true if a goes before b
    bool operator() (Walkway a, Walkway b)
    {
        // ascending order order of speed
        return a.speed < b.speed;
    }
};

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
        int X, S, R, maxRunTime, N;
        cin >> X >> S >> R >> maxRunTime >> N;
        vector<int> B(N), E(N), w(N);
        for (int i = 0; i < N; ++i) {
            cin >> B[i] >> E[i] >> w[i];
        }

        double walkwayDist = 0;
        vector<Walkway> walkways;
        for (int i = 0; i < N; ++i) {
            walkwayDist += E[i] - B[i];
            walkways.push_back(Walkway(B[i], E[i], w[i]));
        }

        // Always prefer to run on the regular corridor
        // (this is provably superior)
        double time = 0;
        double regular = X - walkwayDist;
        if (regular > 0)  {
            if (time < maxRunTime)  {
                double bestEndTime = time + regular / R;
                if (bestEndTime > maxRunTime)   {
                    // had to stop running at maxRunTime
                    double runTime = maxRunTime - time;
                    double runDist = R * runTime;
                    double walkTime = (regular - runDist) / S;
                    time += runTime + walkTime;
                }
                else    {
                    time = bestEndTime;
                }
            }
            else    {
                time += regular / S;
            }
        }

        // Similarly, always prefer to run on the slower walkways
        sort(walkways.begin(), walkways.end(), SortComparator());

        for (int i = 0; i < N; ++i) {
            Walkway walkway = walkways[i];
            double runRate = R + walkway.speed;
            double walkRate = S + walkway.speed;
            double dist = walkway.dist();
            if (time < maxRunTime)   {
                double bestEndTime = time + dist / runRate;
                if (bestEndTime > maxRunTime)   {
                    // had to stop running at maxRunTime
                    double runTime = maxRunTime - time;
                    double runDist = runRate * runTime;
                    double walkTime = (dist - runDist) / walkRate;
                    assert(walkTime > 0 && runDist > 0);
                    time += runTime + walkTime;
                }
                else    {
                    time = bestEndTime;
                }
            }
            else    {
                time += dist / walkRate;
            }
        }


        printf("Case #%i: %0.12lf\n", t, time);
    }
    
    return 0;
}
