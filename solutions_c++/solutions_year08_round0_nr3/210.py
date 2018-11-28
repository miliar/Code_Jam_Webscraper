#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <set>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <list>
#include <map>
#include <queue>
#include <cassert>
#include <algorithm>
#include <math.h>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPV(i,ar) for(int i=0;i<int(ar.size());i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define EACH(it,mp) for(__typeof(mp.begin()) it(mp.begin());it!=mp.end();it++)
#define GI ({int y;scanf("%d",&y);y;})
#define sz size()
#define pb push_back
#define INF (1<<30)
#define LINF (1e18)
#define sor(ar) sort(ar.begin(),ar.end())

typedef long long int LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

double f,R,t,r,g;
#define EPS (1e-9)

bool is_inside( const double& x , const double& y ){
	return hypot(x,y) <= R + EPS;	
}

double intersect( double p ){	
	assert( p < R + EPS);
	return sqrt( R*R - p*p + EPS);
}

double get_angle( double x, double y ) {
	if( !y ) return M_PI_2;
	else if( !x ) return 0;
	return atan(y/x);
}
int main(){
	int T = GI;
	freopen("swatter.out","w",stdout);
	FOR(tt,1,T){
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		R -= t;
		R -= f;		
		double inc = g + 2*r;
		double box = g - 2*f;
		
		double flyarea = 0;
		int cnt = 0;
		if( box > EPS && R > 0 )  {
			
		for(double x = r + f; x < R ; x += inc ){
			double maxY = intersect( x );
			for(double y = r + f; y <= maxY + EPS; y += inc ){				
				if( is_inside(x+box,y+box) ) cnt++;					
				else {
					double tx = x, ty = y;
					const bool top = is_inside(x,y+box);
					const bool right = is_inside(x+box,y);					
					if( top ) tx = intersect(y+box);
					if( right ) ty = intersect(x+box);					
					
					const double xdash = intersect( ty );
					const double ydash = intersect( tx );
					double sq = 0;
					if( top ) sq += ( tx - x)*( ydash - y );
					if( right ) sq += (xdash - x)*(ty-y);
					if( top && right ) sq -= (tx-x)*(ty-y);
					/*
					#define dbg(x) cout << #x <<" -> " << x <<" ";
					#define dbge(x) cout << #x <<" -> " << x << endl;
					dbg(tx);dbge(ty);
					dbg(tx);dbge(ydash);
					dbg(xdash);dbge(ty);
					cout <<" --> "<< endl;					
					*/
					
					const double angle = get_angle( tx , ydash ) - get_angle( xdash , ty );
					const double sectorarea = .5*R*R*angle; assert( sectorarea >= -EPS );
					const double sub1 = .5 * tx * ( ydash - ty );assert( sub1 >= -EPS );
					const double sub2 = .5 * ty * ( xdash - tx );assert( sub2 >= -EPS );					
					const double add = (sectorarea - sub1 - sub2);assert( add >= -EPS );
					flyarea += add + sq;
				}
			}
		}
		}
		
		flyarea += ( box > EPS ? box : 0 ) * ( box > EPS ? box : 0 ) * cnt;
		R += t; R += f;
		double totalarea = M_PI*R*R;
		printf("Case #%d: %.6lf\n",tt,1-(flyarea*4)/totalarea);
		
	}
	return 0;
}