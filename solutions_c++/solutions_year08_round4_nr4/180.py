#include<cstdio>
#include<string.h>
#include<vector>
using namespace std;
#define N 6
#define MAX 50005
#define gmin( a, b) ( ( a) < ( b) ? ( a) : ( b))

int n, l, c, ans;
int A[ N], Ch[ N];
char Str[ MAX];
char New[ MAX];

void inp( void) {

	scanf( "%d %s", &n, Str);

	l = strlen( Str);

	ans = l;

	for ( int i = 0; i < n; i++) Ch[ i] = 0;

}

void prs( int d, int x) {

	A[ d] = x;

	if ( d == n) {		
		for ( int i = 0; i < l; ) {
			for( int j = 0; j < n; j++) {
				New[ i + j] = Str[ i + A[ j + 1]];
			}
			i += n;
		}
		c = 1;
		for ( int i = 1; i < l; i++) {
			if ( New[ i] != New[ i - 1]) c++;
		}

		ans = gmin( ans, c);
	} else {
		for ( int i = 0; i < n; i++) {
			if ( Ch[ i] == 0) {
				Ch[ i] = 1;
				prs( d + 1, i);
				Ch[ i] = 0;
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
		prs(0, 0);
		printf( "Case #%d: %d\n", i + 1, ans);

	}
	fclose(stdin);
	return 0;
}


