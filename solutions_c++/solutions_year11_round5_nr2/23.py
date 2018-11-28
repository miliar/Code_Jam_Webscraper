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

const int h = 1111;
int n, a[h];
pii g[h];

int main()
{
	freopen("b-large.in", "r", stdin); //-small-attempt0
	freopen("b-large.out", "w", stdout); //-large
	int ntest, itest=1;
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	printf("Case #%d: ", itest);
	scanf("%d", &n);
	if(n==0)
	{
		printf("0\n");
		continue;
	}
	REP(i, n) scanf("%d", a+i);
	sort(a, a+n);
	int k = 0;
	REP(i, n)
	{
		g[k].X = a[i];
		g[k].Y = 0;
		int j = i;
		while(a[i]==a[j])
		{
			++g[k].Y;
			++j;
		}
		++k;
		i = j-1;
	}
	int res = n;
	FORD(i, k-1, 0)
	{
		while(g[i].Y>0 && (i==0 || g[i-1].X+1!=g[i].X || (g[i-1].X+1==g[i].X && g[i-1].Y < g[i].Y)))
		{
			int c = 0, j = i;
			while(j!=k && g[j].Y>0)
			{
				--g[j].Y;
				++c;
				++j;
			}
			res = min(res, c);
		}
	}
	printf("%d\n", res);
}
	return 0;
}
