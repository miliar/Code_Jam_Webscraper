//For Future
//By JFantasy

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1005;

struct node {
	int x , v;
	double t;
} data[maxn];
int n , x , s , r , t;

void init() {
	memset( data , 0 , sizeof(data) );
	scanf( "%d%d%d%d%d" , &x , &s , &r , &t , &n );
	for ( int i = 0; i < n; i++ ) {
		int st , ed;
		scanf( "%d%d%d" , &st , &ed , &data[i].v );
		data[i].v += s;
		data[i].x = ed - st;
		x -= ed - st;
	}
	data[n].v = s;
	data[n++].x = x;
}

bool cmp( node a , node b ) {  
	if ( a.v != b.v ) return a.v < b.v;
	else return a.x < b.x;
}

void work( int cas ) {
	sort( data , data+n , cmp );
	double limit = t;
	int i = 0;
	while ( limit > 0 && i < n ) {
		if ( double(data[i].x)/double(data[i].v+r-s) <= limit ) {
			limit -= double(data[i].x)/double(data[i].v+r-s);
			data[i].t += double(data[i].x)/double(data[i].v+r-s);
			i++;
		} else {
			data[i].t += limit;
			limit = 0;
		}
	}
	double ans = 0;
	for ( int i = 0; i < n; i++ ) {
		ans += data[i].t + (data[i].x-data[i].t*(data[i].v+r-s))/double(data[i].v);
	}
	printf( "Case #%d: %.9lf\n" , cas , ans );
}

int main() {
	int cas , q = 0;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		init();
		work(++q);
	}
	return 0;
}
