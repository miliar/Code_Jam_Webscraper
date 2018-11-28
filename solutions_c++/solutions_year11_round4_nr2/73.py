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

const int h = 555;

struct D
{
	ll x,y,w;
	D (ll x=0, ll y=0, ll w=0) : x(x), y(y), w(w) {}
} d[h][h], sum[h][h];

D operator + (const D &a, const D &b)
{	return D(a.x+b.x, a.y+b.y, a.w+b.w); }

D operator - (const D &a, const D &b)
{	return D(a.x-b.x, a.y-b.y, a.w-b.w); }

int r,c, dd, sx,sy;
int w[h][h], x[h][h], y[h][h];
char s[h][h];

int main()
{
	freopen("b-large.in", "r", stdin); //-small-attempt0
	freopen("b-large.out", "w", stdout); //-large
	int ntest, itest=1;
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	scanf("%d%d%d", &r, &c, &dd);
	REP(i, r) scanf("%s", s+i);
	REP(i, r) REP(j, c) w[i][j] = s[i][j]-'0';
	REP(i, r) REP(j, c)
	{
		x[i][j] = w[i][j]*i;
		y[i][j] = w[i][j]*j;
		d[i][j] = D(x[i][j], y[i][j], w[i][j]);
		sum[i+1][j+1] = d[i][j] + sum[i][j+1] + sum[i+1][j] - sum[i][j];
	}
	//REP(i, r+1) { REP(j, c+1) printf("%d ", sum[i][j].w); printf("\n"); };
	int ans = -1;
	FORD(k, min(r, c), 3)
	{
		//printf("%d:\n", k);
		bool ok = false;
		REP(i, r-k+1) REP(j, c-k+1)
		{
			//printf("%d %d:\n", i, j);
			D sq = sum[i+k][j+k] - sum[i][j+k] - sum[i+k][j] + sum[i][j];
			//printf("%d %d %d\n", sq.x, sq.y, sq.w);
			sq = sq - d[i][j] - d[i][j+k-1] - d[i+k-1][j] - d[i+k-1][j+k-1];
			//printf("%d %d %d\n", sq.x, sq.y, sq.w);
			//printf("%d %d\n", 2 * sq.x - (2*i + k-1) * sq.w, 2 * sq.y - (2*j + k-1) * sq.w);
			if((2 * sq.x == (2*i + k-1) * sq.w) && (2 * sq.y == (2*j + k-1) * sq.w))
			{
				ok = true;
				ans = k;
				break;
			}
		}
		if(ok) break;
	}
	printf("Case #%d: ", itest);
	if(ans==-1) printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
}
	return 0;
}
