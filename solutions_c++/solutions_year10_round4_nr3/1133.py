#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x) {
    return x*x;
}

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

bool work(int arr[105][105]) {
    bool ret=0;
    for (int i = 104; i > 0; --i) {
        for (int j = 104; j > 0; --j) {
            if (arr[i - 1][j] && arr[i][j - 1]) arr[i][j] = 1;
            if (!arr[i - 1][j] && !arr[i][j - 1]) arr[i][j] = 0;
            if(arr[i][j]) ret=1;
        }
    }
    return ret;
}

int main(int argc, char** argv) {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for (int ti = 0; ti < t; ti++) {
        int n;
        cin >> n;
        int arr[105][105] = {0};
        for (int i = 0; i < n; ++i) {
            int x1, x2, y1, y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int x = x1; x <= x2; ++x) {
                for (int y = y1; y <= y2; ++y) {
                    arr[x][y] = 1;
                }
            }
        }
        int cnt = 0;
        for (; work(arr); ++cnt);
        printf("Case #%d: %d\n", ti+1, cnt+1);

    }
    return (EXIT_SUCCESS);
}

