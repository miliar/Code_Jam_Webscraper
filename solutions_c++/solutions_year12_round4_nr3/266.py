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

int A[2010];
int X[2010];
int N;
const int MAXH = 1000000000;
bool possible;

int geth(int a, int b, int ha, int hb, int c)
{
	int vx = b-a, vy = hb-ha, cx = c-a;
	int r = (int)(ha + (ld)vy / (ld)vx * (ld)cx - 0.1);
	return r;
}

void rec(int a, int b)
{
	if (a+1 == b) return;
	if (X[a+1] > b)
	{
		possible = false;
		return;
	}
	if (X[a+1] == b)
	{
		A[a+1] = geth(a, b, A[a], A[b], a+1);
		rec(a+1, b);
		return;
	}
	int xa1 = X[a+1];
	A[xa1] = geth(a, b, A[a], A[b], xa1);
	A[a+1] = geth(b, xa1, A[b], A[xa1], a+1);
	rec(a+1, xa1);
	if (!possible) return;
	rec(xa1, b);
}

void solve_case(int TN)
{
	fin >> N;
	FOR(i, N-1) fin >> X[i+1];
	FOR(i, N) A[i+1] = 0;
	A[1] = MAXH;
	possible = true;
	for (int i = 1; i < N; i = X[i])
	{
		A[X[i]] = MAXH;
		rec(i, X[i]);
		if (!possible) break;
	}

	fout << "Case #" << TN << ":";
	cout << "Case #" << TN << ":";
	if (possible)
	{
		FOR(i, N) fout << " " << A[i+1];
		FOR(i, N) cout << " " << A[i+1];
		fout << endl;
		cout << endl;
	}
	else
	{
		fout << " Impossible\n";
		cout << " Impossible\n";
	}
}

int main()
{
// 	ofstream fff("test.txt");
// 	FOR(i, 1000) fff << 2000-i << " ";
// 	FOR(i, 999) fff << 1002+i << " ";
// 	fff << endl;

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
