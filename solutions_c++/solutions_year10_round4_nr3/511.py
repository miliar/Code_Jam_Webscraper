#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

const char inFileName[] = "C-small.in";
const char outFileName[] = "C-small.out";

const int MaxN = 1000;

int n, sol, T, Min, Max;
vector<int> X1, Y1, X2, Y2;
int a[MaxN][MaxN];

int solve() {
	int time = 0, count = 0;

	for (int i = 0; i < MaxN; i++)
		for (int j = 0; j < MaxN; j++)
			if (a [i][j] == 1) count++;

	while (count > 0) {
		X1.clear(); X2.clear();
		Y1.clear(); Y2.clear();
		time++;
		for (int k = Min; k <= Max; k++) {

			bool exists = false;
			for (int i = 1; i < k; i++) {
				int j = k - i;
				if (a[i][j] == 1) {
					exists = true;
					if ((a[i][j - 1] == 0) && (a[i - 1][j] == 0)) {
						X1.push_back(i);
						Y1.push_back(j);
						count--;
					}
					if ((a[i - 1][j + 1] == 1) && (a[i][j + 1] == 0)) {
						X2.push_back(i);
						Y2.push_back(j + 1);
						count++;
					}
				}
			}
			if ((exists == false) && (k == Min))
				Min++;
		}
			
		for (int i = 0; i < X2.size(); i++) {
			a[X2[i]][Y2[i]] = 1;
			if (Max < X2[i] + Y2[i]) Max = X2[i] + Y2[i];
		}
		for (int i = 0; i < X1.size(); i++)
			a[X1[i]][Y1[i]] = 0;
	}

	return time;
}
	
int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");
		
	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) {

		for (int i = 0; i < MaxN; i++)
			for (int j = 0; j < MaxN; j++) a[i][j] = 0;
		fscanf(inFile, "%d", &n);
		Min = MaxN * MaxN;
		Max = 1;

		for (int i = 0; i < n; i++) {
			int x1, y1, x2, y2;
			fscanf(inFile, "%d%d%d%d", &x1, &y1, &x2, &y2);
			if (Min > x1 + y1) Min = x1 + y1;
			if (Max < x2 + y2) Max = x2 + y2;

			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					a[x][y] = 1;
		}

		fprintf(outFile, "Case #%d: %d\n", t + 1, solve());
	}

	fclose(inFile);
	fclose(outFile);
	return 0;
}
