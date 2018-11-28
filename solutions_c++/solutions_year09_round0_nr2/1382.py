#include <iostream>

using namespace std;

const int INF = 1000000000;

int area[128][128];
char labeled[128][128];
int h, w;


void getSink(int& r, int& c) {
	while (true) {
		int minH = min(
			min(r > 0 ? area[r-1][c] : INF,
				c > 0 ? area[r][c-1] : INF),
			min(c < w-1 ? area[r][c+1] : INF,
				r < h-1 ? area[r+1][c] : INF)
		);
		
		if (minH >= area[r][c]) {
			return;
		}
	
		if (r > 0 && area[r-1][c] == minH) {
			r--;
		} else if (c > 0 && area[r][c-1] == minH) {
			c--;
		} else if (c < w-1 && area[r][c+1] == minH) {
			c++;
		} else if (r < h-1 && area[r+1][c] == minH) {
			r++;
		} else {
			return;
		}
	}
}


int main() {
	int T;

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> h >> w;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> area[i][j];
				labeled[i][j] = ' ';
			}
		}
		
		char c = 'a';
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				int sr = i,
					sc = j;

				getSink(sr, sc);

				if (labeled[sr][sc] == ' ') {
					labeled[sr][sc] = c++;
				}
				
				labeled[i][j] = labeled[sr][sc];
			}
		}
		
		cout << "Case #" << t << ":" << endl;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w-1; j++) {
				cout << labeled[i][j] << " ";
			}
			cout << labeled[i][w-1] << endl;
		}
	}
}
