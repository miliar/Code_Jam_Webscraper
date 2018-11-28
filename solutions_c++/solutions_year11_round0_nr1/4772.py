#include <cstdio>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream IN( "input.txt" );
	ofstream OUT( "output.txt" );
	int n, a;
	IN >> n;
	for( int i = 0; i < n; i++ ){
		IN >> a;
		char b;
		int br = 0, po = 1, pb = 1;
		int so = 0, sb = 0, k;
		for( int j = 0; j < a; j++ ){
			IN >> b;
			if( b == 'O' ){
				IN >> k;
				int m = abs( k - po ) - so;
				if( m > 0 ){
					br+= m;
					sb+= m;
				}
				br++;
				sb++;
				so = 0;
				po = k;
			}
			else{
				IN >> k;
				int m = abs( k - pb ) - sb;
				if( m > 0 ){
					br+= m;
					so+= m;
				}
				br++;
				so++;
				sb = 0;
				pb = k;
			}
		}
		OUT << "Case #" << i+1 << ": " << br << endl;
	}
	return 0;
}