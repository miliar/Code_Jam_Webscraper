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


void solve_case(int TN)
{
	int n;
	fin >> n;
	vs A(n);
	FOR(i, n) fin >> A[i];

	vd WP(n, 0.0);
	vd OWP(n, 0.0);
	FOR(i, n)
	{
		int cnto = 0;
		FOR(j, n)
		{
			if (A[i][j] == '.') continue;
			++cnto;
			WP[i] += A[i][j]-'0';
		}
		WP[i] /= cnto;

		cnto = 0;
		FOR(j, n) if (A[i][j] != '.')
		{
			++cnto;
			int cnt2o = 0;
			ld s = 0.0;
			FOR(k, n) if (k != i && A[j][k] != '.')
			{
				++cnt2o;
				s += A[j][k]-'0';
			}
			s /= cnt2o;
			OWP[i] += s;
		}
		OWP[i] /= cnto;
	}

	vd OOWP(n, 0.0);
	FOR(i, n)
	{
		int cnto = 0;
		FOR(j, n) if (A[i][j] != '.')
		{
			++cnto;
			OOWP[i] += OWP[j];
		}
		OOWP[i] /= cnto;
	}

	fout << "Case #" << TN << ":" << endl;
	cout << "Case #" << TN << ":" << endl;
	FOR(i, n)
	{
		ld x = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		fout << fixed << setprecision(10) << x << endl;
		cout << fixed << setprecision(10) << x << endl;
	}
}

int main()
{
	fin.open("A.in"); 
	fout.open("A.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
