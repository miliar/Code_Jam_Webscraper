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

const int K = 120;
int A[2][K][K];

void solve_case(int TN)
{
	FOR(i, K) FOR(j, K) A[0][i][j] = A[1][i][j] = 0;
	int R;
 	fin >> R;
	int mx = 0, my = 0;
	FOR(i, R)
	{
		int x1, y1, x2, y2;
		fin >> x1 >> y1 >> x2 >> y2;
		FORD(xx, x1, x2) FORD(yy, y1, y2) A[0][xx][yy] = 1;
		mx = max(mx, x2);
		my = max(my, y2);
	}

	++mx, ++my;
	int ans = 0;
	for (int i = 0; ; i = 1-i)
	{
		++ans;
		int j = 1-i;
		bool found = false;
		FORD(xx, 1, mx) FORD(yy, 1, my)
		{
			A[j][xx][yy] = A[i][xx][yy];
			if (!A[i][xx][yy] && A[i][xx-1][yy] && A[i][xx][yy-1]) A[j][xx][yy] = 1;
			if (A[i][xx][yy] && !A[i][xx-1][yy] && !A[i][xx][yy-1]) A[j][xx][yy] = 0;
			if (A[j][xx][yy]) found = true;
		}
		if (!found) break;
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
