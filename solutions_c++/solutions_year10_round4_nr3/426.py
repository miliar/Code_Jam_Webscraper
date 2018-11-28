#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

int r, polje[100][100], polje2[100][100];

int task() {
	//init
	memset(polje, 0, sizeof polje);

	//read
	scanf("%d", &r);
	for (int i = 0; i < r; i++) {
		int a, b, c, d;
		scanf("%d %d %d %d", &a, &b, &c, &d); a--; b--; c--; d--;
		for (int i = a; i <= c; i++)
			for (int j = b; j <= d; j++)
				polje[i][j] = 1;
	}
		
	//solve
	for (int days = 0; ; days++) {
		bool p = 1;
		
		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 100; j++) {
				polje2[i][j] = polje[i][j];
				if (polje[i][j]) {
					p = 0;
					if ((i == 0 || !polje[i - 1][j]) && (j == 0 || !polje[i][j - 1]))
						polje2[i][j] = 0;
				} else {
					if ((i > 0 && polje[i - 1][j]) && (j > 0 && polje[i][j - 1]))
						polje2[i][j] = 1;
				}
			}

		if (p) return days;
		
		memcpy(polje, polje2, sizeof polje);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		printf("%d\n", task());
		//task();
	}
}

