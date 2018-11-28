#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen( "in", "r" , stdin );
	freopen( "out", "w", stdout );
	
	int n;
	cin >> n;
	int N, S, p;
	
	for ( int i = 1 ; i <= n ; i++) {
		cin >> N >> S >> p;									
		int temp = p-2;
		int minimum = p + (( temp <= 0 ) ? 0 : 2*temp );
		int a[N+1];
		int b[N+1];
		int c[N+1];
	
		for ( int j = 0 ; j < N ; j++ ) {
			cin >> a[j];
			b[j] = 0;
			c[j] = 0;
		
			if ( a[j] >= minimum ) {
				b[j] = 1;
			}
			
			if ( a[j] % 3 == 0 ) {
				if ( a[j]/3 >= p ) {
					c[j] = 1;
				}
			} else if ( a[j] % 3 == 1 ) {
				if ( (a[j]/3)+1 >= p ) {
					c[j] = 1;
				}
			} else {
				if ( (a[j]+1)/3 >= p ) {
					c[j] = 1;
				}
			}
			
			if ( a[j] == 29 or a[j] == 30 ) {
				b[j] = 0;
			}
			
//			cout << a[j] << " " << b[j] << " " << c[j] << endl;
		}
		
		int count = 0;
		int cnt = 0;
		for ( int k = 0 ; k < N ; k++ ) {
			if ( b[k] == 1 and c[k] == 0 ) {
				cnt++;
			}
			if ( c[k] == 1 ) {
				count++;
			}
		}
//		cout << S << "   " << cnt << " "<< count<< endl;
		
		cout << "Case #" << i <<": " ;
		if ( S >= cnt ) {
			cout << cnt + count << endl;
		} else {
			cout << S + count << endl;
		}			 
	}
}
