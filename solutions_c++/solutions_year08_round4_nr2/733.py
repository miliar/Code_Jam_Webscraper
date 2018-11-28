#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <cmath>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <cfloat>

using namespace std;

typedef long long int64_t;

template <typename T, int N>
inline size_t length_of(T(&)[N]) throw() { return N; }


int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int Case = 1; Case <= T; ++Case) {
        int N, M, A;
        cin >> N >> M >> A;

        int x1 = 0, y1 = 0, x2, y2, x3, y3;

        for (x2 = 0; x2 <= N; ++x2)
        for (y2 = 0; y2 <= M; ++y2)
        for (x3 = 0; x3 <= N; ++x3)
        for (y3 = y2; y3 <= M; ++y3)
        {
            int quad = max(x2, x3) * y3;
            if (quad < A) continue;

            int sum = x2 * y2 + abs(x2 - x3) * (y3 - y2) + x3 * y3;

            if (x3 > x2) {
                if (x2*y3 > x3*y2) {
                    sum += (x3 - x2) * y2 * 2;
                }
                else {
                    sum += (y3 - y2) * x2 * 2;
                }
            }

            if (quad * 2 - sum == A) goto print;
        }

        printf("Case #%d: IMPOSSIBLE\n", Case);
        continue;

print:
        printf("Case #%d: %d %d %d %d %d %d\n", Case, x1, y1, x2, y2, x3, y3);

    }

    return 0;
}

