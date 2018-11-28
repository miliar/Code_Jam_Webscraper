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
#define		MP	make_pair
#define		PB	push_back

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int main()
{
	ifstream fin("A.in"); ofstream fout("A.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int n;
		fin >> n;
		vi a(n);
		FOR(i, n)
		{
			string s;
			fin >> s;
			a[i] = 0;
			FOR(j, n) if (s[j] == '1') a[i] = j; 
		}
		int cnt = 0;
		while (1)
		{
			int idx = -1;
			FOR(i, n)
			{
				if (a[i] > i)
				{
					FORD(j, i+1, n-1)
					{
						if (a[j] < a[i])
						{
							idx = j;
							break;
						}
					}
				}

				if (idx > -1)
				{
					FORR(j, i+1, idx)
					{
						swap(a[j],a[j-1]);
						++cnt;
					}
					break;
				}
			}

			if (idx == -1) break;
		}
		fout << "Case #" << tt+1 << ": " << cnt << endl;
		cout << "Case #" << tt+1 << ": " << cnt << endl;
	}
	return 0;	
}
