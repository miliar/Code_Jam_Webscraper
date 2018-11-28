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

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int main()
{
	ifstream fin("s1.in"); ofstream fout("s1.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int ncnt, m;
		char ch[255];

		fin >> ncnt;
		fin.getline(ch, sizeof(ch));
		vector<string> names(ncnt);
		FOR(i, ncnt) 
		{
			fin.getline(ch, sizeof(ch));
			names[i] = ch;
		}

		fin >> m;
		fin.getline(ch, sizeof(ch));
		vector<string> queries(m);
		FOR(i, m) 
		{
			fin.getline(ch, sizeof(ch));
			queries[i] = ch;
		}

		const int inf = 12345678;

		vvi f(m+1, vi(ncnt, inf));

		FOR(i, ncnt) f[0][i] = 0;

		FORD(i, 1, m)
		{
			string& cq = queries[i-1];
			FOR(cj, ncnt)
			{
				if (cq == names[cj]) continue;
				FOR(pj, ncnt)
				{
					if (pj == cj)
						f[i][cj] = min(f[i][cj], f[i-1][pj]);
					else
						f[i][cj] = min(f[i][cj], f[i-1][pj] + 1);
				}
			}
		}

		int res = *min_element(ALL(f[m]));
		fout << "Case #" << tt+1 << ": " << res << endl;
	}
	return 0;	
}
