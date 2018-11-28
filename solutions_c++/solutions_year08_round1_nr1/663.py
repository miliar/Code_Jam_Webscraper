#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long LL;
typedef vector<LL> VL;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef stringstream SS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define FOR(i,a,b) for(int i = (a); i < int(b); ++i)
#define SZ(v) ((int)(v).size())
LL getMinSum(VL& x, VL& y) {
    sort(x.begin(), x.end());
    sort(y.begin(),y.end());
    LL ret = 0;
    int n = SZ(x);
    for (int i = 0; i < n/2; ++i) {
        ret += x[i]*y[n-1-i]+x[n-1-i]*y[i];
    }
    if (n%2!=0)
        ret += x[n/2]*y[n/2];
    return ret;
}
void main() {
    freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, num;
        scanf("%d", &n);
        VL x,y;
        for (int j = 0; j < n; ++j) {
            scanf("%d", &num);
            x.push_back((LL)num);
        }
        for (int j = 0; j < n; ++j) {
            scanf("%d", &num);
            y.push_back((LL)num);
        }
        LL mnSum = getMinSum(x, y);
        printf("Case #%d: %lld\n", i+1,  mnSum);
    }
}