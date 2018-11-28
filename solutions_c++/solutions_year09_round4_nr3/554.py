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

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<tint> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

int g[32][32];

int dp[1<<17];
int va[1<<17];

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		int n,k;
		cin >> n >> k;
		vvint v(n,vint(k));
		forn(i,n)
		forn(j,k)
			cin >> v[i][j];
		zMem(g);
		forn(i,n)
		forn(j,n)
		{
			int c = 0;
			forn(z,k-1)
			if ((v[i][z] - v[j][z]) * (v[i][z+1] - v[j][z+1]) <= 0)
			{
				c = 1;
				break;
			}
			g[i][j] = c;
		}
		forn(m,1<<n)
		{
			int funca = 1;
			forn(i,n)
			if ((1<<i)&m)
			forn(j,i)
			if (((1<<j)&m)&& g[i][j])
			{
				funca = 0;
				goto salida;
			}
salida:
			va[m] = funca;
		}
		dp[0] = 0;
		forsn(m,1,1<<n)
		{
			int res = 10000;
			for(int sub = m;sub != 0;sub = (sub-1)&m)
			if (va[sub] && dp[m-sub] < res)
			{
				res = dp[m-sub];
			}
			dp[m] = res + 1;
		}
		int res = dp[(1<<n)-1];
		cout << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}

