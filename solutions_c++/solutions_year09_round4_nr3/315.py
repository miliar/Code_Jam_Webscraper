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
#define		MP	make_pair
#define		PB	push_back

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int n, k;
int p[17][27];
int f[1<<17];
int g[1<<17];
int I[17][17];

int inters(int a, int b)
{
	FOR(i, k) if (p[a][i] == p[b][i]) return 1;
	FOR(i, k-1)
	{
		if (p[a][i] < p[b][i] && p[a][i+1] > p[b][i+1]) return 1;
		if (p[a][i] > p[b][i] && p[a][i+1] < p[b][i+1]) return 1;
	}
	return 0;
}

int check(int msk)
{
	if (g[msk] > -1) return g[msk];
	if (msk == 0) return g[msk] = 1;
	if ((msk & (msk-1)) == 0) return g[msk] = 1;

	int idx = 0;
	while ((msk & (1<<idx)) == 0) ++idx;

	g[msk] = check(msk-(1<<idx));

	if (g[msk] == 0) return g[msk];

	FOR(i, n)
	{
		if (i == idx || ((1<<i) & msk) == 0) continue;
		if (I[i][idx]) return g[msk] = 0;
	}

	return g[msk] = 1;
}

int rec(int msk)
{
	if (f[msk] > -1) return f[msk];
	if (msk == 0) return f[msk] = 0;
	if ((msk & (msk-1)) == 0) return f[msk] = 1;

	f[msk] = n;
	for (int nmsk = msk; nmsk > 0; nmsk = ((nmsk-1) & msk))
	{
		if (check(nmsk))
		{
			int rr = rec(msk ^ nmsk);
			f[msk] = min(f[msk], rr + 1);
		}
	}

	return f[msk];
}

int main()
{
	ifstream fin("C.in"); ofstream fout("C.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		fin >> n >> k;
		FOR(i, n) FOR(j, k) fin >> p[i][j];

		FOR(i, n) FOR(j, n) I[i][j] = inters(i,j);

		FOR(msk, 1<<n) f[msk] = g[msk] = -1;
		int ans = rec((1<<n)-1);

		fout << "Case #" << tt+1 << ": " << ans << endl;
		cout << "Case #" << tt+1 << ": " << ans << endl;
	}
	return 0;	
}
