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

const int h = 262;

int C,D, n;
char c[h][h];
bool o[h][h];

char s[h];
int k[h];

string r;

int main()
{
	freopen("b-large.in", "r", stdin); //-small-attempt
	freopen("b-large.out", "w", stdout); //-large
	int T, it=1;
for(scanf("%d", &T); it<=T; ++it)
{
	CL(c, 0);
	CL(o, 0);
	scanf("%d", &C);
	REP(i, C)
	{
		scanf("%s", s);
		c[s[0]][s[1]] = c[s[1]][s[0]] = s[2];
	}
	scanf("%d", &D);
	REP(i, D)
	{
		scanf("%s", s);
		o[s[0]][s[1]] = o[s[1]][s[0]] = 1;
	}
	scanf("%d%s", &n, s);
	CL(k, 0);
	r.clear();
	REP(i, n)
	{
		if(r.empty())
		{
			r.pb(s[i]);
			++k[s[i]];
		}
		else
		{
			char x = c[r[sz(r)-1]][s[i]];
			if(x==0)
			{
				r.pb(s[i]);
				++k[s[i]];
			}
			else
			{
				--k[r[sz(r)-1]];
				r.erase(sz(r)-1, 1);
				r.pb(x);
				++k[x];
			}
			x = r[sz(r)-1];
			for(char y='A'; y<='Z'; ++y)
				if(o[x][y] && k[y]>0)
			{
				CL(k, 0);
				r.clear();
				break;
			}
		}
	}
	printf("Case #%d: [", it);
	REP(i, sz(r))
	{
		printf("%c", r[i]);
		if(i+1<sz(r)) printf(", ");
	}
	printf("]\n");
}
	return 0;
}
