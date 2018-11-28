#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin( "B.in" );
ofstream fout( "B.out" );
int test, n, s, arr[200], p;
int best[32][2], cnt = 1;
bool mark[200];

#define cin fin
#define cout fout

int main(){
	memset( best, -1, sizeof best );
	for( int i = 0; i <= 10; i++ )
		for( int j = i; j <= i + 2; j++ )
			for( int k = j; k <= i + 2; k++ ){
				int sup = ( k - i == 2 ) ? 1 : 0;
				//if( i + j + k <= 23 && i + j + k >= 21 )
				//	cout << i + j + k << ' ' << i << ' ' << j << ' ' << k << ' ' << sup << endl;
				best[i + j + k][sup] = max( best[i + j + k][sup], k );
			}
	/*for( int i = 2; i <= 30; i++ )
		while( best[i][0] > best[i][1] )
			cout << i << endl;
	*/
	for( cin >> test; test--; ){
		cin >> n >> s >> p;
		memset( mark, false, sizeof mark );
		for( int  i = 0; i < n; i++ )
			cin >> arr[i];
		/*for( int i = 0;i < n; i++ )
			cout << arr[i] << ' ' << best[arr[i]][0] << ' ' << best[arr[i]][1] << endl;
		*/
		int ret = 0;
		for( int i = 0; i < n; i++ )
			if( s && best[arr[i]][1] >= p && best[arr[i]][0] < p ){
				mark[i] = true;
				s--;
				ret++;
			}
		for( int i = 0; i < n; i++ )
			if( !mark[i] && s && best[arr[i]][1] >= p ){
				mark[i] = true;
				ret++;
				s--;
			}
		for( int i = 0; i < n; i++ )
			if( !mark[i] && best[arr[i]][0] >= p )
				ret++;
		cout << "Case #" << cnt++ << ": ";
		cout << ret << endl;
	}
	return 0;
}