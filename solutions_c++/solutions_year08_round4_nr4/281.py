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

int rle(string& s)
{
	int res = 1;
	FOR(i, LEN(s)-1) if (s[i] != s[i+1]) ++res;
	return res;
}

void perm(string& s, string& d, vector<int>& p)
{
	d = s;
	int m = LEN(s) / SZ(p);
	FOR(i, m)
	{
		int iii = i * SZ(p);
		FOR(j, SZ(p)) d[iii+j] = s[iii+p[j]]; 
	}
}

int main()
{
	ifstream fin("d.in"); ofstream fout("d.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int k;
		string s;
		fin >> k >> s;

		vector<int> p(k);
		FOR(i, k) p[i] = i;

		string d;
		int ans = LEN(s);

		do 
		{
			perm(s, d, p);
			ans = min(ans, rle(d));
		} while(next_permutation(ALL(p)));

		fout << "Case #" << tt+1 << ": " << ans << endl;
	}
	return 0;	
}
