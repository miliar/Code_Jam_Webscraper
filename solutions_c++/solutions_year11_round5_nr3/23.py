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

const int mod = 1000003;
void inc (int a, int b) { a+=b; if(a>=mod) a-=mod; }
int add (int a, int b) { a+=b; if(a>=mod) a-=mod; return a; }
int mul (int a, int b) { return ll(a) * b % mod; }

const int h = 111;
int r,c;
char a[h][h];
bool o[h][h];
pii u0[h][h], u1[h][h];
int k[h][h];

vector<pii> q;

inline void go (pii p, int v)
{
	k[p.X][p.Y] += v;
	if(v==-1 && k[p.X][p.Y]==1) q.pb(p);
}

int main()
{
	freopen("c-large.in", "r", stdin); //-small-attempt0
	freopen("c-large.out", "w", stdout); //-large
	int ntest, itest=1;
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	scanf("%d%d", &r, &c);
	REP(i, r) scanf("%s", a[i]);
	REP(i, r) REP(j, c) switch(a[i][j])
	{
		case '|':
			u0[i][j] = pii((i-1+r)%r, j);
			u1[i][j] = pii((i+1)%r, j); 
			break;
		case '-':
			u0[i][j] = pii(i, (j-1+c)%c);
			u1[i][j] = pii(i, (j+1)%c); 
			break;
		case '/':
			u0[i][j] = pii((i-1+r)%r, (j+1)%c);
			u1[i][j] = pii((i+1)%r, (j-1+c)%c); 
			break;
		case '\\':
			u0[i][j] = pii((i-1+r)%r, (j-1+c)%c);
			u1[i][j] = pii((i+1)%r, (j+1)%c); 
			break;
	}
	REP(i, r) REP(j, c) k[i][j] = 0;
	REP(i, r) REP(j, c)
	{
		go(u0[i][j], 1);
		go(u1[i][j], 1);
		o[i][j] = 0;
	}
	//REP(i, r) { REP(j, c) printf("%d", k[i][j]); printf("\n"); }
	q.clear();
	bool ok = true;
	REP(i, r) REP(j, c)
	{
		if(k[i][j]==0) ok = false;
		if(k[i][j]==1) q.pb(pii(i, j));
	}
	int e = 0;
	int ans = 0;
	if(ok) while(e<sz(q))
	{
		pii u = q[e++];
		if(k[u.X][u.Y]!=1)
		{
			ok = false;
			break;
		}
		ok = false;
		FOR(x, u.X-1, u.X+2) FOR(y, u.Y-1, u.Y+2)
		{
			int i = (x+r)%r, j = (y+c)%c;
			if(!o[i][j] && (u0[i][j]==u || u1[i][j]==u))
			{
				ok = true;
				o[i][j] = 1;
				if(u0[i][j]==u) go(u1[i][j], -1);
				else go(u0[i][j], -1);
				goto l1;
			}
		}
		l1:;
		if(!ok) break;
	}
if(ok)
{
	//REP(i, r) { REP(j, c) printf("%d", o[i][j]); printf("\n"); }
	ans = 1;
	REP(ii, r) REP(jj, c) if(!o[ii][jj])
	{
		//printf("%d %d:\n", ii, jj);
		pii u = pii(ii, jj), p = pii(-1, -1);
		while(1)
		{
			//printf("%d %d\n", u.X, u.Y);
			o[u.X][u.Y] = 1;
			if(p==u0[u.X][u.Y]) p = u1[u.X][u.Y];
			else p = u0[u.X][u.Y];
			bool ye = false;
			FOR(x, p.X-1, p.X+2) FOR(y, p.Y-1, p.Y+2)
			{
				int i = (x+r)%r, j = (y+c)%c;
				if(!o[i][j] && (u0[i][j]==p || u1[i][j]==p))
				{
					u = pii(i, j);
					ye = true;
					goto l2;
				}
			}
			l2:;
			if(!ye) break;
		}
		ans = mul(ans, 2);
	}
}
	printf("Case #%d: %d\n", itest, ans % mod);
}
	return 0;
}
