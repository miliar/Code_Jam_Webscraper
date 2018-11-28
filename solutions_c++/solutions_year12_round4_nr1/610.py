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

int f[10100];
int d[10100];
int len[10100];

void solve_case(int TN)
{
	int N, D;
	fin >> N;
	FOR(i, N) fin >> d[i] >> len[i];
	fin >> D;
	len[0] = min(len[0], d[0]);

	FOR(i, N) f[i] = -1;
	f[0] = d[0];
	FOR(i, N-1)
	{
		if (f[i] == -1) continue;
		FORD(j, i+1, N-1)
		{
			if (d[i] + f[i] < d[j]) break;
			f[j] = max(f[j], min(len[j], d[j]-d[i]));
		}
	}
	string ans = "NO";
	FOR(i, N) 
	{
		if (f[i] != -1 && d[i] + f[i] >= D)
			ans = "YES";
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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
