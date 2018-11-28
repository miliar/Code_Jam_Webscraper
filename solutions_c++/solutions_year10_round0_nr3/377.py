#include <vector>
#include <algorithm>
#include <cmath>
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
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<i64> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;


void solve_case(int TN)
{
	int R, k, n;
	fin >> R >> k >> n;

	vi a(n);
	FOR(i, n) fin >> a[i];
	FOR(i, n) a.push_back(a[i]);

	vector<int> x(n);
	vi b(n);
	FORR(i, 0, n-1)
	{
		i64 s = 0;
		int j = i;
		for (; j <= i+n && s <= k; ++j) s += a[j];
		x[i] = (j-1) % n;
		b[i] = s - a[x[i]];
	}

	i64 ans = 0;
	vector<int> y(n, -1);
	vi ps(n, 0);
	y[0] = 0;
	ps[0] = 0;
	int c = 1, v = 0;
	for (v = 0; c <= R; ++c)
	{
		ans += b[v];
		v = x[v];
		if (y[v] != -1) 
		{
			c -= y[v];
			R -= y[v];
			ans += (i64)(R / c - 1) * (ans - ps[v]);
			break;
		}
		y[v] = c;
		ps[v] = ans;
	}

	if (c < R) for (int i = v, j = 0; j < R%c; ++j, i = x[i])
	{
		ans += b[i];
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("c.in"); 
	fout.open("c.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
