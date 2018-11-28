#include <iostream>
#include <algorithm>

using namespace std;


int main() {
	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		int n, k;
		cin >> n >> k;
		char board[50][50];
		for (int i = n - 1; i >= 0; i--)
			for (int j = 0; j < n; j++)
				cin >> board[i][j];
		char rotate[50][50];
		fill(rotate[0], rotate[50], '.');

		for (int r = 0; r < n; r++) {
			int c = 0;
			for (int j = n - 1; j >= 0; c += board[r][j] != '.', j--)
				rotate[c][r] = board[r][j];
		}

		char left[50][50];
		char down[50][50];
		char dl[50][50];
		char dr[50][50];

		bool blue = false, red = false;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (rotate[i][j] == '.') continue;
				left[i][j] = j == 0 ? 1 :
					rotate[i][j - 1] != rotate[i][j] ? 1 :
					left[i][j - 1] + 1;
				down[i][j] = i == 0 ? 1 :
					rotate[i - 1][j] != rotate[i][j] ? 1 :
					down[i - 1][j] + 1;
				dl[i][j] = j == 0 || i == 0 ? 1 :
					rotate[i - 1][j - 1] != rotate[i][j] ? 1 :
					dl[i - 1][j - 1] + 1;
				dr[i][j] = i == 0 || j == n - 1 ? 1 :
					rotate[i - 1][j + 1] != rotate[i][j] ? 1 :
					dr[i - 1][j + 1] + 1;

				if (left[i][j] == k
						|| down[i][j] == k
						|| dl[i][j] == k
						|| dr[i][j] == k)
					(rotate[i][j] == 'B' ? blue : red) = true;
			}
		}

		cout << "Case #" << caseno << ": ";
		if (red && blue) cout << "Both" << endl;
		else if (blue) cout << "Blue" << endl;
		else if (red) cout << "Red" << endl;
		else cout << "Neither" << endl;
	}
	return 0;
}
