//For Future
//By JFantasy

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const double eps = 1e-9;

const int maxn = 205;
const int maxp = 1000005;

struct node {
	int x , y;
} data[maxn];
int n , d , sum;

bool cmp( node a , node b ) {  return a.x < b.x;  }

double getmin( double a , double b ) {  return a<b?a:b;  }

void init() {
	scanf( "%d%d" , &n , &d );
	sum = 0;
	for ( int i = 0; i < n; i++ ) {
		scanf( "%d%d" , &data[i].x , &data[i].y );
		sum += data[i].y;
	}
	sort( data , data+n , cmp );
}

double pos[maxp];
bool check( double key ) {
	int t = 0;
	for ( int i = 0; i < n; i++ ) {
		for ( int j = 1; j <= data[i].y; j++ ) {
			pos[t++] = data[i].x;
		}
	}
	pos[0] -= key;
	for ( int i = 1; i < t; i++ ) {
		if ( pos[i-1] < pos[i] ) {
			if ( pos[i] - pos[i-1] >= d ) pos[i] -= getmin( key , pos[i]-pos[i-1]-d );
			else {
				if ( pos[i] + key - pos[i-1] >= d ) pos[i] = pos[i-1] + d;
				else return 0;
			}
		} else {
			if ( pos[i] + key - pos[i-1] >= d ) pos[i] = pos[i-1] + d;
			else return 0;
		}
	}
	return 1;
}

void work( int cas ) {
	double lower = 0 , upper = double(d)*double(sum);
	while ( upper - lower > eps ) {
		double mid = ( lower + upper ) / 2.0;
		if ( check(mid) ) upper = mid;
		else lower = mid;
	}
	printf( "Case #%d: %.6lf\n" , cas , lower );
}

int main() {
	int cas , t = 0;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		init();
		work(++t);
	}
	return 0;
}
