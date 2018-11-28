#include <cstdio>
#include <iostream>

using namespace std;


int main(int argc, char **argv) {
	int nT;
	scanf("%d", &nT);
	for (int i = 1; i <= nT; ++i) {
		int swaps = 0;

		int N;
		scanf("%d", &N);
		char dummy = getchar();

		char matrix[N][N];

		for (int j = 0; j < N; ++j) {
			for (int k = 0; k < N; ++k) {
				scanf("%c", &matrix[j][k]);
				// cerr << "read \"" << matrix[j][k] << "\"\n";
			}
			dummy = getchar();
		}

		for (int l = 0; l < N; ++l) {
			int j;
			for (j = l; j < N; ++j) {
				int pos = N-1;
				while ((pos > l)  && (matrix[j][pos] == '0')) {
					--pos;
				}
				// cerr << "line " << j << " pos " << pos << endl;
				if (pos <= l) break;

			}
			// cerr << "line " << l << "\t fetching from " << j << endl;
			swaps += j - l;
			char tmp[N];
			for (int x = 0; x < N; ++x) {
				tmp[x] = matrix[j][x];
			}
			for (int x = j; x > l; --x) {
				for (int y = 0; y < N; ++y) {
					matrix[x][y] = matrix[x-1][y];
				}
			}
			for (int x = 0; x < N; ++x) {
				matrix[l][x] = tmp[x];
			}
		}
		printf("Case #%d: %d\n", i, swaps);

	}
}
