#include<cstdio>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<algorithm>
#include<map>
#include<set>

#define gmin( a, b) (( a) < ( b) ? ( a) : ( b))
#define gmax( a, b) (( a) > ( b) ? ( a) : ( b))
#define MAX 1000000

using namespace std;

int n, m;
struct Inf {
	int h, w;
	int type; // 0 = bird, 1 = not, 2= unknown;
};

vector < Inf > Know, Question;

void inp( void) {

	scanf( "%d", &n);

	char Tmp[ 100];

	Know = vector < Inf > ( n);
	
	for ( int i = 0; i < n; i++) {

		scanf( "%d %d %s", &Know[ i].h, &Know[ i].w, Tmp);
		if ( Tmp[ 0] == 'B') {
			Know[ i].type = 0;
		} else {
			scanf( "%s", Tmp);
			Know[ i].type = 1;
		}

	}

	scanf( "%d", &m);

	Question = vector < Inf > ( m);

	for ( int i = 0; i < m; i++) {
		scanf( "%d %d", &Question[ i].h, &Question[ i].w);
	}

}

void prs( void) {

	int minw, minh, maxw, maxh;
	int underw, overw, underh, overh;

	minw = MAX; maxw = 0;
	minh = MAX; maxh = 0;

	underw = 0; overw = MAX + 1;
	underh = 0; overh = MAX + 1;

	for ( int i = 0; i < n; i++) {
		if ( Know[ i].type == 0) {
			minw = gmin( minw, Know[ i].w);
			minh = gmin( minh, Know[ i].h);
			maxw = gmax( maxw, Know[ i].w);
			maxh = gmax( maxh, Know[ i].h);
		}
	}
	for ( int i = 0; i < n; i++) {
		if ( Know[ i].type == 1) {
			if ( minw <= Know[ i].w && Know[ i].w <= maxw) {
				if ( Know[ i].h < minh) underh = gmax( underh, Know[ i].h);
				if ( Know[ i].h > maxh) overh = gmin( overh, Know[ i].h);
			}
			if ( minh <= Know[ i].h && Know[ i].h <= maxh) {
				if ( Know[ i].w < minw) underw = gmax( underw, Know[ i].w);
				if ( Know[ i].w > maxw) overw = gmin( overw, Know[ i].w);
			}
		}
	}

	for ( int i = 0; i < m; i++) {
		if ( minh <= Question[ i].h && Question[ i].h <= maxh && minw <= Question[ i].w && Question[ i].w <= maxw) {
			Question[ i].type = 0;
		} else if ( Question[ i].h <= underh || Question[ i].h >= overh || Question[ i].w <= underw || Question[ i].w >= overw) {
			Question[ i].type = 1;
		} else 
			Question[ i].type = 2;

		if ( Question[ i].type == 2) {
			for ( int j = 0; j < n; j++) {
				if ( Know[ j].h == Question[ i].h && Know[ j].w == Question[ i].w && Know[ j].type == 1) {
					Question[ i].type = 1;
				}
			}
		}
	}
}

void outp( int test_num) {

	printf( "Case #%d:\n", test_num);

	for ( int i = 0; i < m; i++) {
		if ( Question[ i].type == 0) 
			printf( "BIRD\n");
		else if ( Question[ i].type == 1)
			printf( "NOT BIRD\n");
		else
			printf( "UNKNOWN\n");
	}

}

int main( void) {

	int tmp;

	scanf( "%d", &tmp);

	for ( int i = 0; i < tmp; i++) {
		inp();
		prs();
		outp( i + 1);
	}

	return 0;
}
