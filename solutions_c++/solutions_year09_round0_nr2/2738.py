#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

typedef uint32_t	altitudes_t;
typedef uint32_t	region_t;

int solve( const altitudes_t *map, int H, int W, int L ) {
	int R = W-1;
	int B = H-1;
	region_t r = 1;
	vector<region_t> index( L );
	vector<region_t> region( L );
	for ( int i = 0, y = 0; y < H; y++ ) {
		for ( int x = 0; x < W; x++ ) {
			altitudes_t min = map[i];
			int dir = 0;
			if ( 0 < y && map[i-W] < min ) { min = map[i-W]; dir = 1; }
			if ( 0 < x && map[i-1] < min ) { min = map[i-1]; dir = 2; }
			if ( x < R && map[i+1] < min ) { min = map[i+1]; dir = 3; }
			if ( y < B && map[i+W] < min ) { min = map[i+W]; dir = 4; }

			if ( !region[i] ) {
				if ( dir == 0 ) region[i] = index[r] = r++;
				if ( dir == 1 ) region[i] = region[i-W];
				if ( dir == 2 ) region[i] = region[i-1];
				if ( dir == 3 ) {
					if ( region[i+1] ) region[i] = region[i+1];
					else region[i+1] = region[i] = index[r] = r++;
				}
				if ( dir == 4 ) region[i+W] = region[i] = index[r] = r++;
			}
			else {
				if ( dir == 1 ) index[region[i]] = region[i-W];
				if ( dir == 2 ) index[region[i]] = region[i-1];
				if ( dir == 3 ) {
					if ( !region[i+1] ) region[i+1] = region[i];
					else index[region[i]] = region[i+1];
				}
				if ( dir == 4 ) region[i+W] = region[i];
			}
			i++;
		}
	}
	for ( int i = 1; i < r; i++ ) {
		if ( index[i] == i ) continue;
		int j = i;
		while ( index[j] != j ) j = index[j];
		index[i] = j;
	}
	int n = 0;
	for ( int i = 1; i < r; i++ ) {
		if ( index[i] <= n ) continue;
		int diff = index[i] - n;
		for ( int j = i; j < r; j++ ) {
			if ( n < index[j] ) index[j] -= diff;
		}
		n++;
	}
	for ( int i = 0, y = 0; y < H; y++ ) {
		for ( int x = 0; x < W; x++ ) {
			cout << (char)( 'a' + index[region[i++]] );
			if ( x < R ) cout << " ";
		}
		cout << endl;
	}
	return n;
}

int main( int ac, char *av[] ) {
	int num;
	cin >> num;
	for ( int i = 0; i < num; i++ ) {
		cout << "Case #" << (i+1) << ":" << endl;
		int h, w;
		cin >> h;
		cin >> w;
		int l = h * w;
		vector<altitudes_t> map( l );
		for ( int i = 0, y = 0; y < h; y++ ) {
			for ( int x = 0; x < w; x++ ) {
				cin >> map[i++];
			}
		}
		solve( &map[0], h, w, l );
	}
}

