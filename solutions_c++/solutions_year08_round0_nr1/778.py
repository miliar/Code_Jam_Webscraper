
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


const int MAXQ = 1001;
const int MAXS = 101;

int DP[MAXQ][MAXS];


int main(int argc, char* argv[])
{
    int N;
    cin >> N;

    for (int n = 0; n < N; ++n) {
        string s;
        int S, Q;
        vector<string> engines, queries;

        cin >> S;
        getline(cin, s, '\n');

        for (int i = 0; i < S; ++i) {
            getline(cin, s, '\n');
            engines.push_back(s);
        }

        cin >> Q;
        getline(cin, s, '\n');

        for (int i = 0; i < Q; ++i) {
            getline(cin, s, '\n');
            queries.push_back(s);
        }

        if (Q > 0) {
            for (int s = 0; s < S; ++s) {
                DP[0][s] = queries[0] == engines[s] ? INT_MAX : 0;
            }

            for (int q = 1; q < Q; ++q)
            for (int s = 0; s < S; ++s)
            {
                if (queries[q] == engines[s]) {
                    DP[q][s] = INT_MAX;
                }
                else {
                    DP[q][s] = DP[q-1][s];
                    for (int i = 0; i < S; ++i) {
                        if (DP[q-1][i] < INT_MAX) DP[q][s] = min(DP[q][s], DP[q-1][i]+1);
                    }
                }
            }

            printf("Case #%d: %d\n", n+1, *min_element(DP[Q-1], DP[Q-1]+S));
        }
        else {
            printf("Case #%d: %d\n", n+1, 0);
        }
    }

    return 0;
}

