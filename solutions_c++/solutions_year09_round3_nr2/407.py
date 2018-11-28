
/* Author :: Yash */
#include <vector>
#include <list>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <deque>
#include <fstream>
#include <stack>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define PP pop()
#define EM empty()
#define INF 1000000000
#define PF push_front
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define V(x) vector< x >
#define Debug false
#define PRINT(x)        cout << #x << " " << x << endl
#define LET(x,a) 	    __typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define SZ(x) 		x.size();
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define D(N) 		int N
#define S(N)		scanf("%d",&N)

typedef pair<int,int>  PI;
typedef pair<int,PI>   TRI;
typedef V( int )       VI;
typedef V( PI  )       VII;
typedef V( string )    VS;
typedef long long      LL;

double x,y,z,vx,vy,vz;
#define sqr(x) (x)*(x)

double calc(double t) {

	double a = sqr(x + vx*t);
	double b = sqr(y + vy*t);
	double c = sqr(z + vz*t);
	return sqrt(a+b+c);
}


inline double tsearch(double lo, double hi) {

	if( fabs( lo-hi ) < 1e-9 ) return (lo+hi)/2;
	double left = ( lo*2 + hi ) / 3.0;
	double righ = (lo + hi*2 ) / 3.0;
	
	if( calc( left ) > calc( righ ) ) 
		return tsearch( left, hi );
	else
		return tsearch( lo, righ );

}	


int main() {
	
	int kases; S(kases);
	REP(kk,kases) {
		
		int n;S(n);	
		double a,b,c,a1,b1,c1;
		x = y = z = vx= vy = vz = 0;

		REP(i,n) {

			cin >> a >> b >> c >> a1 >> b1 >> c1;
			x += a; vx += a1;
		        y += b; vy += b1;
			z += c;	vz += c1;
		}
		x /= (n * 1.);y /= (n * 1.);z /= (n * 1.);
		vx /= (n * 1.);vy /= (n * 1.);vz /= (n * 1.);
	
		double ans = tsearch(0,100000.000);
		double d = calc(ans);

		printf("Case #%d: %lf %lf\n",kk+1,calc(ans),ans);	
		
	}	
	return 0;
}


