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

typedef std::pair<int, int> TPos;
typedef std::set< std::pair<int, int> > TState;

TPos GetLeft(TPos pos) {
    return TPos(pos.first - 1, pos.second);
}

TPos GetUp(TPos pos) {
    return TPos(pos.first, pos.second - 1);
}

TPos GetRight(TPos pos) {
    return TPos(pos.first + 1, pos.second);
}

TPos GetDown(TPos pos) {
    return TPos(pos.first, pos.second + 1);
}

bool Has(TState& state, TPos pos) {
    return state.find(pos) != state.end();
}

void DoStep(TState& cur, TState& next) {
    for (TState::const_iterator it = cur.begin(); it != cur.end(); ++it) {
        TPos pos = *it;
        if (Has(cur, GetLeft(pos)) || Has(cur, GetUp(pos))) {
            next.insert(pos);
        }
        if (Has(cur, GetLeft(GetDown(pos)))) {
            next.insert(GetDown(pos));
        }
        if (Has(cur, GetUp(GetRight(pos)))) {
            next.insert(GetRight(pos));
        }
    }
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int testCasesCount;
    std::cin >> testCasesCount;
    for (int testCaseIndex = 1; testCaseIndex <= testCasesCount; ++testCaseIndex) {

        TState cur, next;
        int rectsCount;
        std::cin >> rectsCount;
        for (int k = 0; k < rectsCount; ++k) {
            int iFrom, iTo, jFrom, jTo;
            std::cin >> iFrom >> jFrom >> iTo >> jTo;
            for (int i = iFrom; i <= iTo; ++i) {
                for (int j = jFrom; j <= jTo; ++j) {
                    cur.insert(TPos(i, j));
                }
            }
        }

        int steps = 0;
        while (!cur.empty()) {
            next.clear();
            DoStep(cur, next);
            cur = next;
            ++steps;
        }

        std::cerr << "complete\n";

        std::cout << "Case #" << testCaseIndex << ": " << steps << std::endl;

    }

    return 0;
}
