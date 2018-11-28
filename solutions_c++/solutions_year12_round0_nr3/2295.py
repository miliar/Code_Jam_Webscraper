#include <iostream>
#include <cstdio>
#include <set>
#include <utility>
#include <cmath>

using namespace std;

int main()
{
	int T, A, B;
	int digits, count, x, y;
	set< pair< int, int > > data;
	pair< int, int > p;
	int hash[] = { 0, 0, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };
	scanf("%d",&T);

	for( int a = 1; a <= T; a ++ ) {
		scanf("%d %d",&A,&B);
		count = 0;

		digits = 0;
		x = A;
		data.clear();
		while( x != 0 ) {
			x = x / 10;
			digits ++;
		}
		for( int b = A; b <= B; b ++ ) {
			x = b;
			for( int c = 1; c < digits; c ++ ) {
				y = (x % 10) * hash[digits];
				y += (x / 10);
				if( b < y && y <= B ) {
					p.first = b;
					p.second = y;
					data.insert(p);
					//cout << b << " : " << c << " : " << y << endl;
				}
				x = y;
			}
		}
		printf("Case #%d: %d\n",a,data.size());
	}
	return 0;
}
