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

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <boost/regex.hpp>



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


bool found(const vector<char> &x, char a)
{
	for (vector<char>::const_iterator iter=x.begin(); iter!=x.end(); iter++)
	{
		if (a == *iter) return true;
	}
	return false;
}

void printvec(const vector<char> &x)
{
	for (vector<char>::const_iterator iter=x.begin(); iter!=x.end(); iter++)
	{
		cout << *iter << " ";
	}
	cout << endl;
}

int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		int num;
		char str[1000];

		//XXX  -- Read input --  XXX
		cin >> str;
		unsigned int map[256]={0};
		vector<char> seen;

		for(i=0;str[i];i++)
		{
			if (!found(seen, str[i]))
			seen.pb(str[i]);
		}
		//printvec(seen);

		unsigned long long int res=0, base;
		vector<char>::const_iterator iter;
		//assign values
		for (i=0,base=2, iter=seen.begin(); iter!=seen.end(); iter++,i++)
		{
			if(i==0)
			{
				map[*iter]=1;
			}
			else if(i==1)
			{
				map[*iter]=0;
			}
			else
			{
				map[*iter]=base;
				base++;
			}
		}

		//XXX  -- Process input --  XXX
		for(i=0;str[i];i++)
		{
			res=res*base+map[str[i]];
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %lld\n",testId, res);
	}

	return 0;
}
