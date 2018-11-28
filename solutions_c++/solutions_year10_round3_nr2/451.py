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

const int MAX = 2000;
int mark[MAX][MAX];
int answers[MAX][MAX];
int testCaseIndex;
int l, p, c;

int Get(const int from, const int to) {
    if (from * c >= to) {
        return 0;
    }
    if (mark[from][to] == testCaseIndex) {
        return answers[from][to];
    }
    int a = from * c;
    int b = to / c;
    if (to % c > 0) {
        ++b;
    }
    if (a >= b) {
        mark[from][to] = testCaseIndex;
        answers[from][to] = 1;
        return 1;
    }
    answers[from][to] = 1e9;
    for (int t = a; t <= b; ++t) {
        answers[from][to] = std::min(answers[from][to], 1 + std::max(Get(from, t), Get(t, to)));
    }
    mark[from][to] = testCaseIndex;
    return answers[from][to];
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int testCasesCount;
    std::cin >> testCasesCount;
    for (testCaseIndex = 1; testCaseIndex <= testCasesCount; ++testCaseIndex) {
        std::cin >> l >> p >> c;

        std::cout << "Case #" << testCaseIndex << ": " << Get(l, p) << std::endl;
        std::cerr << testCaseIndex << std::endl;

    }

    return 0;
}
