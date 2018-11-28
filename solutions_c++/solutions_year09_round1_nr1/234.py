#include <iostream>
#include <string>
#include <sstream>
using namespace std;

bool started[100001][11];
bool done[100001][11];
bool happyInBase[100001][11];

bool recurse(int n, int b) {
	if (done[n][b]) return happyInBase[n][b];
	if (started[n][b]) return false;
	if (n == 1) {
		happyInBase[n][b] = true;
		done[n][b] = true;
		return true;
	}
	started[n][b] = true;
	int z = n, v = 0;
	while (z) {
		v += (z%b)*(z%b);
		z /= b;
	}
	happyInBase[n][b] = recurse(v, b);
	done[n][b] = true;
	return happyInBase[n][b];
}

int main() {
	for (int i = 2; i <= 100000; i++)
		for (int j = 2; j <= 10; j++)
			recurse(i, j);
	
	int T;
	cin >> T;
	string line;
	getline(cin, line);
	for (int z = 0; z < T; z++) {
		getline(cin, line);
		istringstream values(line);
		bool required[11];
		for (int j = 2; j <= 10; j++) required[j] = false;
		int b;
		while (values >> b) required[b] = true;
		for (int i = 2; i <= 100000; i++) {
			int alive = true;
			for (int j = 2; j <= 10 && alive; j++)
				if (required[j] && !happyInBase[i][j]) alive = false;
			if (alive) {
				cout << "Case #" << (z+1) << ": " << i << endl;
				break;
			}
		}
	}
	return 0;
}
