#include <cstdio>
#include <cmath>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

const double pi = 2 * acos(0.0);

double f, R, t, r, g, rad;

double dist(double x1, double y1, double x2, double y2) {
	double dx = x1 - x2;
	double dy = y1 - y2;
	return sqrt(dx * dx + dy * dy);
}

double luas3(double x1, double y1, double x2, double y2, double x3, double y3) {
	double a = dist(x1,y1,x2,y2);
	double b = dist(x1,y1,x3,y3);
	double c = dist(x2,y2,x3,y3);
	double s = (a + b + c) / 2;
	return sqrt(s * (s-a) * (s-b) * (s-c));
}

double segment(double x1, double y1, double x2, double y2) {
	double alpha = abs(atan(y1/x1) - atan(y2/x2));
	double sector = alpha * 0.5 * rad * rad;
	return sector - luas3(0,0,x1,y1,x2,y2);
}

double area(double x, double y) {
	double ax = x, ay = y;
	double bx = x, by = y+g;
	double cx = x+g, cy = y;
	double dx = x+g, dy = y+g;

	if ( dist(0,0,dx,dy) <= rad ) return g * g;
	else if ( dist(0,0,bx,by) <= rad && dist(0,0,cx,cy) <= rad ) {
		double bdx = sqrt(rad*rad - by*by), bdy = by;
		double cdx = cx, cdy = sqrt(rad*rad - cx*cx);
		return g * g - (luas3(bdx,bdy,cdx,cdy,dx,dy) - segment(bdx,bdy,cdx,cdy));
	}
	else if ( dist(0,0,bx,by) <= rad ) {
		double bdx = sqrt(rad*rad - by*by), bdy = by;
		double acx = sqrt(rad*rad - ay*ay), acy = ay;
		return g * g - (luas3(bdx,bdy,acx,acy,cx,cy) + luas3(bdx,bdy,cx,cy,dx,dy) - segment(bdx,bdy,acx,acy));
	}
	else if ( dist(0,0,cx,cy) <= rad ) {
		double abx = ax, aby = sqrt(rad*rad - ax*ax);
		double cdx = cx, cdy = sqrt(rad*rad - cx*cx);
		return g * g - (luas3(abx,aby,cdx,cdy,bx,by) + luas3(bx,by,cdx,cdy,dx,dy) - segment(abx,aby,cdx,cdy));
	}
	else {
		double abx = ax, aby = sqrt(rad*rad - ax*ax);
		double acx = sqrt(rad*rad - ay*ay), acy = ay;
		return luas3(abx,aby,acx,acy,ax,ay) + segment(abx,aby,acx,acy);
	}
}

int main()
{
	int ncase;
	scanf( "%d", &ncase );

	FOR(tcase,1,ncase) {
		scanf( "%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g );
		
		g -= f + f; t += f; r += f; rad = R - t;
		if ( g <= 0 || rad <= 0 ) { printf( "Case #%d: %.6lf\n", tcase, 1.0 ); continue; }
		
		double ans = 0;
		bool found = true;
		for ( int i = 0; found; i++ ) {
			found = false;
			for ( int j = 0; ; j++ ) {
				double px = r + i * (g + r + r);
				double py = r + j * (g + r + r);
				if ( dist(0,0,px,py) >= rad ) break;
				ans += area(px, py);
				found = true;
			}
		}
		
		printf( "Case #%d: %.6lf\n", tcase, 1.0 - (ans * 4.0 / (pi * R * R)) );
		fprintf( stderr, "Case #%d: %.6lf\n", tcase, 1.0 - (ans * 4.0 / (pi * R * R)) );
	}
	
	return 0;
}
