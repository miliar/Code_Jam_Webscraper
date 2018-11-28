#include <cstdlib>
#include <cctype>
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
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define clr(a) memset(a, 0, sizeof(a))
#define fil(a, b) memset(a, b, sizeof(a));
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define se(x) cout<<#x<<" = "<<x<<endl

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair <int, int> pii;

ll inf = 1LL << 60;
const int N = 210;
ll d, n;
pair<ll, ll> ven[N];

bool check(ll chk) {
	ll lim = -inf;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < ven[i].second; ++j) {
			ll l = ven[i].first - chk;
			ll r = ven[i].first + chk;
			if (lim <= l) {
				lim = l + d;
			} else if (lim <= r) {
				lim += d;
			} else {
				return false;
			}
		}
	}
	return true;
}

void solve(int cas) {
	ll a, b;
	scanf("%lld%lld", &n, &d);
	d *= 2;
	for (int i = 0; i < n; ++i) {
		scanf("%lld%lld", &a, &b);
		ven[i] = make_pair(a + a, b);
	}
	sort(ven, ven + n);
	ll mid, low = 0, high = inf / 8;
	while (low < high) {
		mid = (low + high) >> 1;
		if (!check(mid)) low = mid + 1;
		else high = mid;
	}
//	printf("%lld\n", low);
	printf("Case #%d: %lld", cas, low / 2);
	if (low & 1) puts(".5");
	else puts(".0");
}

int main() {
//	freopen("in","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		solve(i);
	}
	return 0;
}
