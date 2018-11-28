#include <iostream>

#define f(x,y) for (int x = 0; x < y; ++x)

#define T 105
#define H 105
#define W 105

using namespace std;

int t, h, w;

int adx[4] = {0, -1, 1, 0}, ady[4] = {-1, 0, 0, 1};

int alt[H][W];
int lab[H][W];
int labels;

int rec(int x, int y) {
	if (lab[y][x] != -1) return lab[y][x];

	int bx = x, by = y;
	f(i,4) if (x+adx[i] >= 0 && x+adx[i] < w && y+ady[i] >= 0 && y+ady[i] < h)
		if (alt[by][bx] > alt[y+ady[i]][x+adx[i]]) bx = x+adx[i], by = y+ady[i];
	
	if (bx == x && by == y) return lab[y][x] = labels++;
	
	return lab[y][x] = rec(bx, by);
}

int main() {
	cin >> t;
	
	f(counter,t) {
		cin >> h >> w;
		f(i,h) f(j,w) cin >> alt[i][j];
		
		f(i,h) f(j,w) lab[i][j] = -1;
		labels = 0;
		
		cout << "Case #" << (counter+1) << ":" << endl;
		f(i,h) {
			f(j,w) cout << (char) ('a' + rec(j,i)) << " ";
			cout << endl;
		}
	}

	return 0;
}

