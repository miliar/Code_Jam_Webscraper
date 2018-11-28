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

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int main()
{
	ifstream fin("B.in"); ofstream fout("B.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		string s;
		fin >> s;
		
		bool found = false;
		string d;
		FORR(i, 1, LEN(s)-1)
		{
			d += s[i];
			if (s[i] > s[i-1])
			{
				found = true;
				sort(ALL(d));
				FOR(j, SZ(d))
					if (d[j] > s[i-1])
					{
						swap(s[i-1], d[j]);
						break;
					}
				s.erase(i);
				s += d;
				break;
			}
		}

		if (!found)
		{
			s += "0";
			sort(ALL(s));
			FOR(i, LEN(s)) 
				if (s[i] > '0') 
				{
					swap(s[0], s[i]);
					break;
				}
		}

		fout << "Case #" << tt+1 << ": " << s << endl;
		cout << "Case #" << tt+1 << ": " << s << endl;
	}
	return 0;	
}
