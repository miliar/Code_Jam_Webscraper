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
        int K;
        string S;
        cin >> K >> S;

        vector<int> perm(K);
        for (int i = 0; i < K; ++i) perm[i] = i;

        int result = INT_MAX;

        do {
            string tmp(S);
            for (int i = 0; i < S.size(); i += K) {
                for (int k = 0; k < K; ++k) {
                    tmp[i+k] = S[i+perm[k]];
                }
            }
            tmp.push_back('?');

            int size = 0;
            int c = tmp[0];

            for (int i = 0; i < tmp.size(); ++i) {
                if (tmp[i] != c) {
                    c = tmp[i];
                    ++size;
                }
            }

            result = min(result, size);
        } while (next_permutation(perm.begin(), perm.end()));

        printf("Case #%d: %d\n", Case, result);
    }

    return 0;
}

