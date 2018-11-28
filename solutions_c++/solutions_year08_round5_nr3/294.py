#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()

#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef vector<int> VI;
int M[16][1024];

int toInt(string s)
{
	int res = 0;
	REP(i,SZ(s))
	{
		res *= 2;
		if (s[i] != '.')
			res += 1;
	}
	return res;
}
bool good(int k)
{
	int was = 0;
	while (k)
	{
		if (k&1)
		{
			if (was > 0)
				return false;
			was = 2;
		}
		was--;
		k /= 2;
	}
	return true;
}
int bitCount(int k)
{
	int res = 0;
	while (k)
	{
		k &= k-1;
		res++;
	}
	return res;
}
int tran(int k, int m)
{
	int res = 0;
	REP(i,m)
		if ((i && k&(1<<(i-1))) || k&(1<<(i+1)))
			res |= 1<<i;
	return res;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w+", stdout);
	int c;
	cin >> c;
	REP(it,c)
	{
		int n, m;
		cin >> n >> m;
		VI A(n);
		REP(i,n)
		{
			string s;
			cin >> s;
			A[i] = toInt(s);
		}
		reverse(ALL(A));
		memset(M, 0, sizeof(M));		
		int res = 0;
		REP(i,n)
		{
			REP(j,1<<m)
			{
				int zan = j|A[i];
				int cc = M[i][j];
				REP(k,1<<m)
					if ((zan&k) == 0 && good(k))
					{
						int tra = tran(k,m);
						M[i+1][tra] = max(M[i+1][tra], cc+bitCount(k));
						res = max(res, M[i+1][tra]);
					}
			}
		}

		printf("Case #%d: %d\n", it+1, res);
	}
}
