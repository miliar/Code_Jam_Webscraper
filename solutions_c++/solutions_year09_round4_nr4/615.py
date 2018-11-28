
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
using namespace std;

struct point {
	int y,x;
};

vector<point> p;
vector<double> r;
double ans;

double getradius(point a, point b, double r1, double r2)
{
	return ( (sqrt( (double)(a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) ) + (double)r1 + (double)r2)/2.0 );

}

void process()
{
	if( p.size() == 1 ) {
		ans = r[0];
	}
	else if( p.size() == 2 ) {
		ans = 1000000000.0;
		ans = min( ans, getradius( p[0], p[1], r[0], r[1]) );
		ans = min( ans, max( r[0], r[1]) );
	}
	else {
		ans = 1000000000.0;
		ans = min( ans, max( getradius( p[0], p[1], r[0], r[1]) , r[2] ) );
		ans = min( ans, max( getradius( p[1], p[2], r[1], r[2]) , r[0] ) );
		ans = min( ans, max( getradius( p[2], p[0], r[2], r[0]) , r[1] ) );
	}
}

int main()
{
	freopen("D-small-attempt3.in", "rt", stdin);
	freopen("D.out","wt", stdout);
	int c;
	int n;
	cin>>c;
	for(int i=0; i<c; i++ ) {
		cin>>n;
		p.clear();
		r.clear();
		for( int j=0; j<n; j++ ) {
			point po;
			double rr;
			cin>>po.x>>po.y>>rr;


			p.push_back(po);
			r.push_back(rr);
		}


		cout<<"Case #"<<i+1<<": ";
		process();
		printf("%.6lf\n", ans);

	}
	return 0;
}