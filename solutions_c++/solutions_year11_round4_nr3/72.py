#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for(int i=(a), _b=(b); i<_b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FORD(i, a, b) for(int i=(a), _b=(b); i>=_b; --i)
#define CL(a, v) memset(a, v, sizeof a)
#define INF 1000000000
#define INF_LL 1000000000000000000LL
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int h = 1000011;

ll n;
bool y[h];
ll p[h], k=0;

int main()
{
	freopen("c-large.in", "r", stdin); //-small-attempt0
	freopen("c-large.out", "w", stdout); //-large
	int ntest, itest=1;
	y[1] = 1;
	for(int i = 2; i < h; ++i) if(!y[i])
	{
		p[k++] = i;
		for(ll j = i; j * i < h; ++j) y[j * i] = 1;
	}
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	scanf("%I64d", &n);
	ll ans = 1;
	for(int i=0; i<k && p[i]*p[i] <= n; ++i)
	{
		ll t = n;
		while(t) t /= p[i], ++ans;
		ans -= 2;
	}
	if(n==1) ans = 0;
	printf("Case #%d: %I64d\n", itest, ans);
}
	return 0;
}
