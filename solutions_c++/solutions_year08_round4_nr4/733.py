#include <iostream>

using namespace std;

char s[50009];
char s2[50009];

int main() {
	int cases;
	
	cin >> cases;
	for( int c = 1; c <= cases; ++c ) {
		int k;
		string ss;
		
		cin >> k >> ss;
		strcpy( s, ss.c_str() );
		
		int n = strlen(s);
		int p[5];
		for( int i =0 ; i < k; ++i ) {
			p[i] = i;
		}
		int res = 1000000000;
		do {
			for( int i = 0; i < n; i += k ) {
				for( int j = 0; j < k; ++j) {
					s2[i+j] = s[i+p[j]];
				}
			}
			int cnt = 1;
			for( int i = 1; i < n; ++i ) {
				if( s2[i] != s2[i-1] ) ++cnt;
			}
			res = min( res, cnt );
		} while( next_permutation( p, p+k ) );
		cout << "Case #" << c << ": " << res << endl;
	}
	return 0;
}
