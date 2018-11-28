#include <stdio.h>
#include <time.h>
#include <vector>
#include <list>
#include <set>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <iomanip>
#include <cmath>
#include <stack>
#include <numeric>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <utility>
#include <memory>
#include <functional>
#include <complex>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;

#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))
#define SORT(a) sort(a.begin(), a.end())
#define REVERSE(a) reverse(a.begin(), a.end())
#define PB(n) push_back(n)
#define SZ(a) int((a).size())
#define IPOW(a,b) ((long long) pow((double)(a),(double)(b)))
#define PI M_PI
#define EPS 1e-13
#define INF 0x7f7f7f7f

#define DEBUG 1
#define DBG(a) if (DEBUG) cout <<"DEBUG::: " <<a <<endl;
#define DBG2(a, b) if (DEBUG) cout <<"DEBUG::: " <<a <<"=" <<b <<endl;

#define MAX_N 10005

int N;
int D;
int d[MAX_N];
int l[MAX_N];

bool dfs(int d_from, int i_have) {
    int d_to = 2 * d[i_have] - d_from;
    if (D <= d_to) return true;
    for (int i=i_have+1;i<N;i++) {
        if (d[i] <= d_to) {
            int d_from_tmp = d[i] - min(d[i]-d[i_have], l[i]);
            if (dfs(d_from_tmp, i)) return true;
        }
    }
    return false;
}

int main() {
    int T;
    cin >>T;
    cin.ignore();

    for(int t=1; t<=T; t++) {

        cin >>N;
        FORI(i, N) cin >>d[i] >>l[i];
        cin >>D;

        if (dfs(0,0)) {
            cout <<"Case #" <<t <<": YES" <<endl;
        }
        else {
            cout <<"Case #" <<t <<": NO" <<endl;
        }
    }
    return 0;
}
