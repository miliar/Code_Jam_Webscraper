#include <iostream>
#include <fstream>
using namespace std;

#ifdef WIN32
ifstream in("B-large.in");
#define cin in
ofstream out("B-large.out");
#define cout out
#endif

int mm[110][110], w, h, move[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
char bb[110][110];

char go(int r, int c, char cur)
{
	if (bb[r][c]) return bb[r][c];

	int r2 = -1, c2 = -1;
	for (int i = 0; i < 4; ++i) {
		int rr = r + move[i][0], cc = c + move[i][1];
		if (rr >= 0 && rr < h && cc >= 0 && cc < w && mm[rr][cc] < mm[r][c]) {
			if (r2 < 0 || mm[rr][cc] < mm[r2][c2]) {
				r2 = rr; c2 = cc;
			}
		}
	}
	if (r2 >= 0) {
		return bb[r][c] = go(r2, c2, cur);
	}

	return bb[r][c] = cur;
}

int main()
{
	int T, ca = 0;
	for (cin >> T; T; --T) {
		cin >> h >> w;
		memset(bb, 0, sizeof(bb));
		for (int i = 0; i < h; ++i) for (int j = 0; j < w; ++j) {
			cin >> mm[i][j];
		}

		char cur = 'a';
		for (int i = 0; i < h; ++i) for (int j = 0; j < w; ++j) {
			if (!bb[i][j]) {
				if (cur == go(i, j, cur))
					++cur;
			}
		}

		cout << "Case #" << ++ca << ":" << endl;
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				if (j) cout << " ";
				cout << bb[i][j];
			}
			cout << endl;
		}
	}

	return 0;
}
