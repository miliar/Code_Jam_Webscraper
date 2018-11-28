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
        int n;
        std::cin >> n;
        std::vector< std::pair<int, int> > wires(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> wires[i].first >> wires[i].second;
        }
        std::sort(wires.begin(), wires.end());
        int count = 0;
        for (int i = 1; i < n; ++i) {
            int j = i;
            while (j > 0 && wires[j - 1].second > wires[j].second) {
                std::swap(wires[j - 1], wires[j]);
                --j;
                ++count;
            }
        }

        std::cout << "Case #" << testCaseIndex << ": " << count << std::endl;

    }

    return 0;
}
