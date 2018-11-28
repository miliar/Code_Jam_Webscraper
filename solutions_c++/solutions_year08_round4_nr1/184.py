#include<cstdio>
#include<vector>
using namespace std;
#define N 10001
#define MAX 999999
#define gmin( a, b) ( ( a) < ( b) ? ( a) : ( b))

int n, v;
int Change[ N + 2], Gate[ N + 2];
int Interior[ N + 2][ 2];

void inp( void) {

	scanf( "%d %d", &n, &v);

	int a, b;

	for ( int i = 1; i <= ( n - 1) / 2; i++) {
		scanf( "%d %d", &a, &b);
		Gate[ i] = a; // 1 and 0 or
		Change[ i] = b;
		Interior[ i][ 0] = Interior[ i][ 1] = MAX;
	}

	for ( int i = (n - 1) / 2 + 1; i <= n; i++) {

		scanf( "%d", &a);

		Interior[ i][ a] = 0;
		Interior[ i][ !a] = MAX;

	}

}

void prs( void) {

	int i, j;

	for ( i = ( n - 1) / 2; i >= 1; i--) {

		if ( Gate[ i] == 0) {
			Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 0]);
			Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 0]);
			Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 1]);
			Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 1]);
		} else {
			Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 0]);
			Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 0]);
			Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 1]);
			Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 1]);
		}

		if ( Change[ i] == 1) {	
			if ( Gate[ i] == 1) { // OR
				Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 0] + 1);
				Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 0] + 1);
				Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 1] + 1);
				Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 1] + 1);
			} else {
				Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 0] + 1);
				Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 0] + 1);
				Interior[ i][ 0] = gmin( Interior[ i][ 0], Interior[ i * 2][ 0] + Interior[ i * 2 + 1][ 1] + 1);
				Interior[ i][ 1] = gmin( Interior[ i][ 1], Interior[ i * 2][ 1] + Interior[ i * 2 + 1][ 1] + 1);
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
		prs();
		if ( Interior[ 1][ v] == MAX) 
			printf( "Case #%d: IMPOSSIBLE\n", i + 1);
		else 
			printf( "Case #%d: %d\n", i + 1, Interior[ 1][ v]);

	}
	fclose(stdin);
	return 0;
}

