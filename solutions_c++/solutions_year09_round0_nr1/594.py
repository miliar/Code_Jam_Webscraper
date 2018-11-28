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
	int N, L, D;
	fin >> L >> D >> N;

	vector<string> w(D);
	FOR(i, D) fin >> w[i];

	FOR(i, N)
	{
		vector<vector<int> > B(L, vector<int>(256, 0));

		string p;
		fin >> p;

		for (int idx = 0, j = 0; j < L; ++j)
		{
			if (isalpha(p[idx]))
			{
				B[j][p[idx]] = 1;
				++idx;
				continue;
			}
			for (++idx; isalpha(p[idx]); ++idx)
			{
				B[j][p[idx]] = 1;
			}
			++idx;
		}

		int ans = 0;
		FOR(j, D)
		{
			int ok = true;
			FOR(k, L)
			{
				ok = ok && B[k][w[j][k]];
				if (!ok) break;
			}
			if (ok) ++ans;
		}

		fout << "Case #" << i+1 << ": " << ans << endl;
		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;	
}
