#include <iostream>
using namespace std;

int w,h;
bool m[100][100];

void input() {
	int rn;
	cin >> w >> h >> rn;
	
	for(int i=0;i<w;i++)
		for(int j=0;j<h;j++)
			m[i][j] = false;
	
	for(int i=0;i<rn;i++) {
		int x, y;
		cin >> x >> y;
		m[x-1][y-1] = true;
	}
}

int table[100][100];

int gettable(int i, int j) {
	int& item = table[i][j];
	if(item == -1) {
		item = 0;
		if(!m[i][j]) {
			if(i==w-1 && j==h-1)
				item = 1;
			else {
				if(i+2 < w && j+1 < h)
					item += gettable(i+2, j+1);
				if(i+1 < w && j+2 < h)
					item += gettable(i+1, j+2);
			}
		}		
		item %= 10007;
	}
	return item;
}

int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		
		for(int i=0;i<w;i++)
			for(int j=0;j<h;j++)
				table[i][j] = -1;
		



		cout << "Case #" << casei << ": ";
		
		cout << gettable(0,0) << endl;
	}
	return 0;
}
