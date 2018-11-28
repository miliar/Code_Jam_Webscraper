#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <memory.h>
using namespace std;

#define MAXN 110
#define SIZE 4
#define BIT(i) (1 << (i))

char tmp[MAXN];

int row[SIZE] = { BIT(0) + BIT(1) + BIT(2) + BIT(3), BIT(4) + BIT(5) + BIT(6)
		+ BIT(7), BIT(8) + BIT(9) + BIT(10) + BIT(11), BIT(12) + BIT(13)
		+ BIT(14) + BIT(15), };
int col[SIZE] = { BIT(0) + BIT(4) + BIT(8) + BIT(12), BIT(1) + BIT(5) + BIT(9)
		+ BIT(13), BIT(2) + BIT(6) + BIT(10) + BIT(14), BIT(3) + BIT(7)
		+ BIT(11) + BIT(15), };
int diag[2] = { BIT(0) + BIT(5) + BIT(10) + BIT(15), BIT(3) + BIT(6) + BIT(9)
		+ BIT(12) };

int main() {
	int cases;
	int caseId = 1;
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {

		bool isComplete = true;
		int Omap = 0;
		int Xmap = 0;
		bool Owin = false;
		bool Xwin = false;

		// IO
		for (int i = 0; i < SIZE; i++) {
			scanf("%s", tmp);
			for (int j = 0; j < SIZE; j++) {
				switch (tmp[j]) {
				case '.':
					isComplete = false;
					break;
				case 'O':
					Omap |= BIT(i * SIZE + j);
					break;
				case 'X':
					Xmap |= BIT(i * SIZE + j);
					break;
				case 'T':
					Omap |= BIT(i * SIZE + j);
					Xmap |= BIT(i * SIZE + j);
					break;
				}
			}
		}

		// solve
		for (int i = 0; i < SIZE; i++) {
			if ((row[i] & Omap) == row[i])
				Owin = true;
			if ((row[i] & Xmap) == row[i])
				Xwin = true;
			if ((col[i] & Omap) == col[i])
				Owin = true;
			if ((col[i] & Xmap) == col[i])
				Xwin = true;
		}
		for (int i = 0; i < 2; i++) {
			if ((diag[i] & Omap) == diag[i])
				Owin = true;
			if ((diag[i] & Xmap) == diag[i])
				Xwin = true;
		}

		// print
		printf("Case #%d: ", caseId++);
		if (isComplete && Owin == Xwin) {
			printf("Draw\n");
		} else if (Xwin) {
			printf("X won\n");
		} else if (Owin) {
			printf("O won\n");
		} else if (isComplete == false) {
			printf("Game has not completed\n");
		}

	}
	return 0;
}

