#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string.h>
#include <climits>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

#define NMAX 40

bool a[NMAX][NMAX];
int hone[NMAX];
int T, N;

void print(void) {
	for (int i = 0; i < N; i++) {
		cout << hone[i] << " ";
		for (int j = 0; j < N; j++) {
			cout << a[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

void printz(void) {
	for (int i = 0; i < N; i++) {
		cout << hone[i] << " ";
	}
	cout << endl;
}

int
main()
{
	int swaps, tmp;
	char ch;

	cin >> T;

	for (int cas = 1; cas <= T; cas++) {
		cin >> N;
		swaps = 0;

		for (int i = 0; i < N; i++) {
			hone[i] = 0;
			for (int j = 0; j < N; j++) {
				cin >> ch;
				a[i][j] = ch - 0x30;
				if (a[i][j] == 1)
					hone[i] = j;
			}
		}

		//print();

		/*
		printf("swaps = %d\n", swaps);
		printz();
		*/
		for (int i = 0; i < N - 1; i++) {
			if (hone[i] > i) {
				int p = i + 1;
				while (hone[p] > i)
					p++;
				tmp = hone[p];
				for (int k = p; k > i; k--)
					hone[k] = hone[k-1];
				hone[i] = tmp;
				swaps += p - i;
			}
		}
			


		printf("Case #%d: %d\n", cas, swaps);
	}

	return 0;
}
