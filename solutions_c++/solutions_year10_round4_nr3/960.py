#include <string>
#include <set>
#include <iostream>
#include <vector>

using namespace std;

int main ( ) {

	int cases;
	cin >> cases; 
	for ( int caseno = 1; caseno <= cases; caseno++) {
		
		int bacteria [102][102];
		memset ( bacteria, 0, sizeof(bacteria));

		int r ;
		cin >> r;
		for ( int i = 0; i < r ; i ++ ) {
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for ( int a = x1+1; a <= x2+1; a ++ ){
				for ( int b =  y1+1; b <= y2+1; b++ ) {
					bacteria [b][a] = 1;
				}
			}
		}
		int result = 0;
		for ( int r = 0 ; r < 100000; r ++ ) {
			int cos = false;
			for ( int x = 101; x >=  1; x -- ) {
				for ( int y = 101; y >= 1; y-- ) {
					if ( bacteria [y][x] ) {
						cos = true;
					}
					if ( bacteria[y-1][x] && bacteria[y][x-1]  )
					{ 
						bacteria[y][x] = 1;
					}
					if ( (!bacteria[y-1][x]) && (! bacteria[y][x-1]) ) {
						bacteria[y][x] = 0; 
					}
				}
			}
			if (!cos ) {
				result = r;
				break;
			}
		}
			
		cout << "Case #" << caseno << ": " << result << endl;
	}

	return 0;

}