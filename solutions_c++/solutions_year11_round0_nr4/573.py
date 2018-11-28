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

/*
double getCycleE(int length);

double getSmallerCyclesE(int length) {
    if (!length) {
        return 0;
    }
    double E = 0;
    for (int i = 1; i <= length; ++i) {
        E += (1.0 / length) * (getCycleE(i) + getSmallerCyclesE(length - i));
    }
    return E;
}

double getCycleE(int length) {
    if (length == 1) {
        return 0;
    } else {
        double X = 1;
        for (int i = 1; i < length; ++i) {
            X += (1.0 / length) * (getCycleE(i) + getSmallerCyclesE(length - i));
        }
        return X / (1 - 1.0 / length);
    }
}
*/

double getCycleE(int length) {
    if (length == 1) {
        return 0;
    } else {
        return length;
    }
}


int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int numTests;
    std::cin >> numTests;
    for (int testIdx = 1; testIdx <= numTests; ++testIdx) {
        int n;
        std::cin >> n;

        std::vector<int> pi(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> pi[i];
            --pi[i];
        }
        
        double E = 0;
        std::vector<bool> marked(n);
        for (int i = 0; i < n; ++i) {
            if (!marked[i]) {
                int cycleLength = 0;
                for (int j = i; !marked[j]; j = pi[j]) {
                    marked[j] = true;
                    ++cycleLength;
                }
                E += getCycleE(cycleLength);
            }
        }

        std::cout << "Case #" << testIdx << ": " << E << std::endl;
    }

    return 0;
}