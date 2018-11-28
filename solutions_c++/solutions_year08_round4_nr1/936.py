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


int eval(int node, int size, int index)
{
    if (index >= size/2) return (node >> index) & 1;

    if (node & (1<<index)) {
        return eval(node, size, index*2 + 1) & eval(node, size, index*2 + 2);
    }
    else {
        return eval(node, size, index*2 + 1) | eval(node, size, index*2 + 2);
    }
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int Case = 1; Case <= T; ++Case) {
        int M, V;
        cin >> M >> V;

        int interior = M/2;

        int node = 0;
        int changeable = 0;

        for (int i = 0; i < interior; ++i) {
            int a, b;
            cin >> a >> b;
            node |= a << i;
            changeable |= b << i;
        }

        for (int i = 0; i < M - interior; ++i) {
            int a;
            cin >> a;
            node |= a << (i+interior);
        }

        int result = INT_MAX;

        for (int mask = 0; mask < (1<<interior); ++mask) {
            if ((mask | changeable) > changeable) continue;
            if (eval(node ^ mask, M, 0) == V) {
                result = min(result, __builtin_popcount(mask));
            }
        }

        printf("Case #%d: ", Case);

        if (result == INT_MAX) {
            printf("IMPOSSIBLE\n");
        }
        else {
            printf("%d\n", result);
        }
    }

    return 0;
}

