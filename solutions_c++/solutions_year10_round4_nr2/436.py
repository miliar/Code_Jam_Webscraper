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

const int MAX_P = 13;

const long long INF = 1000000000000;

int miss[1 << MAX_P];
int cost[1 << MAX_P];
int depth[1 << MAX_P];
int P;
int flag[1 << MAX_P][MAX_P];
long long cache[1 << MAX_P][MAX_P];

int testCaseIndex;

int GetLeft(int match) {
    return (match + 1) * 2 - 1;
}
int GetRight(int match) {
    return GetLeft(match) + 1;
}

int GetFirst(const int round) {
    return (1 << round) - 1;
}

long long GetCost(int match, int prev) {
    if (flag[match][prev] == testCaseIndex) {
        return cache[match][prev];
    }
    if (prev + P - depth[match] < miss[match]) {
        return INF;
    }
    flag[match][prev] = testCaseIndex;
    if (GetLeft(match) >= GetFirst(P)) {
        if (prev >= miss[match]) {
            cache[match][prev] = 0;
        } else {
            cache[match][prev] = cost[match];
        }
        return cache[match][prev];
    } else {
        cache[match][prev] = std::min(GetCost(GetLeft(match), prev) + GetCost(GetRight(match), prev),
                                      GetCost(GetLeft(match), prev + 1) + GetCost(GetRight(match), prev + 1) + cost[match]);
        return cache[match][prev];
    }
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int testCasesCount;
    std::cin >> testCasesCount;
    for (testCaseIndex = 1; testCaseIndex <= testCasesCount; ++testCaseIndex) {

        std::cin >> P;

        for (int i = 0; i < (1 << P); ++i) {
            int cnt;
            std::cin >> cnt;
            miss[GetFirst(P) + i] = P - cnt;
        }
        for (int i = GetFirst(P) - 1; i >= 0; --i) {
            miss[i] = std::max(miss[GetLeft(i)], miss[GetRight(i)]);
        }

        for (int i = P - 1; i >= 0; --i) {
            for (int j = 0; j < (1 << i); ++j) {
                std::cin >> cost[GetFirst(i) + j];
                depth[GetFirst(i) + j] = i;
            }
        }

        std::cout << "Case #" << testCaseIndex << ": " << GetCost(0, 0) << std::endl;

    }

    return 0;
}
