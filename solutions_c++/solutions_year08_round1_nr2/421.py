#define _CRT_SECURE_NO_DEPRECATE

#include<cstdio>

#include<iostream>

#include<fstream>

using namespace std;

int testcases;

const int maxN = 20;

const int maxM = 110;

int N, M;

int link[maxM][maxN]; // 1 0 -1 not need

int main() {

	FILE *fin = fopen("b.in", "r");

	ofstream cout("b.out");

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		fscanf(fin, "%d", &N);

		fscanf(fin, "%d", &M);

		memset(link, 255, sizeof link);

		for (int i = 0; i < M; i++) {

			int t;

			fscanf(fin, "%d", &t);

			for (int k = 0; k < t; k++) {

				int a, b;

				fscanf(fin, "%d %d", &a, &b);

				link[i][a - 1] = b;
			}
		}

		int max = 1 << N;

		int ans, ansvalue;

		ans = N + 1;

		for (int i = 0; i < max; i++) {
	//	for (int i = 1; i < 2; i++) {

            int now = 0;

		//	cout << "Test " << i << endl;

			for (int k = 0; k < N; k++) if ((i & (1 << k)) > 0) ++now;

			if (now >= ans) continue;

		//	cout << "Enter " << i << endl;

			bool suc = true;

			for (int k = 0; k < M; k++) {

				int num = 0;

				for (int r = 0; r < N; r++) if (link[k][r] != -1) {

					if ((i & (1 << r)) > 0 && link[k][r] == 1) ++num;

					if ((i & (1 << r)) == 0 && link[k][r] == 0) ++num;
				}

           //     cout << "at k num" << k << " " << num << endl;

				if (num == 0) { suc = false; break; }
			}

			if (suc) { ans = now; ansvalue = i; }
		}

		cout << "Case #" << cases << ":";

		if (ans == N + 1) { cout << " IMPOSSIBLE" << endl; continue; }

		for (int i = 0; i < N; i++) if ((ansvalue & (1 << i)) > 0) 

			cout << " " << 1; else cout << " " << 0;

		cout << endl;
	}

	return 0;
}
