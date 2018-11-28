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
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<string> VS;
struct SO
{
	bool operator()(VI x, VI y)
	{
		while (SZ(x))
		{
			int xI = max_element(ALL(x))-x.begin();
			int yI = max_element(ALL(y))-y.begin();
			if (x[xI] != y[yI])
				return x[xI] > y[yI];
			if (xI != yI)
				return xI < yI;
			x.erase(x.begin()+xI);
			y.erase(y.begin()+yI);
		}
		return false;
	}
};

bool operator<(const VI &x, const VI &y)
{
	return true;
}

bool good(const VI &v1, const VI &v2)
{
	REP(i,SZ(v1))
		if (v1[i] <= v2[i])
			return false;
	return true;
}
int calc(VVI v)
{
	int res = 0;
	while (SZ(v))
	{
		res++;
		int ind = 0;
		int lInd = 0;
		while (ind < SZ(v))
		{
			if (good(v[lInd], v[ind]))
			{					
				v.erase(v.begin()+lInd);
				lInd = ind-1;
				ind--;
			}
			ind++;
		}
		v.erase(v.begin()+lInd);
	}
	return res;
}
bool good(const VVI &x, int mask)
{
	VVI y;
	REP(i,SZ(x))
		if (mask&(1<<i))
			y.pb(x[i]);
	sort(ALL(y));
	REP(i,SZ(y)-1)
		if (good(y[i+1], y[i]) == false)
			return false;
	return true;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w+", stdout);	int T;
	cin >> T;
	REP(it,T)
	{
		cerr << it << ' ' << T << endl;
		int n, k;
		cin >> n >> k;
		VVI v(n, VI(k));
		REP(i,n)
			REP(j,k)
				cin >> v[i][j];
		VI goodMasks;
		REP(i,1<<SZ(v))
			if (good(v,i))
				goodMasks.pb(i);
		vector<bool> WAS(1<<SZ(v), false);
		REP(i,SZ(goodMasks))
			WAS[goodMasks[i]] = true;
		int kk = 0;
		REP(i,SZ(goodMasks))
		{
			bool need = true;
			int mask = goodMasks[i];
			REP(j,SZ(v))
				if ((mask&(1<<j)) == 0 & WAS[mask|(1<<j)])
					need = false;
			if (need)
				goodMasks[kk++] = goodMasks[i];
		}
		goodMasks.resize(kk);
/*		sort(ALL(goodMasks));
		reverse(ALL(goodMasks));
		int res = INF;
		sort(ALL(v), SO());
		REP(i,SZ(v))
			cout << *max_element(ALL(v[i])) << endl;
			*/
		//reverse(ALL(v));
		VI S(1<<SZ(v),INF);
		S[0] = 0;
		REP(i,SZ(S))
		{
			if (S[i] < S.back()-1)
			{
				int val = S[i];
				REP(j,SZ(goodMasks))
					S[i|goodMasks[j]] = min(val+1,S[i|goodMasks[j]]);
			}
		}
		printf("Case #%d: %d\n", it+1, S.back());
	}
}
