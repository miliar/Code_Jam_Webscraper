#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int maxR = 64;

int R,C;

string map[maxR];

void input() {
	
	cin >> R >> C;
	for (int i=0;i<R;i++) {
		cin >> map[i];
		//result[i] = map[i];
	}
	
}

bool inbounds(int i, int j) {
	return (i >= 0 && i < R && j >= 0 && j < C);
}

bool solve() {
	for (int i=0;i<R;i++) {
		for (int j=0;j<C;j++) {
			if (map[i][j] == '#') {
				if (!(inbounds(i+1,j) && inbounds(i,j+1) && inbounds(i+1,j+1))) return false;
				if (map[i+1][j] != '#' || map[i][j+1] != '#' || map[i+1][j+1] != '#') return false;
				map[i][j] = '/';
				map[i][j+1] = '\\';
				map[i+1][j] = '\\';
				map[i+1][j+1] = '/';
			}
		}
	}
	return true;
}

void output() {
	for (int i=0;i<R;i++) {
		cout << map[i] << "\n";
	}
}

int main() {
	int t, T;
	cin >> T;
	for (t=1;t<=T;t++) {
		input();
		bool result = solve();
		cout << "Case #" << t << ":\n";
		if (!result) cout << "Impossible\n";
		else output();
	}
	return 0;
}