#include <cstdio>
#include <memory.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>

using namespace std;

int N[111], S[111];
int d[111][111];

void getBounds(int idx, int x) {
	N[idx] = S[idx] = -1;

	for (int i = 0; i <= 10; i++){
		if (i > x) break;
		for (int j = i; j <= 10; j++) {
			if (i + j > x) break;
			int k = x - i - j;

			if (k < 0 || k > 10) continue;

			if (abs(i - j) > 2 || abs(i - k) > 2 || abs(j - k) > 2) continue;

			bool un = true;
			if (abs(i - j) == 2 || abs(i - k) == 2 || abs(j - k) == 2) un = false;
			int mx = max(max(i, j), k);

			if (un) N[idx] = max(N[idx], mx);
			else S[idx] = max(S[idx], mx);
		}
	}
}

int main(){
	FILE *fin = fopen("B.in", "r");
	FILE *fout = fopen("B.out", "w");

	int t;
	fscanf(fin, "%d", &t);

	for (int test = 1; test <= t; test++) {
		memset(N, 0, sizeof(N));
		memset(S, 0, sizeof(S));

		fprintf(fout, "Case #%d: ", test);
		int n, s, p;
		fscanf(fin, "%d%d%d", &n, &s, &p);

		for (int i = 0; i < n; i++) {
			int x;
			fscanf(fin, "%d", &x);
			getBounds(i, x);
		}

		memset(d, 0, sizeof(d));

		if (N[0] >= p) d[0][0] = 1;
		if (S[0] >= p) d[0][1] = 1;
		else if (S[0] == -1) d[0][1] = -555555555;

		for (int i = 1; i < n; i++) {
			d[i][0] = d[i - 1][0];
			if (N[i] >= p) d[i][0]++;

			for (int j = 1; j <= s; j++) {
				int tmp = d[i - 1][j];
				if (N[i] >= p) tmp++;

				d[i][j] = d[i - 1][j - 1];
				if (S[i] >= p) d[i][j]++;

				d[i][j] = max(d[i][j], tmp);
			}
		}
		fprintf(fout, "%d\n", d[n - 1][s]);
	}
}