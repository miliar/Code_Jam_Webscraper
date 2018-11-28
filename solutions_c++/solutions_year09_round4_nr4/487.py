#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <math.h>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for(int (a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))


#define IMAX 30000000
#define EPS 1e-7

bool lineIntersect( double x[], double y[], double r[] )
{
    double n[2]; n[0] = y[3] - y[2]; n[1] = x[2] - x[3];
    double denom = n[0] * ( x[1] - x[0] ) + n[1] * ( y[1] - y[0] );
    if( fabs( denom ) < EPS ) return false;
    double num = n[0] * ( x[0] - x[2] ) + n[1] * ( y[0] - y[2] );
    double t = -num / denom;
    r[0] = x[0] + t * ( x[1] - x[0] );
    r[1] = y[0] + t * ( y[1] - y[0] );
    return true;
}

double circle3pts( double x[], double y[], double r[] )
{
    double lix[4], liy[4];
    lix[0] = 0.5 * ( x[0] + x[1] ); liy[0] = 0.5 * ( y[0] + y[1] );
    lix[1] = lix[0] + y[1] - y[0];  liy[1] = liy[0] + x[0] - x[1];
    lix[2] = 0.5 * ( x[1] + x[2] ); liy[2] = 0.5 * ( y[1] + y[2] );
    lix[3] = lix[2] + y[2] - y[1];  liy[3] = liy[2] + x[1] - x[2];
    if( !lineIntersect( lix, liy, r ) ) return -1.0;
    return sqrt(
        ( r[0] - x[0] ) * ( r[0] - x[0] ) +
        ( r[1] - y[0] ) * ( r[1] - y[0] ) );
}

double dist( double ax, double ay, double bx, double by )
{
    return sqrt( ( ax - bx ) * ( ax - bx ) + ( ay - by ) * ( ay - by ) );
}


int main()
{   
	int t, n;
	int x[100], y[100], r[100];
		    
	cin >> t;
	
    RP(test, t)
    {
		cin >> n;
		RP(i, n) cin >> x[i] >> y[i] >> r[i];
		
		double res = 0;
		if (n == 1)
		{
			res = r[0];
		}
		else if (n == 2)
		{
			res = (r[0] > r[1])? r[0] : r[1];
		}
		if (n == 3)
		{
			double d = dist(x[0], y[0], x[1], y[1]) + r[0] + r[1];
			d <?= dist(x[2], y[2], x[1], y[1]) + r[2] + r[1];
			d <?= dist(x[2], y[2], x[0], y[0]) + r[2] + r[0];
			
			res = d/2;
		}
		
		printf("Case #%d: %lf\n", test+1, res);
	}
    
    return 0;
}
