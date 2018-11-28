//DS includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>

//Other Includes
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define oo 					(int)13e7
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define ull 					unsigned long long
#define ll 						long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb( z ) 				push_back( z )
#define gcd					__gcd
using namespace std;

#define type double
//find position of px py w.r.t to x1,y1, x2,y2
int relativeCCW(type x1, type y1,  type x2, type y2,	  type px, type py)
{
	x2 -= x1;
	y2 -= y1;
	px -= x1;
	py -= y1;
	type ccw = px * y2 - py * x2;
	if (ccw == 0) {
	    ccw = px * x2 + py * y2;
	    if (ccw > 0) {
		px -= x2;
		py -= y2;
		ccw = px * x2 + py * y2;
			if (ccw < 0) {
		    	ccw = 0;
			}
	    }
	}
	return (ccw < 0) ? -1 : ((ccw > 0) ? 1 : 0);
}

bool linesIntersect(	type x1, type y1,type x2, type y2,
									type x3, type y3,type x4, type y4 )
{
	return ((relativeCCW(x1, y1, x2, y2, x3, y3) *
		 relativeCCW(x1, y1, x2, y2, x4, y4) <= 0)
		&& (relativeCCW(x3, y3, x4, y4, x1, y1) *
		    relativeCCW(x3, y3, x4, y4, x2, y2) <= 0)) ;
}

int main()
{
	
	//freopen("A-small-attempt0.in", "r", stdin ); freopen("A-small-attempt0.out", "w", stdout );
	//freopen("A-small-attempt1.in", "r", stdin ); freopen("A-small-attempt1.out", "w", stdout );
	//freopen("A-small-attempt2.in", "r", stdin ); freopen("A-small-attempt2.out", "w", stdout );
	
	freopen("A-large.in", "r", stdin ); freopen("A-large.out", "w", stdout );
	
	int t;
	cin>>t;
	for(int T=1; T <= t; T++)
	{
		int n;
		cin>>n;
		vector< pair<int,int> > a;
		for(int i=0; i < n; i++)
		{
			int x, y; cin>>x>>y;
			a.pb( make_pair( x, y ) );
		}
		sort( all( a ) );
		
		int sol = 0;
		for(int i=0; i < n; i++)
		for(int j=i+1; j < n; j++)
		if( linesIntersect( a[i].first, 0, a[i].second, 100, a[j].first, 0, a[j].second, 100 ) )
		{
			sol++;
		}
		printf("Case #%d: %d\n", T, sol );
	}
	
	return 0;
}
