
#include <iostream>
#include <vector>

using namespace std;

void findnext(vector< vector<int> > v, int i, int j, int *rx, int *ry) {
	int min = 100000;
	*rx = -1;
	*ry = -1;
	
	int ni, nj;
	ni = i+1;
	nj = j;
	if( ni >= 0 && ni < v.size() && nj >= 0 && nj < v[0].size() ) {
		int alt = v[ni][nj];
		if( alt <= min ) {
			min = alt;
			*rx = ni;
			*ry = nj;
		}
	}
	ni = i;
	nj = j+1;
	if( ni >= 0 && ni < v.size() && nj >= 0 && nj < v[0].size() ) {
		int alt = v[ni][nj];
		if( alt <= min ) {
			min = alt;
			*rx = ni;
			*ry = nj;
		}
	}
	ni = i;
	nj = j-1;
	if( ni >= 0 && ni < v.size() && nj >= 0 && nj < v[0].size() ) {
		int alt = v[ni][nj];
		if( alt <= min ) {
			min = alt;
			*rx = ni;
			*ry = nj;
		}
	}
	ni = i-1;
	nj = j;
	if( ni >= 0 && ni < v.size() && nj >= 0 && nj < v[0].size() ) {
		int alt = v[ni][nj];
		if( alt <= min ) {
			min = alt;
			*rx = ni;
			*ry = nj;
		}
	}

	if( min >= v[i][j] ) {
		*rx = -1;
		*ry = -1;
	}
}

void fill(vector< vector<char> > &res, char c) {
	for(int i = 0; i < res.size(); i++) {
		for(int j = 0; j < res[i].size(); j++) {
			if( res[i][j] == '#' ) res[i][j] = c;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int H, W;
		cin >> H >> W;

		vector< vector<int> > v = vector< vector<int> >(H, vector<int>(W));
		vector< vector<char> > res = vector< vector<char> >(H, vector<char>(W, '-'));
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				int x;
				cin >> x;
				v[i][j] = x;
			}
		}
		
		cout << "Case #" << t+1 << ":" << endl;
		char ibasin = 'a';
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				int cx, cy;
				cx = i;
				cy = j;
				while(res[cx][cy] == '-' || res[cx][cy] == '#') {
					int x, y;
					findnext(v, cx, cy, &x, &y);
					if( x != -1 ) {
						res[cx][cy] = '#';
						cx = x;
						cy = y;
					}
					else {
						res[cx][cy] = ibasin++;
					}
				}
				fill(res, res[cx][cy]);
				cout << res[i][j];
				if(j != W-1) cout << " ";
			}
			cout << endl;
		}
	}
	
	return 0;
}


