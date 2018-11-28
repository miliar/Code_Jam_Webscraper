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
	int C;
	fin >> C;
	map<int,int> v;
	FOR(i, C)
	{
		int p, k;
		fin >> p >> k;
		v[p] += k;
	}

	int m = 0;
	bool found = true;
	while (found)
	{
		found = false;
		map<int,int> q;
		for (map<int,int>::iterator it = v.begin(); it != v.end(); ++it)
		{
			int pos = it->first;
			int s = it->second;
			if (s > 1) found = true;
			if (s & 1) q[pos] += 1;
			q[pos-1] += s>>1;
			q[pos+1] += s>>1;
			m += s>>1;
		}
		v = q;
	}

	fout << "Case #" << TN << ": " << m << endl;
	cout << "Case #" << TN << ": " << m << endl;
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
