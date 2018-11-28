#include<cstdio>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<algorithm>
#include<map>
#include<set>

using namespace std;

int n, m, ans;
int D[ 8][ 8];
int M[ 8], Ch[ 9];
int L[ 8][ 2];

void inp( void) {

	scanf( "%d", &n);

	for ( int i = 0; i < n; i++){ 
		for ( int j = 0; j < n; j++) {
			D[ i][ j] = 0;
		}
	}

	for ( int i = 0; i < n - 1; i++) {
		int a, b;
		scanf( "%d %d", &a, &b);
		D[ a - 1][ b - 1] = D[ b - 1][ a - 1] = 1;
	}

	for ( int i = 0; i < n; i++) Ch[ i] = 0;

	scanf( "%d", &m);

	for ( int i = 0; i < m - 1; i++) {
		scanf( "%d %d", &L[ i][ 0], &L[ i][ 1]);
	}

	ans = 0;

}

void prs( int d) {
	
	if ( n == d) {

		int ch = 0;
		for ( int i = 0; i < m - 1; i++) {
			if ( D[ M[ L[ i][ 0]]][ M[ L[ i][ 1]]] == 0) ch = 1;
		}

		if ( ch == 0) ans = 1;

	} else {

		for ( int i = 0; i < n; i++) {
			if ( !Ch[ i]) {
				M[ d] = i; Ch[ i] = 1;
				prs( d + 1);
				Ch[ i] = 0;
			}
		}
	}
}

void outp( int test_num) {

	printf( "Case #%d: ", test_num);

	if ( ans) printf( "YES");
	else printf( "NO");


	printf( "\n");

}

int main( void) {

	int tmp;

	scanf( "%d", &tmp);

	for ( int i = 0; i < tmp; i++) {
		inp();
		prs(0);
		outp( i + 1);
	}

	return 0;
}
