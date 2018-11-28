#include <vector>
#include <algorithm>
#include <math.h>
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

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

const i64 M = 10007;

int main()
{
	ifstream fin("d.in"); ofstream fout("d.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		vvi a(110, vi(110, 0)), f(110, vi(110, 0));
		int h, w, R;
		fin >> h >> w >> R;
		FOR(i, R) 
		{
			int x, y;
			fin >> x >> y;
			a[x][y] = 1;
		}

		f[1][1] = 1;
		FORD(i, 1, h) FORD(j, 1, w)
		{
			if (a[i][j]) continue;
			f[i+2][j+1] += f[i][j];
			f[i+1][j+2] += f[i][j];
			f[i+2][j+1] %= M;
			f[i+1][j+2] %= M;
		}

		fout << "Case #" << tt+1 << ": " << f[h][w] << endl;
	}
	return 0;	
}
