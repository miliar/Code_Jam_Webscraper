#include<iostream>
#include<vector>
#include<string>
using namespace std;


int main(){
	int N;
	cin >> N;
	for( int i = 0; i< N; i++ ){
		long long int n,m,X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;

		long long int A[m];
		long long int AA[n];
		for( int j=0; j < m; j++ ){
			cin >> A[j];
			AA[j] = A[j];
		}
		
		long long int B[n];
		fill_n( B, n, 0 );
		for( int j = 0; j < n; j++ ){
			//cout << A[j%m] << " ";
			AA[j] = A[j%m];
			
			B[j] = 1;
			for( int k = 0; k < j; k++ ){
//				cout << j << " " << k << " : " << A[j%m] << " > " << AA[k] << endl;
				if( A[j%m] > AA[k] ){
					B[j] += B[k];
					B[j] %= 1000000007LL;
				}
			}
			
			A[j%m] = (((X * A[j%m]) % Z) + ((Y * (j+1))%Z)) % Z;
		}
		//cout << endl;

		long long int ans = 0;
		for( int j = 0; j < n; j++ ){
			//cout << B[j] << " ";
			ans += B[j];
			ans %= 1000000007LL;
		}
		//cout << endl;

		cout << "Case #" << (i+1) << ": " << ans << endl;
	}
}
