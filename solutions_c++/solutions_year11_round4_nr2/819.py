#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("B-small-attempt1.in");
ofstream fout("B-small-attempt1.out");
#define cin fin
#define cout fout

string inp[20];
int t, r, c, d, test = 1;

inline int getVal( char a ) {
	return a - '0' + d;
}

int main() {
	for( cin >> t; t--; ) {
		cin >> r >> c >> d;
		getline( cin, inp[0] );
		for( int i = 0; i < r; i++ ) {
			getline( cin, inp[i] );
		}
		int res = 0;
		int mx = min( r, c );
		for( int k = 3; k <= mx; k++ ) {
			for( int i = 0; i <= r - k; i++ ) {
				for( int j = 0; j <= c - k; j++ ) {
					int a = 0, b = 0, c = 0, d = 0;
					int mid = k / 2;
					for( int l = 0; l < mid; l++ ) {
						for( int m = 0; m < k; m++ ) {
							a += (mid - l) * getVal(inp[i + l][j + m]);
							b += (l + 1) * getVal(inp[i + l + (k + 1) / 2][j + m]);
							
							c += (mid - l) * getVal(inp[i + m][j + l]);
							d += (l + 1) * getVal(inp[i + m][j + l + (k + 1) / 2]);
						}
					}
					if( a - mid * getVal(inp[i][j]) - mid * getVal(inp[i][j + k - 1]) == b - mid * getVal(inp[i + k - 1][j]) - mid * getVal(inp[i + k - 1][j + k - 1]) && 
						c - mid * getVal(inp[i][j]) - mid * getVal(inp[i + k - 1][j]) == d - mid * getVal(inp[i][j + k - 1]) - mid * getVal(inp[i + k - 1][j + k - 1]) )
						 res = max( res, k );
				}
			}
		}
		cout << "Case #" << test++ << ": ";
		if( res == 0 )
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}