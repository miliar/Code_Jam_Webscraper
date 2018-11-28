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
	int N;
	fin >> N;
	vi a(N), c(N);
	int s = 0;
	FOR(i, N) 
	{
		fin >> a[i];
		c[i] = i;
		s += a[i];
	}
	FOR(i, N) FORD(j, i+1, N-1) if (a[i] > a[j])
	{
		swap(a[i], a[j]);
		swap(c[i], c[j]);
	}
	vd ans(N, 0.0);
	FOR(i, N)
	{
		ld score = 0.0;
		FORD(j, 1, i) score -= a[0] - a[j];
		score /= s;
		score += 1.0;
		score /= i+1;
		score = a[0] + s * score;
		if (i < N-1 && score > a[i+1]) continue;
		FOR(k, i+1)
		{
			score = 0.0;
			FOR(j, i+1) score -= a[k] - a[j];
			score /= s;
			score += 1.0;
			score /= i+1;
			ans[c[k]] = 100.0 * score;
		}
		break;
	}

	fout << "Case #" << TN << ":";
	cout << "Case #" << TN << ":";
	FOR(i, N)
	{
		fout << fixed << setprecision(7) << " " << ans[i];
		cout << fixed << setprecision(7) << " " << ans[i];
	}
	fout << endl;
	cout << endl;
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
