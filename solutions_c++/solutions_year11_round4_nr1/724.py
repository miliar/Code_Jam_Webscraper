#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define OUT(t) cerr<<#t" = "<<t<<" ";
#define OLN()  cerr<<endl;

struct node {
	int s, e, v;
	double up;
}a[2000];

bool cmp( const node &a, const node &b ) {
	return a.v < b.v;
}

int main( ) {
	freopen( "D:\\GoogleCodeJam\\A\\A-small-attempt0.in", "r", stdin );
	freopen( "D:\\GoogleCodeJam\\A\\A-small-attempt0.out", "w", stdout );

	int re, ri = 1;
	int i;

	scanf( "%d", &re );
	while( re-- ) {
		int x, s, r, t, n;

		scanf( "%d%d%d%d%d", &x, &s, &r, &t, &n );
		int len = 0;
		for( i=0 ; i<n ; i++ ) {
			scanf( "%d%d%d", &a[i].s, &a[i].e, &a[i].v );
			a[i].up = 0;
			len += (a[i].e - a[i].s );
		}
		sort( a, a+n, cmp );

		double tt = t;
		double sum = 0;


		double tn = (x-len)/(double)r;
		if( tt>=tn ) {
			sum += (x-len)/(double)r;
			tt -= tn;
		} else {
			sum += tt;
			sum += ( x - len - tt*r )/ s ;
			tt = 0;
		}

		for( i=0 ; i<n ; i++ ) {
			double tn = ( a[i].e - a[i].s )/(double)( a[i].v + r );
			if( tn<tt ) {
				a[i].up = tn;
				tt -= tn;
				sum += tn;
			} else {
				a[i].up = tt;
				tt = 0;
				sum += a[i].up + ( a[i].e-a[i].s - a[i].up *  (double)( a[i].v + r ) ) / ( (double)a[i].v + s );
				i++; break;
			}
		}

		for(  ; i<n ; i++ ) {
			sum += (a[i].e-a[i].s) / (double)(a[i].v + s);
		}


		printf( "Case #%d: %lf\n", ri++, sum );
	}

	return 0;
}
