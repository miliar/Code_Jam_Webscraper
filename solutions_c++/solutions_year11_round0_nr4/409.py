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

const int h = 1010;
double f[h], s;

int n, a[h];
bool y[h];

int main()
{
	s = f[1] = 0;
	FOR(i, 2, h)
	{
		f[i] = 2 * (s + 1) / (i-1);
		s += f[i];
	}
	freopen("d-large.in", "r", stdin); //-small-attempt
	freopen("d-large.out", "w", stdout); //-large
	//REP(i, 30) printf("%d %lf\n", i, f[i]);
	int T, it=1;
for(scanf("%d", &T); it<=T; ++it)
{
	scanf("%d", &n);
	REP(i, n) scanf("%d", a+i);
	double ans = 0;
	CL(y, 0);
	REP(i, n) if(!y[i])
	{
		int j=i, k=0;
		while(!y[j])
		{
			++k;
			y[j] = 1;
			j = a[j]-1;
		}
		ans += f[k];
	}
	printf("Case #%d: %.9lf\n", it, ans);
}
	return 0;
}
