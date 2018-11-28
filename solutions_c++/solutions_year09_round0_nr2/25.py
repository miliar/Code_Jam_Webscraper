#include <iostream>
using namespace std;

int N;
int H, W;
int elev[500][500];
bool done[500][500];
char label[500][500];
char nextLabel;

char recurse(int i, int j) {
	if (done[i][j]) return label[i][j];
	done[i][j] = true;
	int nextI = i, nextJ = j;
	if (i-1 >= 0 && elev[i-1][j] < elev[nextI][nextJ]) {
		nextI = i-1;
		nextJ = j;
	}
	if (j-1 >= 0 && elev[i][j-1] < elev[nextI][nextJ]) {
		nextI = i;
		nextJ = j-1;
	}
	if (j+1 < W && elev[i][j+1] < elev[nextI][nextJ]) {
		nextI = i;
		nextJ = j+1;
	}
	if (i+1 < H && elev[i+1][j] < elev[nextI][nextJ]) {
		nextI = i+1;
		nextJ = j;
	}
	if (nextI == i && nextJ == j) return (label[i][j] = nextLabel++);
	return (label[i][j] = recurse(nextI, nextJ));
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> H >> W;
		cout << "Case #" << (i+1) << ":\n";
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++) {
				cin >> elev[i][j];
				done[i][j] = false;
			}
		nextLabel = 'a';
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				cout << recurse(i, j) << (j == W-1 ? '\n' : ' ');
	}
}
