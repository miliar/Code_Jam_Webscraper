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
        int n, k, b, t;
        std::cin >> n >> k >> b >> t;
        std::vector<int> sx(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> sx[i];
        }
        std::vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> v[i];
        }
        
        int badCount = 0;
        int arriveCount = 0;
        int swapCount = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (sx[i] + t * v[i] >= b) {
                ++arriveCount;
                swapCount += badCount;
                if (arriveCount == k) {
                    break;
                }
            } else {
                ++badCount;
            }
        }

        std::cout << "Case #" << testCaseIndex << ": ";
        if (arriveCount == k) {
            std::cout << swapCount;
        } else {
            std::cout << "IMPOSSIBLE";
        }
        std::cout << std::endl;
    }

    return 0;
}
