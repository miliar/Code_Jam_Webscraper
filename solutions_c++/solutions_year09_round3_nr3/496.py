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

int fact(int n)
{
    int ret=1;
    FOR(i,1,n)
    {
        ret*=i;
    }

    return ret;
}


int cell[12000];
int rel[120];

void printarr(const int *p, int n)
{
	for(int i=0; i<n; i++) cout << p[i] << " ";
	cout << endl;
}
int eval(int p, int q, const int *c, const int *r)
{
	int i,j,k;
	int c1[p+2];

	//printarr(r,q);

	for(i=0;i<p+2; i++) c1[i]=c[i];

	int b=0;
	for(i=0;i<q;i++)
	{
		int cnt;

		//mark r[i] ] released
		c1[ r[i] ] = 0;

		//find bribe needed leftside
		for(cnt=0, j=r[i]-1; c1[j] != 0; j--)
			cnt++;

		b+=cnt;
		//find bribe needed right side
		for(cnt=0, j=r[i]+1; c1[j] != 0; j++)
			cnt++;
		b+=cnt;
	}

	return b;
}

int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		int p,q;
		cin >> p >> q;

		cell[0]=0;
		for(i=1;i<=p;i++)
			cell[i]=1;
		cell[p+1]=0;

		//XXX  -- Read input --  XXX
		for(i=0; i<q; i++)
		{
			cin >> rel[i];
		}

		//XXX  -- Process input --  XXX
		int ans=INT_MAX;
		int numComb=fact(q);
		for(int comb=1; comb <= numComb; comb++)
        {
			int tmp;
            next_permutation(rel, rel+q);

			tmp=eval(p, q, cell, rel);

			if(tmp<ans)
				ans=tmp;
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %d\n",testId,ans);
	}

	return 0;
}
