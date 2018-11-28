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
	ifstream fin("s2.in"); ofstream fout("s2.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int a[2], p, hh1, mm1, hh2, mm2;
		fin >> p >> a[0] >> a[1];

		string s;
		multiset<pair<int,int>> A[2];
		deque<pair<int,int>> R[2];

		FOR(c, 2) FOR(i, a[c])
		{
			fin >> s; 
			s[2] = ' ';
			iss(s) >> hh1 >> mm1;

			fin >> s; 
			s[2] = ' ';
			iss(s) >> hh2 >> mm2;

			A[c].insert(make_pair(hh1 * 60 + mm1, hh2 * 60 + mm2 + p));
			R[c].push_back(make_pair(hh1 * 60 + mm1, hh2 * 60 + mm2 + p));
		}

		int res[2] = {0, 0};
		while (SZ(A[0]) > 0 && SZ(A[1]) > 0)
		{
			int c = (*A[0].begin() < *A[1].begin()) ? 0 : 1;
			++res[c];
			multiset<pair<int,int>>::iterator it = A[c].begin();
			while (it != A[c].end())
			{
				int rt = it->second;
				A[c].erase(it);
				c = 1 - c;
				it = A[c].lower_bound(make_pair(rt, 0));
			}
		}

		res[0] += SZ(A[0]);
		res[1] += SZ(A[1]);

		fout << "Case #" << tt+1 << ": " << res[0] << " " << res[1] << endl;
	}

	return 0;	
}
