#include<algorithm>
#include<cstdio>
#include<vector>
#include<cmath>
#include<string>

using namespace std;
int xl, yl, A;

bool Read(){
	scanf( "%d%d%d", &xl, &yl, &A );
	return true;
}

int xx1, yy1, xx2, yy2;
double eps = 1e-6;

double rast( double x0, double y0, double x3, double y3 ){
	return pow( (x0 - x3)*(x0 - x3 ) + (y0 - y3)*(y0 - y3 ) , 0.5 );
}

double sqr(){
	double a, b, c;
	a = rast( 0, 0, xx1, yy1 );
	b = rast( 0, 0, xx2, yy2 );
	c = rast( xx1, yy1, xx2, yy2 );
	double p = (a + b +c )/2.0;
	return pow( p*(p-a)*(p-b)*(p-c), 0.5 );
}

int Solve(){
	for(xx1 = 0; xx1 <= xl; ++xx1){
		for(yy1 = 0; yy1 <= yl; ++yy1 ){
			for(xx2 = 0; xx2 <= xl; ++xx2){
				for(yy2 = 0; yy2 <= yl; ++yy2 ){
					if( abs( 2.0*sqr() - A*1.0 ) < eps )return 1;
				}
			}
		}
	}
	return 0;
}

void Write( int num, int ans ){
	if( ans == 1 )printf( "Case #%d: 0 0 %d %d %d %d\n", num, xx1, yy1, xx2, yy2 );
	else printf( "Case #%d: IMPOSSIBLE\n", num );
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n;
	scanf( "%d", &n );
	for(int i = 0; i < n; ++i){
		Read();
		Write( i+1, Solve() );
	}

	return 0;
}