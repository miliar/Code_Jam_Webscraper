//      Space Emergency.cpp
//
//      Copyright 2011 Tóth Bence <totesz@totesz-desktop>
//
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

unsigned long calculateTravelLength(const unsigned long speedBoosterCount,
                               const unsigned long speedBoosterBuildTime,
                               const unsigned long destinationStar,
                               const vector<unsigned long> & starDistance,
                               vector<unsigned long> & travelTime) {
    vector<unsigned long> acceleratedTravelTime;

    for (unsigned long i = 0, spentTime = 0; i < destinationStar; ++i) {
        unsigned long possibleTravelTime = 0;

        if (spentTime >= speedBoosterBuildTime) {
            possibleTravelTime = starDistance[i];
            spentTime += possibleTravelTime;
        } else if (spentTime + travelTime[i] >= speedBoosterBuildTime) {
            unsigned long halfSpeedDistance = (speedBoosterBuildTime - spentTime)/2;
            possibleTravelTime = starDistance[i] + halfSpeedDistance;
            spentTime += possibleTravelTime;
        } else {
            possibleTravelTime = travelTime[i];
            spentTime += possibleTravelTime;
        }
        acceleratedTravelTime.push_back(possibleTravelTime);
    }

    vector<unsigned long> speedGain;
    for (unsigned long i = 0; i < destinationStar; ++i) {
        speedGain.push_back(travelTime[i]-acceleratedTravelTime[i]);
    }

    for (unsigned long sbc = speedBoosterCount; sbc > 0; --sbc) {
        unsigned long accelerationPos = destinationStar;
        unsigned long maxGain = 0;
        for (unsigned long i = destinationStar; i > 0; --i) {
            if (speedGain[i-1] > maxGain) {
                maxGain = speedGain[i-1];
                accelerationPos = i-1;
            }
        }
        if (maxGain > 0) {
            travelTime[accelerationPos] = acceleratedTravelTime[accelerationPos];
            speedGain[accelerationPos] = 0;
        }
    }

    unsigned long firstStarToAccelerate = 0;
    for (unsigned long distance = 0; distance < speedBoosterBuildTime; ++firstStarToAccelerate) {
        distance += travelTime[firstStarToAccelerate];
    }
    for (unsigned long i = destinationStar; i > 0; --i) {

    }
    return accumulate(travelTime.begin(), travelTime.end(), 0);
}

int main(int argc, char **argv) {
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);

    unsigned long testCaseCount;
    input >> testCaseCount;

    for (unsigned long testCase = 0; testCase < testCaseCount; ++testCase) {
        output << "Case #" << testCase+1 << ": ";
        cout   << "Case #" << testCase+1 << ": ";

        unsigned long speedBoosterCount;
        input >> speedBoosterCount;
        unsigned long speedBoosterBuildTime;
        input >> speedBoosterBuildTime;
        unsigned long destinationStar;
        input >> destinationStar;

        unsigned long routeParam;
        input >> routeParam;

        vector<unsigned long> starDistance(destinationStar);
        vector<unsigned long> travelTime(destinationStar);

        for (unsigned long i = 0; i < routeParam; ++i) {
            unsigned long distance;
            input >> distance;
            for (unsigned long j = i; j < destinationStar; j += routeParam) {
                starDistance[j] = distance;
                travelTime[j] = distance * 2;
            }
        }

        unsigned long result = calculateTravelLength(speedBoosterCount, speedBoosterBuildTime, destinationStar, starDistance, travelTime);

        output << result << endl;
        cout   << result << endl;
    }

    input.close();
    output.close();
    return 0;
}
