#include <iostream>
using namespace std;

char G[4][4];

int fun(char c) {
	int i, j;
	for(i = 0; i < 4; i++) {
		for(j = 0; j < 4; j++) 
			if(G[i][j] == c || G[i][j] == 'T') continue;
			else break;
		if(j == 4)
			return 1;
	}
	//cout << "@1" << endl;
	for(j = 0; j < 4; j++) {
		for(i = 0; i < 4; i++) 
			if(G[i][j] == c || G[i][j] == 'T') continue;
			else break;
		if(i == 4)
			return 1;
	}
	//cout << "@2" << endl;
	for(i = 0; i < 4; i++) {
		if(G[i][i] == c || G[i][i] == 'T') continue;
		else break;
	}
	if(i == 4) return 1;
	//cout << "@3" << endl;
	for(i = 0; i < 4; i++) {
		if(G[i][3-i] == c || G[i][3-i] == 'T') continue;
		else break;
	}
	if(i == 4) return 1;

	return 0;
}

int isEmpty() {
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (G[i][j] == '.') 
				return 1;
		}
	}
	return 0;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, t;
	int i, j;
	int x, o;

	cin >> T;
	for (t = 1; t < T + 1; t++) {
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				cin >> G[i][j];
			}
		}

		x = fun('X');
		o = fun('O');
		//cout << "x = " << x << " o = " << o << endl;
		cout << "Case #" << t << ": ";
		if (x == 1 && o == 0) cout << "X won" << endl;
		else if (x == 0 && o == 1) cout << "O won" <<endl;
		else if (isEmpty()) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}
	//system("pause");
	return 0;
}