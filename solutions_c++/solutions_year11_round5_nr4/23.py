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

const int h = 133;
char s[h];
int n;
vi o;

int main()
{
	freopen("d-small-attempt0.in", "r", stdin); //-small-attempt0
	freopen("d-small-attempt0.out", "w", stdout); //-large
	int ntest, itest=1;
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	scanf("%s", s);
	n = strlen(s);
	o.clear();
	REP(i, n) if(s[i]=='?')
		o.pb(i);
	printf("Case #%d: ", itest);
	REP(u, 1<<sz(o))
	{
		REP(i, sz(o))
		{
			if(u&1<<i) s[o[i]]='1';
			else s[o[i]]='0';
		}
		ll x = 0;
		REP(i, n)
		{
			x <<= 1;
			if(s[i]=='1') x+=1;
		}
		ll r = (ll)sqrt(double(x));
		while(r*r < x) ++r;
		while(r*r > x) --r;
		if(x == r*r)
		{
			printf("%s\n", s);
			break;
		}
	}
}
	return 0;
}
