#include <iostream>
using namespace std;

int N, K;
char m[64][64], mr[64][64];

int dx[8] = {1, 1,  1, -1, -1, -1, 0,  0};
int dy[8] = {0, 1, -1,  0,  1, -1, 1, -1};

void print(char map[64][64]) {
	for (int j=0; j<=N+1; j++) {
		for (int i=0; i<=N+1; i++) {
			cout << map[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

bool check(char c) {
	int i, j, k, d;

	for (i=1; i<=N; i++) {
		for (j=1; j<=N; j++) {
			for (d=0; d<8; d++) {
				for (k=0; k<K; k++) {
					if (m[i+dx[d]*k][j+dy[d]*k] != c) break;
				}
				if (k == K) return true;
			}
		}
	}
	return false;
}

int main() {

//freopen("in.txt", "r", stdin);

int i, j, tmp, t, T;
bool r, b;

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;
cin >> K;

for (j=1; j<=N; j++) {
	for (i=1; i<=N; i++) {
		cin >> m[i][j];
	}
}
for (i=0; i<=N+1; i++) m[i][0] = m[i][N+1] = m[0][i] = m[N+1][i] = 'X';

//print(m);

for (i=0; i<=N+1; i++) {
	for (j=0; j<=N+1; j++) {
		mr[N+1-j][i] = m[i][j];
	}
}

//print(mr);

for (i=1; i<=N; i++) {
	for (j=tmp=N; j>=1; j--) {
		if (mr[i][j] != '.') m[i][tmp--] = mr[i][j];
	}
	for (; tmp>=1; tmp--) m[i][tmp] = '.';
}

//print(m);

r = check('R');
b = check('B');

cout << "Case #" << t << ": ";
if (r && b) cout << "Both" << endl;
else if (r && !b) cout << "Red" << endl;
else if (!r && b) cout << "Blue" << endl;
else if (!r && !b) cout << "Neither" << endl;

}

return 0;
}
