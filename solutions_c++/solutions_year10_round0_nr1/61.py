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
        int numberOfDevices;
        int numberOfSnaps;
        std::cin >> numberOfDevices >> numberOfSnaps;

        int numberOfPossibleChainStates = 1 << numberOfDevices;
        int chainStateAfterSnaps = numberOfSnaps % numberOfPossibleChainStates;

        bool lightIsOn = chainStateAfterSnaps == numberOfPossibleChainStates - 1;

        std::cout << "Case #" << testCaseIndex << ": " << (lightIsOn ? "ON" : "OFF") << std::endl;
            
    }

    return 0;
}