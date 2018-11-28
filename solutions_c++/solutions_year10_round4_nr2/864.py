#include <iostream>

using namespace std;

const int N = 3000;

int a[N];

int n, m;

int work( int low, int high ){

	int ans = 0;
	
	bool f = true;
	for( int i = low; i <= high; i++ ){
		if( a[i] > 0 ){
			f = false;
		}
	}

	if( f == true ){
		ans = 0;
	}
	else{
		if( high == low + 1 ){
			ans = 1;
		}
		else{
			int mid = ( low + high - 1 ) / 2;
			ans = 1;
			for( int i = low; i <= high; i++ ){
				if( a[i] > 0 ){
					a[i]--;
				}
			}
			ans += work( low, mid ) + work( mid + 1, high );
		}
	}

	return ans;
}

int main(){

	int Tc;
	
	freopen( "B-small-attempt2.in.txt", "r", stdin );
	freopen( "b-small-out.txt", "w", stdout );

	scanf( "%d", &Tc );
	

	for( int tc = 1; tc <= Tc; tc++ ){

		scanf( "%d", &n );

		m = ( 1 << n );
		
//		cout<<"m="<<m<<endl;

		for( int i = 0; i < m; i++ ){
			scanf( "%d", a + i );
		}

		for( int i = 0; i < m; i++ ){
			a[i] = n - a[i];
		}
		
		int tmp;
		for( int i = 0; i < m - 1; i++ ){
			scanf( "%d", &tmp );
		}
/*		
		for( int i = 0; i < m; i++ ){
			cout<<a[i]<<" ";
		}
		cout<<endl;
*/
		printf( "Case #%d: %d\n", tc, work( 0,  m - 1 ) );
	}

	return 0;
}


