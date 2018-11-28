#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char *H;
char *V;
char *X;

#define M 6010
#define M2 (M * M)

int doit() {
	H = (char*)calloc(M2, 1);
	V = (char*)calloc(M2, 1);
	X = (char*)calloc(M2, 1);

	int dx[] = {-1, 0, 1, 0};
	int dy[] = {0, -1, 0, 1};

	int x = M / 2;
	int y = M / 2;
	int d = 0;
	int L;
	cin >> L;
	for (int i = 0; i < L; i++) {
		string S;
		int T;
		cin >> S >> T;
		for (int j = 0; j < T; j++) {
			for (int k = 0; k < S.size(); k++) {
				switch(S[k]) {
					case 'R':
						d = (d + 1) % 4;
						break;
					case 'L':
						d = (d + 3) % 4;
						break;
					case 'F':
						switch (d) {
							case 0:
								H[(x - 1) * M + y] = 1;
								break;
							case 1:
								V[x * M + y - 1] = 1;
								break;
							case 2:
								H[x * M + y] = 1;
								break;
							case 3:
								V[x * M + y] = 1;
								break;
						}
						x += dx[d];
						y += dy[d];
				}
			}
		}
	}
	int c = 0;
	for (x = 0; x < M; x++) {
		for (y = 0; y < M; y++) {
			if (H[x * M + y]) break;
		}
		if (y == M) continue;
		int y0 = y;
		int out = 1;
		int started = 0;
		for (y = M - 1; y > y0; y--) {
			if (started && out) {
				X[x * M + y] = 1;
				// cout << "H: " << x << " " << y << endl;
				c++;
			}
			if (H[x * M + y]) {
				started = 1;
				out = 1 - out;
			}
		}
	}
	for (y = 0; y < M; y++) {
		for (x = 0; x < M; x++) {
			if (V[x * M + y]) break;
		}
		if (x == M) continue;
		int x0 = x;
		int out = 1;
		int started = 0;
		for (x = M - 1; x > x0; x--) {
			if (started && out) {
				if (!X[x * M + y]) {
					// cout << "V: " << x << " " << y << endl;
					c++;
				}
			}
			if (V[x * M + y]) {
				started = 1;
				out = 1 - out;
			}
		}
	}
	free(H);
	free(V);
	free(X);
	return c;
}

int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int res = doit();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}

