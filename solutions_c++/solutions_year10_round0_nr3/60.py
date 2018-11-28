#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int testCasesCount;
    std::cin >> testCasesCount;
    for (int testCaseIndex = 1; testCaseIndex <= testCasesCount; ++testCaseIndex) {
        long long numberOfRuns;
        long long numberOfSeats;
        int numberOfGroups;
        std::vector<long long> groups;

        std::cin >> numberOfRuns >> numberOfSeats;
        std::cin >> numberOfGroups;
        for (int groupIndex = 0; groupIndex < numberOfGroups; ++groupIndex) {
            int groupSize;
            std::cin >> groupSize;
            groups.push_back(groupSize);
        }

        for (int groupIndex = 0; groupIndex < numberOfGroups; ++groupIndex) {
            groups.push_back(groups[groupIndex]);
        }

        std::vector<int> nextWaitingGroup(numberOfGroups);
        std::vector<long long> costOfRun(numberOfGroups);
        for (int firstGroupIndex = 0; firstGroupIndex < numberOfGroups; ++firstGroupIndex) {
            long long numberOfOccupiedSeats = groups[firstGroupIndex];
            int lastGroupIndex = firstGroupIndex;
            while (lastGroupIndex - firstGroupIndex + 1 < numberOfGroups && numberOfOccupiedSeats + groups[lastGroupIndex + 1] <= numberOfSeats) {
                numberOfOccupiedSeats += groups[++lastGroupIndex];
            }

            nextWaitingGroup[firstGroupIndex] = (lastGroupIndex + 1) % numberOfGroups;
            costOfRun[firstGroupIndex] = numberOfOccupiedSeats;
        }

        
        int firstGroupIndex = 0;
        std::vector<int> time(numberOfGroups, false);
        std::vector<int> cycle;
        int timer = 0;
        do {
            cycle.push_back(firstGroupIndex);
            time[firstGroupIndex] = ++timer;;
            firstGroupIndex = nextWaitingGroup[firstGroupIndex];
        } while (time[firstGroupIndex] == 0);

        int predCycleLength = time[firstGroupIndex] - 1;
        int cycleLength = cycle.size() - predCycleLength;

        std::vector<long long> prefixCosts;
        for (int cycleIndex = 0; cycleIndex < cycle.size(); ++cycleIndex) {
            prefixCosts.push_back(costOfRun[cycle[cycleIndex]]);
            if (cycleIndex > 0) {
                prefixCosts[cycleIndex] += prefixCosts[cycleIndex - 1];
            }
        }

        long long predCycleCost = predCycleLength > 0 ? prefixCosts[predCycleLength - 1] : 0;

        long long totalGain = 0;
        if (predCycleLength > 0) {
            totalGain += prefixCosts[std::min((int)numberOfRuns, predCycleLength) - 1];
            numberOfRuns -= std::min((int)numberOfRuns, predCycleLength);
        }

        long long numberOfFullCycles = numberOfRuns / cycleLength;
        long long numberOfRemaindedRuns = numberOfRuns % cycleLength;

        totalGain += numberOfFullCycles * (prefixCosts.back() - predCycleCost);
        if (numberOfRemaindedRuns > 0) {
            totalGain += prefixCosts[predCycleLength + numberOfRemaindedRuns - 1] - predCycleCost;
        }

        std::cout << "Case #" << testCaseIndex << ": " << totalGain << std::endl;

    }

    return 0;
}
