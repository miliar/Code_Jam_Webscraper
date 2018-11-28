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

bool win(vi& a)
{
	bool w = (a[0] > 1);
	FORD(i, 1, SZ(a)-1)
	{
		if (a[i] == 1) w = !w;
		if (a[i] > 1) w = true;
	}
	return w;
}

void solve_case(int TN)
{
	int a1, a2, b1, b2;
	fin >> a1 >> a2 >> b1 >> b2;
	int ans = 0;
	FORD(a, a1, a2) FORD(b, b1, b2)
	{
		int aa = min(a, b);
		int bb = max(a, b);
		vi v;
		while (aa > 0)
		{
			v.push_back(bb / aa);
			bb %= aa;
			swap(aa, bb);
		}
		reverse(ALL(v));
		if (win(v)) ++ans;
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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
