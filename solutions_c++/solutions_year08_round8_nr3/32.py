#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

const i64 MD = 1000000009;

vi w;
vvi a;
i64 c;

i64 HH(i64 n, i64 m)
{
	if (m > n) return 0;
	i64 res = 1;
	FOR(i, m) res = (res * (n-i)) % MD;
	return res;
}

i64 rec(int v, int d, i64 cc)
{
	int N = SZ(a[v]);
	
	if (N == 1 && d > 0) return 1;

	w[v] = 1;
	
	i64 res = 1;

	if (d == 0) 
		res = HH(cc, N);
	else 
		res = HH(cc, N-1);

	FOR(i, N)
	{
		int j = a[v][i];
		if (w[j]) continue;
		res *= rec(j, d+1, c-N);
		res %= MD;
	}

	w[v] = 0;

	return res;
}

int main()
{
	ifstream fin("c.in"); ofstream fout("c.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int n;
		fin >> n >> c;

		a.assign(n+1, vi());
		
		FOR(i, n-1)
		{
			int x, y;
			fin >> x >> y;
			a[x].push_back(y);
			a[y].push_back(x);
		}

		w.assign(n+1, 0);
		i64 ans = rec(1, 0, c);

		fout << "Case #" << tt+1 << ": " << ans << endl;
	}
	return 0;	
}
