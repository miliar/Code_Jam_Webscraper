#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <iostream>

using namespace std;

const int p1 = 1;
const int p2 = 1 << 1;
const int pAny = p1 | p2;
int a[4][4];

int main()
{
	freopen( "data.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	
	int t;
	cin >> t;
	for(  int k = 0; k < t; k++ ) {
		bool isComplete = true;

		for( int i = 0; i < 4; i++ ) {
			string s;
			cin >> s;
			for( int j = 0; j < 4; j++ ) {
				if( s[j] == 'X' ) {
					a[i][j] = p1;
				} else if( s[j] == 'O' ) {
					a[i][j] = p2;
				} else if( s[j] == 'T' ) {
					a[i][j] = pAny;
				} else {
					isComplete = false;
					a[i][j] = 0;
				}
			}
		}

		int res = 0;
		int local = pAny;
		for( int i = 0; i < 4; i++ ) {
			local &= a[i][i];
		}
		res |= local;
		local = pAny;
		for( int i = 0; i < 4; i++ ) {
			local &= a[3-i][i];
		}
		res |= local;

		for( int i = 0; i < 4; i++ ) {
			local = pAny;
			for( int j = 0; j < 4; j++ ) {
				local &= a[i][j];
			}
			res |= local;	
		}
		
		for( int i = 0; i < 4; i++ ) {
			local = pAny;
			for( int j = 0; j < 4; j++ ) {
				local &= a[j][i];
			}
			res |= local;	
		}

		if( res & p1 ) {
			printf( "Case #%d: X won\n", k + 1 );
		} else if( res & p2 ) {
			printf( "Case #%d: O won\n", k + 1 );
		} else if( isComplete ) {
			printf( "Case #%d: Draw\n", k + 1 );
		} else {
			printf( "Case #%d: Game has not completed\n", k + 1 );
		}
	}



	return 0;
}