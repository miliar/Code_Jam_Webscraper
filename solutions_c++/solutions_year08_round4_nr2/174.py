#include<cstdio>
#include<string.h>
#include<vector>
using namespace std;
#define N 100000
#define gmin( a, b) ( ( a) < ( b) ? ( a) : ( b))
#define gabs( a) ( (a) < 0 ? -(a) : (a))

int n, m, s, ans;

void inp( void) {

	scanf( "%d %d %d", &n, &m, &s);

}

void prs( int number) {

	int i, j, k, l, p, tmp;

	ans = 0;

	for ( i = 1; i <= n; i++) {

		for ( j = s / i; j <= m; j++) {

			if ( s <= i * j ) {

				tmp = i * j - s;

				if ( tmp == 0) {
					ans = 1;
					printf( "Case #%d: %d %d %d %d %d %d\n", number, 0, 0, i, 0, 0, j);
					return ;
				}
				for ( k = j; k >= 0; k--) {
					if ( (double)tmp / k > (double)i) break;
					if ( tmp % k == 0) {
						ans = 1;
						printf( "Case #%d: %d %d %d %d %d %d\n", number, 0, 0, i, k, tmp / k, j);
						return;
					}
				}
			}

		}

	}	

}

int main( void) {

	freopen( "input.txt", "r", stdin);
	freopen( "output.txt", "w", stdout);

	int testn;

	scanf( "%d", &testn);

	for ( int i = 0; i < testn; i++) {

		inp();
		prs(i + 1);
		if ( !ans) printf( "Case #%d: IMPOSSIBLE\n", i + 1);

	}
	fclose(stdin);
	return 0;
}



