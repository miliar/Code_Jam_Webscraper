#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define FN "B-large"

char conv[256][256];
bool rev[256][256];

char rc()
{
	char c;
	do c = getc(stdin); while (!isalpha(c));
	return c;
}

int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		CLEAR(conv);
		CLEAR(rev);
		int n;
		scanf("%d",&n);
		REP(i,n)
		{
			char c1 = rc();
			char c2 = rc();
			char c3 = rc();
			conv[c1][c2] = conv[c2][c1] = c3;
		}
		scanf("%d",&n);
		REP(i,n)
		{
			char c1 = rc();
			char c2 = rc();
			rev[c1][c2] = rev[c2][c1] = true;
		}
		scanf("%d",&n);
		vector<char> s;
		REP(i,n)
		{
			int c = rc();
			if (!s.empty() && conv[s.back()][c] != 0)
			{
				s.back() = conv[s.back()][c];
			}
			else
				s.push_back(c);
			REP(j,SZ(s))
				if (rev[s[j]][s.back()])
				{
					s.clear();
					break;
				}
		}
		printf("Case #%d: [",test);
		REP(i,SZ(s)) printf(", %c"+(i==0)*2, s[i]);
		printf("]\n");
	}
	return 0;
}