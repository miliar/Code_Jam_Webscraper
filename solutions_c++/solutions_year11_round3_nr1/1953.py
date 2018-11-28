#include <iostream>
#include <vector>
#include <list>

using namespace std;

typedef list< pair< int, int > > CoordList;
typedef vector< CoordList::iterator > MapRow;
typedef vector< MapRow > Map;

int main (void) {
	int n;
	cin >> n;
	
	for (int prob = 1; prob <= n; ++prob) {
		int row, col;
		
		cin >> row >> col;

		CoordList worklist;
		CoordList::iterator invalid = worklist.end ();
		Map squares (row, MapRow (col, invalid));

		CoordList tracelist;
		tracelist.push_back (pair< int, int > (0, 0));
		tracelist.push_back (pair< int, int > (0, 1));
		tracelist.push_back (pair< int, int > (1, 0));
		tracelist.push_back (pair< int, int > (1, 1));

		for (int i = 0; i < row; ++i) {
			for (int j = 0; j < col; ++j) {
				char c;
				cin >> c;
				if (c == '#') {
					squares[i][j] = worklist.insert (worklist.end (), pair< int, int > (i, j));
				}
			}
		}
		
		bool good = true;
		while (good && not worklist.empty ()) {
			pair< int, int > corner = worklist.front ();

			for (CoordList::iterator it = tracelist.begin (); good && it != tracelist.end (); ++it) {
				int x = corner.first + it->first;
				int y = corner.second + it->second;
				if (x < row && y < col) {
					CoordList::iterator & square = squares[x][y];
					if (square == invalid) {
						good = false;
					} else {
						worklist.erase (square);
						square = it;
					}
				} else {
					good = false;
				}
			}
		}

		cout << "Case #" << prob << ':' << endl;

		if (good) {
			// print
			for (int i = 0; i < row; ++i) {
				for (int j = 0; j < col; ++j) {
					CoordList::iterator it = squares[i][j];
					if (it != invalid) {
						if (it->first == it->second) {
							cout << '/';
						} else {
							cout << '\\';
						}
					} else {
						cout << '.';
					}
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}	

	return 0;
}

