////////////////////////////////////////////////////////////////////////////////
// ProblemB.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Implements the second problem
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  05/22/2011 04:55:39
//  Revision History:
//      05/22/2011  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cassert>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long int uli;
// (distance, count)
typedef pair<uli, uint> SegmentPair;

// Comparse
struct SegmentDescComparator
{
    bool operator()(const SegmentPair &p1, const SegmentPair &p2) const
    {
        if (p1.first > p2.first) // want descending
            return true;
        return false;
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
    for (int test = 1; test <= numTests; ++test)  {
        uli t;
        uint C, N, L;
        cin >> L >> t >> N >> C;

        assert((t & 1) == 0);
        assert(C <= N);

        uint a[C];
        uli aPeriodDist = 0;
        for (unsigned int i = 0; i < C; ++i) {
            cin >> a[i];
            aPeriodDist += a[i];
            assert(a[i] <= 1e4);
        }

        // We will use all boosts for the longest time possible starting at
        // boostTime
        uli boostAvailabilityDist = t * .5;

        uint fullPeriods = N / C;
        uint additionalLegs = N % C;

        uli fullDist = fullPeriods * aPeriodDist;
        for (unsigned int i = 0; i < additionalLegs; ++i)
            fullDist += a[i];

        uli fullTime = fullDist * 2;
        if (boostAvailabilityDist < fullDist)  {
            // We should use at least one boost! Apply the boosts for the
            // longest possbile times

            // In which period do our boosts become available?
            uli boostAvailabilityPeriod = boostAvailabilityDist / aPeriodDist;
            // How many full periods are left after this one?
            int remainingPeriods = fullPeriods - boostAvailabilityPeriod - 1;
            // How much distance was covered within this period before the boost
            // was made available?
            uint distWithinPeriod = boostAvailabilityDist % aPeriodDist;
            // Which how far through which segment is this?
            uint distWithinSegment = distWithinPeriod;
            unsigned int seg;
            for (seg = 0; seg < C; ++seg) {
                if (distWithinSegment >= a[seg])
                    distWithinSegment -= a[seg];
                else
                    break;
            }
            assert(distWithinSegment >= 0);

            vector<SegmentPair> remainingSegments;
            uint segCounts[C];
            memset(segCounts, 0, sizeof(uint) * C);

            if (seg < C)    {
                // There's only one of these partial segments
                remainingSegments.push_back(SegmentPair(a[seg] -
                                            distWithinSegment, 1));
                // The remaining segments in this period are boost-able
                for (unsigned int i = seg + 1; i < C; ++i)
                    ++segCounts[i];
            }
            if (remainingPeriods >= 0)   {
                for (unsigned int i = 0; i < C; ++i)
                    segCounts[i] += remainingPeriods;
                for (unsigned int i = 0; i < additionalLegs; ++i)
                    ++segCounts[i];
            }
            else    {
                // We've already computed the remaining segment distance within
                // the boost-start period
            }

            // Figure out what distances we get boosts on (we get half the time
            // back...)
            for (unsigned int i = 0; i < C; ++i) {
                remainingSegments.push_back(SegmentPair(a[i], segCounts[i]));
            }
            sort(remainingSegments.begin(), remainingSegments.end(),
                    SegmentDescComparator());
            uli boostedDistance = 0;
            for (unsigned int i = 0; i < remainingSegments.size(); ++i)  {
                if (L <= 0)
                    break;

                SegmentPair boostSegment = remainingSegments[i];
                // How many boosts do we spend on this segment type?
                int numBoostedSegs = min(L, boostSegment.second);
                L -= numBoostedSegs;
                boostedDistance += boostSegment.first * numBoostedSegs;
            }

            // We travelled the boosted distance twice as fast, so instead of
            // taking the 2 * boostedDistance we counted first, it only took
            // boostedDistance
            fullTime -= boostedDistance;
        }

        cout << "Case #" << test << ": " << fullTime << endl;
    }

    return 0;
} 
