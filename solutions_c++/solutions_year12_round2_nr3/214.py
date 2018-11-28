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
	int n;
	fin >> n;
	vi a(n);
	FOR(i, n) fin >> a[i];
	map<int,vi> s2s;
	FOR(msk, 1<<n) if (msk > 0)
	{
		int s = 0;
		FOR(i, n) if (msk & (1<<i)) s += a[i];
		s2s[s].push_back(msk);
	}

	int msk1 = -1, msk2 = -1;
	for (map<int,vi>::iterator it = s2s.begin(); it != s2s.end(); ++it)
	{
		if (SZ(it->second) >= 2)
		{
			msk1 = it->second[0];
			msk2 = it->second[1];
			break;
		}
	}

	if (msk1 != -1)
	{
		fout << "Case #" << TN << ":" << endl;
		cout << "Case #" << TN << ":" << endl;
		FOR(i, n) if (msk1 & (1<<i))
		{
			fout << a[i] << " ";
			cout << a[i] << " ";
		}
		fout << endl;
		cout << endl;
		FOR(i, n) if (msk2 & (1<<i))
		{
			fout << a[i] << " ";
			cout << a[i] << " ";
		}
		fout << endl;
		cout << endl;
	}
	else
	{
		fout << "Case #" << TN << ": Impossible\n";
		cout << "Case #" << TN << ": Impossible\n";
	}
}

int main()
{
	fin.open("C.in"); 
	fout.open("C.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
