#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>

using namespace std;

int ans , a , b;

void solve( int x )
{
	map<int,int> num;
	num.clear();
	int w = int(log(double(x))/log(10)) + 1;
	int p = 10 , q = 1;
	for ( int i = 1; i < w; i++ ) q *= 10;
	for ( int i = 1; i < w; i++ ) {
		int c = x/p + (x%p)*q;
		if ( x < c && c <= b && num[c] != 1 ) {
			ans++;
			num[c] = 1;
		}
		p *= 10;
		q /= 10;
	}
}

int main()
{
	int cas;
	scanf( "%d" , &cas );
	for ( int d = 1; d <= cas; d++ ) {
		ans = 0;
		scanf( "%d%d" , &a , &b );
		for ( int i = a; i <= b; i++ ) solve(i);
		printf( "Case #%d: %d\n" , d , ans );
	}
	return 0;
}
