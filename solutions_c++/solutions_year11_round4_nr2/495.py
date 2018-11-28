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

i64 D[510][510];
i64 S[2][510][510];
i64 Zx[2][510][510],LSx[2][510][510],LZx[2][510][510];
i64 Zy[2][510][510],LSy[2][510][510],LZy[2][510][510];

void solve_case(int TN)
{
	// solution...
	int n, m, A;
	fin >> n >> m >> A;
	FOR(i, n)
	{
		string s;
		fin >> s;
		FOR(j, m) D[i][j] = s[j]-'0';
	}

	int ans = -1;
	FORD(i, 2, n-1) FORD(j, 2, m-1)
	{
		S[0][i][j] = 0;
		Zx[0][i][j] = 0;
		LSx[0][i][j] = 0;
		LZx[0][i][j] = 0;
		Zy[0][i][j] = 0;
		LSy[0][i][j] = 0;
		LZy[0][i][j] = 0;
		int ci = i-1, cj = j-1;
		FORD(ii, i-2, i) FORD(jj, j-2, j) 
		{
			S[0][i][j] += D[ii][jj];
			Zx[0][i][j] += D[ii][jj] * (jj-cj) * 2;
			Zy[0][i][j] += D[ii][jj] * (ii-ci) * 2;
		}
		FORD(ii, i-2, i)
		{
			LSy[0][i][j] += D[ii][j];
			LZy[0][i][j] += D[ii][j] * (ii-ci) * 2;
		}
		FORD(jj, j-2, j)
		{
			LSx[0][i][j] += D[i][jj];
			LZx[0][i][j] += D[i][jj] * (jj-cj) * 2;
		}

		i64 xx = Zx[0][i][j] - 2 * (-D[i-2][j-2] + D[i-2][j] - D[i][j-2] + D[i][j]);
		i64 yy = Zy[0][i][j] - 2 * (-D[i-2][j-2] - D[i-2][j] + D[i][j-2] + D[i][j]);
		if (xx == 0 && yy == 0) ans = 3;
	}

	FORD(k, 4, min(n, m))
	{
		int pt = k&1;
		int t = 1-pt;
		FORD(i, k-1, n-1) FORD(j, k-1, m-1)
		{
			S[t][i][j] = S[pt][i-1][j-1] + LSx[pt][i][j-1] + LSy[pt][i-1][j] + D[i][j];

			Zx[t][i][j] = Zx[pt][i-1][j-1] - S[pt][i-1][j-1] + 
				LZx[pt][i][j-1] - LSx[pt][i][j-1] +
				(LSy[pt][i-1][j] + D[i][j]) * (k-1);

			Zy[t][i][j] = Zy[pt][i-1][j-1] - S[pt][i-1][j-1] + 
				(LSx[pt][i][j-1] + D[i][j]) * (k-1) +
				LZy[pt][i-1][j] - LSy[pt][i-1][j];

			LSx[t][i][j] = LSx[pt][i][j-1] + D[i][j];
			LSy[t][i][j] = LSy[pt][i-1][j] + D[i][j];

			LZx[t][i][j] = LZx[pt][i][j-1] - LSx[pt][i][j-1] + D[i][j] * (k-1);
			LZy[t][i][j] = LZy[pt][i-1][j] - LSy[pt][i-1][j] + D[i][j] * (k-1);

			i64 xx = Zx[t][i][j] - (k-1) * (-D[i-k+1][j-k+1] + D[i-k+1][j] - D[i][j-k+1] + D[i][j]);
			i64 yy = Zy[t][i][j] - (k-1) * (-D[i-k+1][j-k+1] - D[i-k+1][j] + D[i][j-k+1] + D[i][j]);
			if (xx == 0 && yy == 0) ans = k;
		}
	}

	if (ans == -1)
	{
		fout << "Case #" << TN << ": IMPOSSIBLE\n";
		cout << "Case #" << TN << ": IMPOSSIBLE\n";
	}
	else
	{
		fout << "Case #" << TN << ": " << ans << endl;
		cout << "Case #" << TN << ": " << ans << endl;
	}
}

int main()
{
	fin.open("B.in"); 
	fout.open("B.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
