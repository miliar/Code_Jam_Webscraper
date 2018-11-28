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

double solve( double a, double b, double c )
{
	double r = b*b + c*c - a*a;
	r /= 2*b*c;
	return acos( r );
}

double intersect( double x1, double y1, double x2, double y2, double r1, double r2 )
{
	double cdis = hypot( x1-x2, y1-y2 );
	if( cdis + min(r1,r2) - 1e-9 <= max(r1,r2) )
		return M_PI*min(r1,r2)*min(r1,r2);
	
	double A1 = 2*solve( r2, r1, cdis );
	double A2 = 2*solve( r1, r2, cdis );
	
	return 1./2*( r1*r1*( A1-sin(A1) ) + r2*r2*( A2-sin(A2) ) );
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin ); freopen("D-small-attempt0.out", "w", stdout );
	//freopen("A-small-attempt1.in", "r", stdin ); freopen("A-small-attempt1.out", "w", stdout );
	//freopen("A-small-attempt2.in", "r", stdin ); freopen("A-small-attempt2.out", "w", stdout );
	
	//freopen("A-large.in", "r", stdin ); freopen("A-large.out", "w", stdout );
	
	int T;
	cin>>T;
	for(int t=1; t <= T; t++)
	{
		int n, m;
		cin>>n>>m;
		vector<int> px(n), py(n);
		vector<int> qx(m), qy(m);
		for(int i=0; i < n; i++)
		cin>>px[i]>>py[i];
		for(int i=0; i < m; i++)
		cin>>qx[i]>>qy[i];
		
		printf("Case #%d: ", t );
		for(int i=0;  i < m; i++)
		{
			double r1 = hypot( px[0]-qx[i], py[0]-qy[i] );
			double r2 = hypot( px[1]-qx[i], py[1]-qy[i] );
			
			double sol =intersect( px[0], py[0], px[1], py[1], r1, r2 );
			printf("%.10lf%c", sol, i+1==m ? '\n' : ' ' );
		}
		
		
		
		
	}
	
	return 0;
}
