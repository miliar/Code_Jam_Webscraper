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

typedef vector<int> vi;
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


void solve_case(int TN)
{
	int D, I, M, N;
	fin >> D >> I >> M >> N;

	vi a(N);
	FOR(i, N) fin >> a[i];

	const int inf = 123456789;
	vi f(256, inf);
	FOR(i, 256) f[i] = abs(i-a[0]);

	FORD(i, 1, N-1)
	{
		vi g = f, h(256, inf);
		FOR(j, 256) h[j] = f[j] + D;
		FOR(k, 256)
		{
			f = g;
			FOR(j, 256) FORD(jj, max(0,j-M), min(255,j+M)) 
			{
				h[jj] = min(h[jj], f[j] + abs(jj-a[i]));
			}
			g.assign(256, inf);
			FOR(j, 256) FORD(jj, max(0,j-M), min(255,j+M))
			{
				g[jj] = min(g[jj], f[j] + I);
			}
		}
		FOR(j, 256) h[j] = min(h[j], abs(j-a[i]) + i*D);
		f = h;
	}

	int ans = *min_element(ALL(f));

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
