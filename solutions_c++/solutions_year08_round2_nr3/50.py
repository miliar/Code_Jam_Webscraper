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

void bst_add(int idx, int cnt, vi& f) { while(idx<SZ(f)){f[idx]+=cnt;idx+=(idx&-idx);} }
int bst_get(int idx, vi& f){ int res=0; while(idx>0){res+=f[idx];idx-=(idx&-idx);} return res; }
int bst_get(int a, int b, vi& f) { return bst_get(b, f) - bst_get(a-1, f); }

int main()
{
	ifstream fin("c.in"); ofstream fout("c.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int K, n;
		fin >> K >> n;
		vector<int> d(n);
		FOR(i, n) fin >> d[i];

		vector<int> b(K+1, 0);
		FORD(i, 1, K) bst_add(i, 1, b);

		vector<int> a(K+1, 0);
		int pos = 1;
		FORD(i, 1, K)
		{
			int skip = i;
			int rght = bst_get(pos, K, b);
			if (skip > rght)
			{
				skip -= rght;
				pos = 1;
			}
			skip %= K-i+1;
			if (skip == 0) skip = K-i+1;

			rght = K;
			while (pos < rght)
			{
				int m = (rght + pos) / 2;
				int cnt = bst_get(pos, m, b);
				if (cnt >= skip)
				{
					rght = m;
				}
				else
				{
					skip -= cnt;
					pos = m+1;
				}
			}

			a[pos] = i;
			bst_add(pos, -1, b);
		}

		fout << "Case #" << tt+1 << ":";
		FOR(i, n) fout << " " << a[d[i]];
		fout << endl;
	}
	return 0;	
}
