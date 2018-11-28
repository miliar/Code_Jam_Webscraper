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

vs B;

int who(int si, int sj, int di, int dj)
{
	int xc = 0, oc = 0, tc = 0; 
	FOR(i, 4)
	{
		if (B[si][sj] == 'X') ++xc;
		if (B[si][sj] == 'O') ++oc;
		if (B[si][sj] == 'T') ++tc;
		si += di, sj += dj;
	}
	if (xc + tc == 4) return 1;
	if (oc + tc == 4) return 2;
	return 0;
}

void outputans(int TN, int aid)
{
	string ans = "Game has not completed";
	if (aid == 0) ans = "Draw";
	if (aid == 1) ans = "X won";
	if (aid == 2) ans = "O won";
	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

void solve_case(int TN)
{
	B.resize(4);
	FOR(i, 4) fin >> B[i];
	if (who(0, 0, 1, 1) == 1 || who(0, 3, 1, -1) == 1)
	{
		outputans(TN, 1);
		return;
	}
	if (who(0, 0, 1, 1) == 2 || who(0, 3, 1, -1) == 2)
	{
		outputans(TN, 2);
		return;
	}
	bool wp = false;
	FOR(i, 4)
	{
		FOR(j, 4) if (B[i][j] == '.') wp = true;
		if (who(i, 0, 0, 1) == 1 || who(0, i, 1, 0) == 1)
		{
			outputans(TN, 1);
			return;
		}
		if (who(i, 0, 0, 1) == 2 || who(0, i, 1, 0) == 2)
		{
			outputans(TN, 2);
			return;
		}
	}
	if (wp)
		outputans(TN, -1);
	else
		outputans(TN, 0);
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
