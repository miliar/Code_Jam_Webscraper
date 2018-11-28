#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define DBG(x) cerr << #x << " = " << (x) << endl

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

#define INF 1000000000

int dp[8192][16];

int main()
{
	stdin = freopen("b.in","r",stdin);
	stdout = freopen("b.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		int p; cin >> p;
		int n = 1<<p;
		forn(i,n)
		{
			int x; cin >> x;
			forn(k,16) dp[n+i][k] = ((k<p - x)?INF:0);
		}
		for(int base = n/2;base >= 1; base /= 2)
		{
			forn(i,base)
			{
				int c; cin >> c;
				int h1 = (base+i)*2;
				int h2 = (base+i)*2+1;
				forn(k,15) dp[base+i][k] = min(INF,min(c + dp[h1][1+k] + dp[h2][1+k],dp[h1][k] + dp[h2][k]));
			}
		}
		int res = dp[1][0];
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
