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

int m[2048];
long long memo[2048][20];
long long prices[2048];
int p;

long long doit(int match, int cur) {
    if(m[match] < cur) {
        return 999999999;
    }

    if(match >= (1<<p)-1)
        return 0;

    long long& ret = memo[match][cur];
    if(ret != -1) return ret;
    ret = 999999999;
    ret = min(ret,
              prices[match] + doit(2*match + 1, cur) + doit(2*match + 2, cur));
    ret = min(ret, doit(2*match + 1, cur + 1) + doit(2*match + 2, cur + 1));

    return ret;
}

void calc_minis()
{
    for(int i = (1<<p)-2; i >= 0; i--)
        m[i] = min(m[2*i+1], m[2*i+2]);
}

int main() {
    int t;
    cin >> t;

    for(int z = 0; z < t; z++) {
        memset(memo, -1, sizeof memo);
        cin >> p;

        for(int i = 0; i < (1<<p); i++)
            cin >> m[(1<<p)-1+i];
        calc_minis();

        for(int i = p-1; i >= 0; i--)
            for(int j = 0; j < (1<<i); j++) {
                cin >> prices[(1<<i)-1 + j];
            }

        cout << "Case #" << z+1 << ": " << doit(0, 0) << endl;
    }
}
