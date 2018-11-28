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
    std::ifstream input("test.in");
    std::ofstream output("test.out");

    int numTests;
    input >> numTests;
    for (int testIdx = 1; testIdx <= numTests; ++testIdx) {
        int n;
        input >> n;

        int xorsum = 0;
        std::vector<int> seq(n);
        for (int i = 0; i < n; ++i) {
            input >> seq[i];
            xorsum ^= seq[i];
        }

        std::sort(seq.begin(), seq.end(), std::greater<int>());
        int maxScore = 0;
        for (int i = 0; i < n-1; ++i) {
            maxScore += seq[i];
        }

        output << "Case #" << testIdx << ": ";
        if (xorsum == 0) {
            output << maxScore;
        } else {
            output << "NO";
        }
        output << std::endl;
    }

    input.close();
    output.close();

    return 0;
}