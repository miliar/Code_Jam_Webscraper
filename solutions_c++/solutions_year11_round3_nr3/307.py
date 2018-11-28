#include <iostream>
#include <cstdio>
using namespace std;

int N, L, H;
int F[100];

bool CanIt( int K ) {
	for( int i=0; i<N; i++ ) {
		if( F[i]%K != 0 && K%F[i] != 0 ) return false;
	}
	return true;
}

int main() {
	freopen( "C_Small.in", "r", stdin );
	freopen( "C_Small.out", "w", stdout );

	int TC;
	scanf( "%d", &TC );

	for( int TCC=1; TCC<=TC; TCC++ ) {
		scanf( "%d %d %d", &N, &L, &H );

		for( int i=0; i<N; i++ ) scanf( "%d", &F[i] );
		
		bool is_no = true;
		cout << "Case #" << TCC << ": ";
		for( int i=L; i<=H; i++ ) {
			if( CanIt( i ) ) {
				cout << i << endl;
				is_no = false;
				break;
			}
		}
		if( is_no ) cout << "NO" << endl;
	}
}