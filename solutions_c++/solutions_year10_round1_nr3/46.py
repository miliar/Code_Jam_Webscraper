#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef double TYPE;
const TYPE EPS = 1e-9, INF = 1e9;

inline int sgn(TYPE a) { return a > EPS ? 1 : (a < -EPS ? -1 : 0); }
inline int cmp(TYPE a, TYPE b) { return sgn(a - b); }

long long f(long long i, long long j) {
    return i*i - j*j - i*j;
}

int main() {
    int t;
    cin >> t;
    for(int z = 0; z < t; z++) {
        long long j = 0, ret = 0;
        long long A1, A2, B1, B2;
        cin >> A1 >> A2 >> B1 >> B2;

        for(long long i = max(1LL, A1); i <= A2; i++) {
            while(f(i,j) > 0)
                j++;
            ret += max(0LL, min(B2, j-1) - B1 + 1);
        }

        j = 0;
        for(long long i = max(1LL, B1); i <= B2; i++) {
            while(f(i,j) > 0)
                j++;
            ret += max(0LL, min(A2, j-1) - A1 + 1);
        }

        cout << "Case #" << z + 1 << ": " << ret << endl;
    }
}
