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

int main()
{
	ifstream fin("a.in"); ofstream fout("a.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int n;
		i64 A, B, C, D, x0, y0, M;
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		
		vvi a(3, vi(3, 0));

		i64 X = x0, Y = y0;
		++a[X%3][Y%3];
		FORD(i, 1, n-1)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			++a[X%3][Y%3];
		}

		i64 ans = 0;

		FOR(i, 9) FORD(j, i, 8) FORD(k, j, 8)
		{
			int i1 = i / 3, j1 = i%3; 
			int i2 = j / 3, j2 = j%3; 
			int i3 = k / 3, j3 = k%3; 
			if ((i1+i2+i3)%3 != 0 || (j1+j2+j3)%3 != 0) continue;
			if (i == j && j == k && a[i1][j1] < 3) continue;
			if (i == j && a[i1][j1] < 2) continue;
			if (j == k && a[i2][j2] < 2) continue;
			if (a[i1][j1] == 0 || a[i2][j2] == 0 || a[i3][j3] == 0) continue;

			if (i < j && j < k)
			{
				ans += a[i1][j1] * a[i2][j2] * a[i3][j3];
				continue;
			}

			if (i == j && j == k)
			{
				ans += a[i1][j1] * (a[i1][j1] - 1) * (a[i1][j1] - 2) / 6;
				continue;
			}

			if (i == j)
			{
				ans += a[i1][j1] * (a[i1][j1] - 1) / 2 * a[i3][j3];
				continue;
			}

			if (j == k)
			{
				ans += a[i2][j2] * (a[i2][j2] - 1) / 2 * a[i1][j1];
				continue;
			}
		}

		fout << "Case #" << tt+1 << ": " << ans << endl;
	}
	return 0;	
}
