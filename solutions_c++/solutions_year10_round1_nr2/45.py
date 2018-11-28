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

int delete_cost, insert_cost, M, N;

int memo[300][150];
int a[150];

int doit(int prev, int pos)
{
    if(pos == N) return 0;

    int& ret = memo[prev][pos];
    if(ret != -1) return ret;

    ret = delete_cost + doit(prev, pos + 1);

    if(abs(a[pos] - prev) <= M)
        ret = min(ret, doit(a[pos], pos + 1));

    for(int i = 0; i <= 255; i++)
        if(abs(i - prev) <= M) {
            ret = min(ret, insert_cost + doit(i, pos));
            ret = min(ret, abs(i - a[pos]) + doit(i, pos+1));
        }

    return ret;
}

int main() {
    int t;
    cin >> t;

    for(int z = 0; z < t; z++) {
        cin >> delete_cost >> insert_cost >> M >> N;
        memset(memo, -1, sizeof memo);

        for(int i = 0; i < N; i++)
            cin >> a[i];

        cout << "Case #" << z+1 << ": ";
        int ret = 999999999;
        for(int i = 0; i <= 255; i++)
            ret = min(ret, doit(i, 0));
        cout << ret << endl;
    }
}
