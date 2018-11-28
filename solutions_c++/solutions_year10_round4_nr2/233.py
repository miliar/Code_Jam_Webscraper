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

i64 inf = 1000000000000000LL;

vvvi f;
vi M;
vvi C;
int P;

i64 rec(int buy, int lev, int idx)
{
	i64 & r = f[buy][lev][idx];
	if (r != -1) return r;

	if (lev == P)
	{
		if (buy < P-M[idx]) return r = inf;
		return r = 0;
	}

	i64 tmp1 = rec(buy, lev+1, 2*idx) + rec(buy, lev+1, 2*idx+1);
	i64 tmp2 = C[lev][idx] + rec(buy+1, lev+1, 2*idx) + rec(buy+1, lev+1, 2*idx+1);
	r = min(tmp1, tmp2);
	return r;
}

void solve_case(int TN)
{
	fin >> P;
	M.resize(1<<P);
	FOR(i, 1<<P) fin >> M[i];
	C.resize(P);
	FOR(i, P)
	{
		int k = 1<<(P-i-1);
		C[i].resize(k);
		FOR(j, k) fin >> C[i][j];
	}
	reverse(ALL(C));

	f.assign(P+1, vvi(P+1, vi(1<<P, -1)));
	i64 ans = rec(0, 0, 0);

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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
