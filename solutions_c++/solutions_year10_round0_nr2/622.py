

#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int64;

const int
	MAXN = 1005;

int T , tc , N;
int64 val[MAXN];

int64 gcd( int64 a , int64 b ){
	if ( b == 0 ) return a;
	return gcd( b , a % b );
}

int main(){

	cin >> T;
	
	for ( tc = 1 ; tc <= T ; tc++ ){
	
		cin >> N;
		
		
		for ( int i = 0 ; i < N ; i++ ){
			cin >> val[i];
			//cout << val[i] << "\n";
		}

		sort( val , val + N );
		
		int64 small = val[0];
				
		for ( int i = 1 ; i < N ; i++ )
			val[i-1] = val[i] - val[i-1];
			
		N--;
		
		int64 maxd = val[0];
		
		for ( int i = 1 ; i < N ; i++ )
			maxd = gcd( maxd , val[i] );
		
		int64 mod = small % maxd;
		
		
		//cout << "small = " << small << "\n";
		//cout << "maxd = " << maxd << "\n";
		//cout << "mod = " << mod << "\n";
		
		
		int64 sol;
		
		if ( mod == 0 ) sol = 0;
		else sol = maxd - mod;
		
		cout << "Case #" << tc << ": " << sol << "\n"; 
		
	}
	

	return 0;
}
