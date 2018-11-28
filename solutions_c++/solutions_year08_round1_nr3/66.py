#include <algorithm>
#include <cstdio>
#include <cstdlib>
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
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

typedef pair <VI, int> num;

num mul (num a, num b)
{
	int n1 = a.X.size();
	int n2 = b.X.size();
	num res(VI(n1+n2-1), a.Y+b.Y);

	REP (i, n1)
	REP (j, n2)
	res.X[i+j]+=a.X[i]*b.X[j];

	for (int i=0; i<res.X.size (); i++)
	{
		if (res.X[i]>9)
		{
			int v = res.X[i]/10;
			res.X[i]%=10;

			if (i==res.X.size ()-1)
				res.X.pb (v);
			else
				res.X[i+1]+=v;
		}
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;

	REP (t, tt)
	{
		cout << "Case #"<<(t+1)<< ": ";


		int n;
		cin >> n;

		long double v = 3+sqrtl(5);

		char ss[100];
		sprintf (ss, "5.23606 79774 99789 69640 91736 68731 3");
		//cout << ss << endl;

		num vv(VI(), 31);

		FORD (i, strlen(ss)-1, 0)
			if (isdigit(ss[i]))
				vv.X.pb (ss[i]-'0');

		//REP (i, vv.X.size ())
		//	cout << vv.X[i];
		//cout << endl;

		num res (VI(3), 0);
		res.X[0] = 1;

		REP (i, n)
			res = mul(res, vv);

		FORD (i, res.Y+2, res.Y)
			cout << res.X[i];
		cout << endl;

	}

	return 0;
}
