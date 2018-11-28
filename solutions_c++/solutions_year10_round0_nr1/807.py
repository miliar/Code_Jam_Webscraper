#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define INF  ((1 << 31) - 1)
#define eps 1e-9
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	ll t, n, k;
	cin >> t;
	for (ll tt = 1; tt <= t; ++tt){
		printf("Case #%lld: ", tt);
		scanf("%lld%lld", &n, &k);
		if (k % (1 << n) == (1 << n) - 1) printf("ON\n");
		else printf("OFF\n");
		cerr << tt << " of " << t << " tests pased\n";
	}
	cerr << "all tests passed\n";
	return 0;
}
