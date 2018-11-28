#include <iostream>
#include <vector>
using namespace std;
int main( void )
{
	int C;
	cin >> C;
	for( int CC = 1; CC <= C; CC ++ ){
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector<int> X(N), V(N);
		for( int i = 0; i < N; i ++ )
			cin >> X[i];
		for( int i = 0; i < N; i ++ )
			cin >> V[i];

		vector<int> kind(N);
		for( int i = 0; i < N; i ++ ){
			kind[i] = ( (long long)X[i] + (long long)T * (long long)V[i] >= (long long)B ) ? 1 : 0;
		}

		int NGs = 0;
		int j = 0;
		long long res = 0;
		for( int i = N - 1; i >= 0 && j < K; -- i ){
			if( kind[i] == 0 )
				NGs ++;
			else{
				res += NGs;
				j ++;
			}
		}
		if( j >= K )
			printf( "Case #%d: %lld\n", CC, res );
		else
			printf( "Case #%d: %s\n", CC, "IMPOSSIBLE" );
	}
	return 0;
}
