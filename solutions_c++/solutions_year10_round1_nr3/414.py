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
#include <string.h>
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



int win[2][31][31];

int func(int a, int b, int pl)
{
	//cout << "func : " << a << " " << b << " " << pl << endl;
	
	/*if(a==0)
		return -1;
	if(b==0)
		return +1;
	*/
	if(a <= 30 && b <= 30 && win[pl][a][b]!=-1)
	{
		return win[pl][a][b];
	}
	
	if(a==b)
	{
		if(a <= 30 && b <= 30)
			win[pl][a][b]=-1;
		return -1;
	}

	int d, w1=1, w2=1, w3=1;
	if(a > b)
	{
		d = a/b;
		
		//two options or three options??
		if(a-b*d != 0)
		w1 = func(a-b*d, b, 1-pl);
		
		if(d-1>0)
			w2 = func(a-b*(d-1), b, 1-pl);

		if(d-2>0)
			w3 = func(a-b*(d-2), b, 1-pl);

		if(w1 == -1 || w2 == -1 || w3 == -1)
			w1=1;
		else
			w1=-1;

		if(a <= 30 && b <= 30)
			win[pl][a][b]=w1;
	}
	else
	{
		d = b/a;
		
		//two options or three options??
		if(b-a*d != 0)
			w1 = func(a, b-a*d, 1-pl);
		
		if(d-1>0)
			w2 = func(a, b-a*(d-1), 1-pl);

		if(d-2>0)
			w3 = func(a, b-a*(d-2), 1-pl);

		if(w1 == -1 || w2 == -1 || w3 == -1)
			w1=1;
		else
			w1=-1;

		if(a <= 30 && b <= 30)
			win[pl][a][b]=w1;	
	}

	return w1;
}

int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	cin >> nTests;
	memset(win, -1, sizeof(win));
	for(testId=1;testId<=nTests;testId++)
	{
		int a1, a2, b1, b2;

		//XXX  -- Read input --  XXX
		cin >> a1 >> a2 >> b1 >> b2;

		//XXX  -- Process input --  XXX

		int a, b, tot=0, w;
		for(a=a1;a<=a2;a++)
		for(b=b1;b<=b2;b++)
		{
			w=func(a,b, 0);
			if(w==1)
				tot++;
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %d\n", testId, tot);
	}

	return 0;
}
