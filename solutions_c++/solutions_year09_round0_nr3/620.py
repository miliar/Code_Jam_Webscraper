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
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int main()
{
	ifstream fin("C.in"); ofstream fout("C.out");
	char buf[512];
	fin.getline(buf,512);
	int T;
	iss(buf) >> T;
	string pat = "welcome to code jam";
	int L = LEN(pat);
	FOR(tt, T)
	{
		fin.getline(buf,512);
		int n = (int)strlen(buf);
		if (n == 0) ++n;
		vvi f(n, vi(L, 0));
		FOR(i, n) FOR(j, L)
		{
			if (i > 0) f[i][j] = f[i-1][j];
			if (buf[i] == pat[j])
			{
				if (j == 0)
					++f[i][j];
				else if (i > 0)
					f[i][j] += f[i-1][j-1];
			}
			f[i][j] %= 10000;
		}

		oss ostr;
		if (f[n-1][L-1] < 1000) ostr << 0;
		if (f[n-1][L-1] < 100) ostr << 0;
		if (f[n-1][L-1] < 10) ostr << 0;
		ostr << f[n-1][L-1];

		fout << "Case #" << tt+1 << ": " << ostr.str() << endl;
		cout << "Case #" << tt+1 << ": " << ostr.str() << endl;
	}
	return 0;	
}
