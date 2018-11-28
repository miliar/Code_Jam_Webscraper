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

template <class T> T sqr(T x)
{
    return x*x;
}

int gcd(int a, int b)
{
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int main(int argc, char** argv)
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    int t;
	scanf("%d", &t);
	for(int ti=1; ti<=t; ++ti) {
		int n;
		int x;
		int res = 0;
		int ans = inf;
		int sum=0;
		scanf("%d", &n);
		for(int i=0; i<n; ++i) {
			int x;
			scanf("%d", &x);
			res ^= x;
			ans = min(ans, x);
			sum += x;
		}
		printf("Case #%d: ", ti);
		if(res != 0) puts("NO");
		else {
			printf("%d\n", sum-ans);
		}

	}
    return (EXIT_SUCCESS);
}

