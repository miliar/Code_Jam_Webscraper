#include <iostream>

using namespace std;


int T, H, W;
int cells[100][100];
char cmap[100][100];

char colorCell(int h, int w, char color) {

	if(cmap[h][w])
		return cmap[h][w];

	//North, West, East, South
	int la, lh, lw;

	la = cells[h][w];
	lh = h; lw = w;
	//North
	if(h - 1 >= 0 && cells[h - 1][w] < la) {
		la = cells[h - 1][w];
		lh = h - 1;
		lw = w;
	}
	//West
	if(w - 1 >= 0 && cells[h][w - 1] < la) {
		la = cells[h][w - 1];
		lh = h;
		lw = w - 1;
	}
	//East
	if(w + 1 < W && cells[h][w + 1] < la) {
		la = cells[h][w + 1];
		lh = h;
		lw = w + 1;
	}
	//South
	if(h + 1 < H && cells[h + 1][w] < la) {
		la = cells[h + 1][w];
		lh = h + 1;
		lw = w;
	}

	if(lh == h && lw == w) {
		cmap[h][w] = color;
	} else {
		cmap[h][w] = colorCell(lh, lw, color);
	}
	return cmap[h][w];
}

void go(int caseId) {
	cin >> H >> W;
	int iH, iW;
	char nextColor = 'a';
	char tColor;
	for(iH = 0; iH < H; iH ++) {
		for(iW = 0; iW < W; iW ++) {
			cin >> cells[iH][iW];
			cmap[iH][iW] = 0;
		}
	}
	cout << "Case #" << caseId << ":" << endl;
	for(iH = 0; iH < H; iH ++) {
		for(iW = 0; iW < W; iW ++) {
			if(!cmap[iH][iW]) {
				tColor = colorCell(iH, iW, nextColor);
				if(tColor == nextColor) {
					nextColor ++;
				}
			}
			if(iW > 0)
				cout << " ";
			cout << cmap[iH][iW];
		}
		cout << endl;
	}
}


int main() {
	cin >> T;
	for(int i = 1; i <= T; i ++) {
		go(i);
	}
	return 0;
}
