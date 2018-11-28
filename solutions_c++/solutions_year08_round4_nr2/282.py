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

i64 cross(i64 x1, int y1, int x2, int y2)
{
	return x1 * y2 - x2 * y1;
}

i64 abs64(i64 a) { return (a >= 0) ? a : -a; }


int main()
{
	ifstream fin("b.in"); ofstream fout("b.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		i64 n, m, A;
		fin >> n >> m >> A;

		bool fnd = false;
		FOR(x1, n+1)
		{
			FOR(y1, m+1)
			{
				FOR(x2, n+1)
				{
					FOR(y2, m+1)
					{
						if (abs64(cross(x1, y1, x2, y2)) == A)
						{
							fout << "Case #" << tt+1 << ": 0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
							fnd = true;
							break;
						}
					}
					if (fnd) break;
				}
				if (fnd) break;
			}
			if (fnd) break;
		}

		if (!fnd) fout << "Case #" << tt+1 << ": IMPOSSIBLE" << endl;
	}
	return 0;	
}
