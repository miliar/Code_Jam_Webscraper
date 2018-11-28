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

typedef vector<ld> vd;
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

i64 solve2(i64 L, i64 a, i64 b)
{
	if (L % a == 0) return L / a;
	for (i64 s = L % a; s <= 2 * a * b && s + a <= L; s += a)
	{
		if (s % b == 0) 
			return (L - s) / a + s / b;
	}
	return -1;
}

i64 solve3(i64 L, i64 a, i64 b, i64 c)
{
	if (L % a == 0) return L / a;
	
	i64 s = L % a;
	i64 res = -1;
	for (i64 i = 1; i <= 2*a && s + a <= L; ++i, s += a)
	{
		i64 dtmp = (L - s) / a;
		i64 tmp1 = solve2(s, a, b);
		i64 tmp2 = solve2(s, a, c);
		i64 tmp3 = solve2(s, b, c);
		if (tmp1 != -1 && (res == -1 || tmp1 + dtmp < res)) res = tmp1 + dtmp;
		if (tmp2 != -1 && (res == -1 || tmp2 + dtmp < res)) res = tmp2 + dtmp;
		if (tmp3 != -1 && (res == -1 || tmp3 + dtmp < res)) res = tmp3 + dtmp;
	}
	return res;
}

void solve_case(int TN)
{
	i64 L;
	int n;
	fin >> L >> n;
	vi a(n);
	FOR(i, n) fin >> a[i];
	sort(ALL(a));

	i64 ans = -1;

	if (n == 1)
	{
		if (L % a[0] == 0) ans = L / a[0];
	}
	else if (n == 2)
	{
		ans = solve2(L, a[1], a[0]);
	}
	else
	{
		FOR(i, n-1) FOR(j, i)
		{
			i64 tmp = solve3(L, a.back(), a[i], a[j]);
			if (ans == -1 || tmp != -1 && tmp < ans) ans = tmp;
		}
	}

	if (ans == -1)
	{
		fout << "Case #" << TN << ": IMPOSSIBLE" << endl;
		cout << "Case #" << TN << ": IMPOSSIBLE" << endl;
	}
	else
	{
		fout << "Case #" << TN << ": " << ans << endl;
		cout << "Case #" << TN << ": " << ans << endl;
	}
}

int main()
{
	fin.open("B.in"); 
	fout.open("B.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
