#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>



//#define INCLUDE_LP

#ifdef INCLUDE_LP
	#include "lp_lib.h"
#else
	#if defined (__GNUC__) && (__GNUC__ <= 2)
	#include <hash_map>
	#include <hash_set>
	#else
	//#include <ext/hash_map>
	//#include <ext/hash_set>
	using namespace __gnu_cxx;
	#endif
#endif



using namespace std;

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
//#include <boost/regex.hpp>



#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1e17



map<pair<int, int>, bool> *m, *m2, *tmp;


int main()
{
	int i,j,k,l,n;
	int testId, nTests;

	m = new map<pair<int,int>, bool>;
	m2 = new map<pair<int,int>, bool>;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		(*m).clear();
		(*m2).clear();

		int num, x1, y1, x2, y2;
		int x, y;
		cin >> num;

		
		map<pair<int,int>, bool>::iterator iter;

		//XXX  -- Read input --  XXX
		for(i=0; i<num; i++)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			for (x=x1; x<=x2; x++)
			for (y=y1; y<=y2; y++)
				(*m)[make_pair(x,y)] = true;
		}

		//XXX  -- Process input --  XXX
		int sec;
		for(sec=0; ;sec++)
		{
			if( (*m).empty() )
				break;
			(*m2).clear();

			for(iter=(*m).begin(); iter!=(*m).end(); iter++)
			{
				int cx, cy;
				cx=(iter->first).first;
				cy=(iter->first).second;
				if( ( (*m).find(make_pair(cx-1, cy)) != (*m).end() ) ||
				    ( (*m).find(make_pair(cx, cy-1)) != (*m).end() ) )
				{
					(*m2)[make_pair(cx,cy)] = true;
				}
				if( (*m).find(make_pair(cx+1, cy-1)) != (*m).end() )
				{
					(*m2)[make_pair(cx+1,cy)] = true;
				}
			}

			tmp=m;
			m=m2;
			m2=tmp;
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %d\n",testId, sec);
	}

	return 0;
}
