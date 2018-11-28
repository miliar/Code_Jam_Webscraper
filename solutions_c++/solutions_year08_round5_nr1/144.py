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
		map<int,set<int> > hor, ver;
		int L;
		fin >> L;
		int x = 0, y = 0;
		int dir = 1;
		FOR(i, L)
		{
			string s;
			int M;
			fin >> s >> M;
			FOR(j, M)
			{
				FOR(k, LEN(s))
				{
					if (s[k] == 'F')
					{
						if (dir == 0)
						{
							hor[x].insert(y);
							++x;
						} else if (dir == 2)
						{
							--x;
							hor[x].insert(y);
						} else if (dir == 1)
						{
							ver[y].insert(x);
							++y;
						} else
						{
							--y;
							ver[y].insert(x);
						}
					}
					else
					{
						if (s[k] == 'L')
							dir = ((dir + 1) & 3);
						else
							dir = ((dir + 3) & 3);
					}
				}
			}
		}

		set<pair<int,int> > pts;

		for (map<int,set<int> >::iterator itX = hor.begin(); itX != hor.end(); ++itX)
		{
			int x = itX->first;
			set<int>& st = itX->second;
			int ii = 0, pry = 0;
			for (set<int>::iterator itY = st.begin(); itY != st.end(); ++itY, ++ii)
			{
				int& y = *itY;
				if (ii > 0 && (ii&1)==0)
				{
					FORD(yyy, pry, y-1) pts.insert(make_pair(x, yyy));
				}
				pry = y;
			}
		}

		for (map<int,set<int> >::iterator itY = ver.begin(); itY != ver.end(); ++itY)
		{
			int y = itY->first;
			set<int>& st = itY->second;
			int ii = 0, prx = 0;
			for (set<int>::iterator itX = st.begin(); itX != st.end(); ++itX, ++ii)
			{
				int& x = *itX;
				if (ii > 0 && (ii&1)==0)
				{
					FORD(xxx, prx, x-1) pts.insert(make_pair(xxx, y));
				}
				prx = x;
			}
		}

		fout << "Case #" << tt+1 << ": " << SZ(pts) << endl;
	}
	return 0;	
}
