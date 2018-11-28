#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <sstream>
#include <map>

using namespace std;

int tab[111][111];
int dx[] = {-1, 0};
int dy[] = {0, -1};

bool simulate(int sz) {
	int alive = 0;
	for (int i = sz-1; i >= 0; i--) {
		for (int j = sz-1; j >= 0; j--) {
			int c = 0;
			for (int k = 0; k < 2; k++) {
				int mX = i+dx[k];
				int mY = j+dy[k];
				if (mX < 0 || mY < 0 || mX >= sz || mY >= sz) continue;
				if (tab[mX][mY]) c++;
			}
			if (tab[i][j]) {
				if (c == 0) tab[i][j] = 0;
			} else {
				if (c == 2) tab[i][j] = 1;
			}
			if (tab[i][j]) alive++;
		}
	}
	return alive ? true : false;
}

void print() {
	for (int i = 1; i <= 5; i++) {
		for (int j = 1; j <= 6; j++) {
			cout << tab[i][j];
		}
		cout << "\n";
	}
	cout << "\n";
}

int main() {
	int C; cin >> C;
	for (int t = 0; t < C; t++) {
		int R; cin >> R;
		memset(tab,0,sizeof(tab));
		for (int tt = 0; tt < R; tt++) {
			int X1, Y1, X2, Y2;
			cin >> X1 >> Y1 >> X2 >> Y2;
			for (int i = X1; i <= X2; i++) {
				for (int j = Y1; j <= Y2; j++) {
					tab[j][i] = 1;
				}
			}
		}
		// simulate
		int count = 1;
		//print();
		while (simulate(101)) {
			//print();
			count++;
		}
		cout << "Case #" << (t+1) << ": " << count << "\n";
	}
	return 0;
}