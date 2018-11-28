#include <iostream>
#include <string>

using namespace std;
string t[55];
int N, K;

bool check (char col) {
	int dx[] = {1, 0, 1, -1, 1};
	int dy[] = {0, 1, 1, 1, -1};
	for (int d=0; d<5; d++) {
		for (int x=0; x<N; x++) {
			for (int y=0; y<N; y++) {
				int ile = 0;
				for (int k=0; k<K; k++) {
					if (y+dy[d]*k >= 0 && y+dy[d]*k < N && x+dx[d]*k >= 0 && x+dx[d]*k < N && t[y+dy[d]*k][x+dx[d]*k] == col)
						ile ++;
					else 
						break;
				}
				if (ile == K)
					return true;
			}
		}
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int q=1; q<=T; q++) {
		cin >> N >> K;
		for (int i=0; i<N; i++) {
			cin >> t[i];
			for (int j=0; j<t[i].size(); j++)
				while (j < t[i].size() && t[i][j] == '.') t[i] =  t[i].substr (0, j) + t[i].substr(j+1);
			while (t[i].length() < N) t[i] = "." + t[i];
		}

		bool b = check('B');
		bool r = check('R');
		string ret = "Neither";
		if (b && r) ret = "Both";
		else if (b) ret = "Blue";
		else if (r) ret = "Red";

		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}