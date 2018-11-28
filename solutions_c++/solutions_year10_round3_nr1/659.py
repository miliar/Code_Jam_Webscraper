#include<iostream>
#include<algorithm>
using namespace std;
int test ;
int a[ 1000 ], b[ 1000 ];
void doit(){
	int n;
	cin>>n;
	for( int i = 0; i < n; ++i ){
		cin>>a[ i ]>>b[ i ];
	}
	for( int i = 0; i < n -1 ; ++i ){
		for( int j = 0; j < n - 1; ++j )if( a[ j ] > a[ j + 1 ] ){
			swap( a[ j ], a[ j + 1 ] );
			swap( b[ j ], b[ j + 1 ] );
		}
	}
	int ret = 0;
	for( int i = 0; i < n; ++i ){
		for( int j = i + 1; j < n; ++j ){
			if( b[ j ] < b[ i ] ){
				ret++;	
			}
		}
	}
	cout<<"Case #"<<test++<<": "<<ret<<endl;
}
int main(){
	
	test = 1;
	int T;
	cin>>T;
	for( int i = 1; i <= T; ++i ){
		doit();
	}
}
