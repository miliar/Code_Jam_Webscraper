#include <iostream>
#include <vector>
#include <set>
#include <cstring>

using namespace std;

const int dr[] = {-1,0,0,1};
const int dc[] = {0,-1,1,0};

int alt[105][105];
int label[105][105];
set<int> diff_alts;
char mapp[100];

int main() {
	int cases;

	cin >> cases;
	for( int caseid = 0; caseid < cases; ++caseid ) {
		int rows, cols;
		cin >> rows >> cols;
		diff_alts.clear();
		for( int r = 0; r < rows; ++r ) {
			for( int c = 0; c < cols; ++c ) {
				cin >> alt[r][c];
				diff_alts.insert( alt[r][c] );
			}
		}
		//
		int cur_label = 0;
		for( set<int>::const_iterator cur_alt = diff_alts.begin(); cur_alt != diff_alts.end(); ++cur_alt ) {
			for( int r = 0; r < rows; ++r ) {
				for( int c = 0; c < cols; ++c ) {
					if( alt[r][c] == *cur_alt ) {
						int min_neighbour_alt = 66666;
						int min_neighbour_index = -1;
						for( int i = 0; i < 4; ++i ) {
							int r2 = r+dr[i];
							int c2 = c+dc[i];
							if( 0 <= r2 && r2 < rows && 0 <= c2 && c2 < cols ) {
								if( alt[r2][c2] < alt[r][c] ) {
									if( alt[r2][c2] < min_neighbour_alt ) {
										min_neighbour_alt = alt[r2][c2];
										min_neighbour_index = i;
									}
								}	
							}
						}
						if( min_neighbour_index != -1 ) {
							label[r][c] = label[r+dr[min_neighbour_index]][c+dc[min_neighbour_index]];
						} else {
							label[r][c] = cur_label++;
						}
					}
				}
			}
		}
		// output
		cout << "Case #" << caseid+1 << ":\n";
		char cur_char = 'a';
		memset( mapp, 0, sizeof(mapp) );
		for( int r = 0; r < rows; ++r ) {
			for( int c = 0; c < cols; ++c ) {
				if( mapp[label[r][c]] == 0 ) {
					mapp[label[r][c]] = cur_char;
					++cur_char;
				}
			}
		}
		for( int r = 0; r < rows; ++r ) {
			for( int c = 0; c < cols; ++c ) {
				if( c > 0 ) cout << ' ';
				cout << mapp[label[r][c]];
			}
			cout << endl;
		}
	}
	return 0;
}
