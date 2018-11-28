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

int ddi[4] = { -1, -1,  0,  1};
int ddj[4] = {  0,  1,  1,  1};

bool belong(int i, int j, int n)
{
	return (0 <= i && i < n && 0 <= j && j < n);
}

void solve_case(int TN)
{
	int n, K;
	fin >> n >> K;
	
	vs b(n);
	FOR(i, n) fin >> b[i];
	
	vs r = b;
	FOR(i, n) FOR(j, n) r[i][j] = b[n-1-j][i];

	FOR(k, n)
	{
		int j = n-1;
		//while (j >= 0 && r[j][k] != '.') --j;
		FORR(i, 0, n-1)
		{
			if (r[i][k] != '.')
			{
				r[j][k] = r[i][k];
				if (j != i) r[i][k] = '.';
				--j;
			}
		}
	}

	bool RW = false, BW = false;
	FOR(i, n) FOR(j, n)
	{
		if (r[i][j] == '.') continue;
		char ch = r[i][j]; 
		FOR(k, 4)
		{
			int cnt = 0;
			for (int ii = i, jj = j; belong(ii, jj, n) && r[ii][jj] == ch; )
			{
				++cnt;
				if (cnt >= K) break;
				ii += ddi[k];
				jj += ddj[k];
			}
			if (cnt >= K)
			{
				if (ch == 'R')
					RW = true;
				else
					BW = true;
			}
		}
	}

	string ans = "Neither";
	if (RW && !BW) ans = "Red";
	if (!RW && BW) ans = "Blue";
	if (RW && BW) ans = "Both";

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
