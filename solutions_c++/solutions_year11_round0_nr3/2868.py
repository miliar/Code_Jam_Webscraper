#include <vector>
#include <list>

#include <deque>
#include <queue>
#include <stack>

#include <map>
#include <set>

#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> ii;
#define infinity ~(1<<31)
#define longInfinity ~((1LL)<<63)
#define eps 1e-7
#define FOR(i,n) for((i) = 0 ; (i) <int(n);++(i))
#define MP make_pair
#define PB push_back
#define sz size()
#define ln length()
#define fill(f,a) memset(f, a, sizeof(f))
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define tr(container, it) for(typeof((container).begin()) it = (container).begin(); it != (container).end(); it++)
#define MT(a,b,c) MP(a,MP(b,c))
typedef pair<int, pair<int, int> > triple;

int a[1000];
map<triple, int> dp;

int f(int i, int x, int s) {
    if (i <= 0) {
        if (x == s && x != 0) {
            return 0;
        } else {
            return 1 << 31;
        }
    }
    triple temp = MT(i, x, s);
    if (dp.count(temp)) {
        return dp[temp];
    }
    return dp[temp] = max(f(i - 1, x ^ a[i - 1], s) + a[i - 1], f(i - 1, x, s^a[i - 1]));
}

int main() {
    int t, iterIndex, n, i;
    scanf("%d", &t);
    for (iterIndex = 0; iterIndex < t; ++iterIndex) {
        scanf("%d", &n);

        FOR(i, n) {
            scanf("%d", &a[i]);
        }
        int r = f(n, 0, 0);
        if (r < 0)
            printf("Case #%d: NO\n", iterIndex + 1);
        else
            printf("Case #%d: %d\n", iterIndex + 1, r);
        dp.clear();
    }
    return 0;
}
