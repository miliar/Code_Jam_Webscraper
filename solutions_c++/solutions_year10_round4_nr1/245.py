#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	int costs[200];
	costs[0] = 0;
	for (int i = 1; i < 200; i++)
		costs[i] = costs[i - 1] + (2 * i - 1);

	for (int caseno = 1; caseno <= ncases; caseno++) {
		int k;
		cin >> k;

		int dia[100][100];
		fill(dia[0], dia[100], -1);
		for (int i = 1; i < 2 * k; i++) {
			int r = 50 - k + i;
			int c = 50 - k + 1;
			c += abs(i - k);
			for (int j = 0; j < min(i, 2 * k - i); j++) {
				cin >> dia[r][c];
				c += 2;
			}
		}

		bool r[100];
		bool c[100];
		fill(r, r + 100, 1);
		fill(c, c + 100, 1);

		for (int i = 50 - k + 1; i < 50 + k; i++) {
			for (int j = 50 - k + 1; j < 50 + k; j++) {
				if (dia[i][j] < 0) continue;
				for (int m = j + 1; m < 50 + k; m++) {
					int j2 = m + m - j;
					if (j2 >= 50 + k) continue;
					if (dia[i][j2] < 0) continue;
					if (dia[i][j2] == dia[i][j]) continue;
					c[m] = 0;
				}
				for (int m = i + 1; m < 50 + k; m++) {
					int i2 = m + m - i;
					if (i2 >= 50 + k) continue;
					if (dia[i2][j] < 0) continue;
					if (dia[i2][j] == dia[i][j]) continue;
					r[m] = 0;
				}
			}
		}

		int dr = 0;
		while (r[50 - dr] == 0 && r[50 + dr] == 0) dr++;
		int dc = 0;
		while (c[50 - dc] == 0 && c[50 + dc] == 0) dc++;

		int mincost = costs[dr + dc + k] - costs[k];

		cout << "Case #" << caseno << ": " << mincost << std::endl;
	}
	return 0;
}
