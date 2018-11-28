#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


int main () 
{
  freopen("input","r",stdin);
  freopen("output","w+",stdout);

  int tests;
  int N;
  
  scanf("%d", &tests);
  
  for (int test = 0; test < tests; ++test) 
  {    
	scanf("%d", &N);
	
	VPII a(N);
	
	REP(i,N)
	{
		cin >> a[i].X >> a[i].Y;		
	}

	int res = 0;

	REP(i,N) REP(j,i)
	{
		if(a[i].X == a[j].X && a[i].Y == a[j].X) continue;

		if(a[i].X == a[j].X)
			++res;
		else if(a[i].X < a[j].X)
		{
			if(a[i].Y >= a[j].Y)
				++res;
		}
		else
		{
			if(a[j].Y >= a[i].Y)
				++res;
		}
	}
	    
	printf("Case #%d: %d\n", (test+1) , res);
	fflush(stdout);
  }
};
