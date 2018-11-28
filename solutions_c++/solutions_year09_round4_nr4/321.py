#include<stdio.h>
#include<math.h>
#define sqr( a) (( a) * ( a))

int n;

struct point {
	double x, y, r;

} P[ 40];

/*
point Circum_Center ( point &a, point &b, point &c) {
    point ret, ta = b - a, tb = c - a;
    double d = ( ta.x * tb.y - tb.x * ta.y) * 2.0;
    ret.x = ( tb.y * ( sqr( ta.x) + sqr( ta.y)) - ta.y * ( sqr( tb.x) + sqr( tb.y)) / d + a.x;
    ret.y = ( ta.x * ( sqr( tb.x) + sqr( tb.y)) - tb.x * ( sqr( ta.x) + sqr( ta.y)) / d + a.y;
    return ret;
} 
*/
double max ( double a, double b) {
	if ( a > b) return a;
	return b;
}
double min ( double a, double b) {
	if ( a < b) return a;
	return b;
}

double distance( point &a, point &b) {
	return sqrt( sqr( a.x - b.x) + sqr( a.y - b.y));
}


double prs( void) {
	if ( n == 1)
		return P[ 0].r;
	if ( n == 2) 
		return max( P[ 0].r, P[ 1].r);

	double ret = max( (distance( P[ 0], P[ 1]) + P[ 0].r + P[ 1].r) / 2.0, P[ 2].r);
	ret = min( ret, max( ( distance( P[ 0], P[ 2]) + P[ 0].r + P[ 2].r) / 2.0, P[ 1].r));
	ret = min( ret, max( ( distance( P[ 1], P[ 2]) + P[ 1].r + P[ 2].r) / 2.0, P[ 0].r));

	return ret;

}

int main( void) {

	int testnum;
	FILE *fin = fopen ( "input.txt", "rt");
	FILE *fout = fopen ( "output.txt", "wt");

	fscanf( fin, "%d", &testnum);

	for ( int testcase = 1; testcase <= testnum; testcase++) {
		
		fscanf( fin, "%d", &n);
		for ( int i = 0; i < n; i++) {
			int a, b, c;
			fscanf ( fin, "%d %d %d", &a, &b, &c);
			P[ i].x = a, P[ i].y = b, P[ i].r = c;
		}			

		fprintf( fout, "Case #%d: %lf\n", testcase, prs());

	}
	return 0;
}