#include <iostream>
#include <utility>
#include <list>
using namespace std;

int main() {
    int T, H, W;
    cin >> T;
    int di[] = { -1, 0, 0, 1};
    int dj[] = { 0, -1, 1, 0};
    for ( int Case = 0; Case < T; Case++ ) {
	cin >> H >> W;
	int map[H][W];
	char assign[H][W];
	for ( int i = 0; i < H; i++ ) {
	    for ( int j = 0; j < W; j++ ) {
		cin >> map[i][j];
		assign[i][j] = 'a' - 1;
	    }
	}

	char current = 'a';
	for ( int i = 0; i < H; i++ ) {
	    for ( int j = 0; j < W; j++ ) {
		if ( assign[i][j] >= 'a' ) continue;

		list< pair<int,int> > flow;

		flow.push_back( make_pair(i, j) );

		int ci = i, cj = j;
		char to_be_assign = 'a' - 1;
		while ( true ) {
		    int min = map[ci][cj];
		    int minci,mincj;
		    for ( int k = 0; k < 4; k++ ) {
			int newci = ci + di[k];
			int newcj = cj + dj[k];
			if ( ci + di[k] < 0 || ci + di[k] >= H ||
			     cj + dj[k] < 0 || cj + dj[k] >= W ) {
			    continue;
			}
			if ( map[newci][newcj] < min ) {
			    min = map[newci][newcj];
			    minci = newci;
			    mincj = newcj;
			}
		    }
		    if ( min < map[ci][cj] ) {
			ci = minci;
			cj = mincj;
			if ( assign[minci][mincj] >= 'a' ) {
			    to_be_assign = assign[minci][mincj];
			    break;
			} else {
			    flow.push_back( make_pair(ci, cj) );
			}
		    } else {
			break;
		    }
		}

		if ( to_be_assign == 'a' - 1 ) {
		    to_be_assign = current;
		    current++;
		}
		list< pair<int,int> >::iterator it;
		//cout << flow.size() << endl;
		for ( it = flow.begin(); it != flow.end(); it++ ) {
		    assign[(*it).first][(*it).second] = to_be_assign;
		}
	    }
	}

	cout << "Case #" << Case+1 << ":" << endl;
	for ( int i = 0; i < H; i++ ) {
	    for ( int j = 0; j < W; j++ ) {
		cout << char(assign[i][j]);
		if ( j == W - 1 ) {
		    cout << endl;
		} else {
		    cout << " ";
		}
	    }
	}
    }
    return 0;
}
