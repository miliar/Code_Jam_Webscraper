#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char A[128][128];

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		printf("Case #%d: ", test+1);
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf(" %c", &A[j][n-1-i]);
			}
		}
		for (int j = 0; j < n; j++) {
			int some = 1;
			for (int i = n-1; i >= 0 && some; i--) {
				if (A[i][j] == '.') {
					some = 0;
					for (int k = i-1; k >= 0; k--) {
						if (A[k][j] != '.') {
							some = 1;
							swap(A[i][j], A[k][j]);
							k = 0;
						}
					}
				}
			}
		}
		int ok[26];
		memset(ok, 0, sizeof(ok));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (A[i][j] != '.') {
					int l;
					for (l = i; l < n && A[l][j] == A[i][j]; l++);
					if (l-i >= k) {
						ok[A[i][j]-'A'] = 1;
					}

					for (l = j; l < n && A[i][l] == A[i][j]; l++);
					if (l-j >= k) {
						ok[A[i][j]-'A'] = 1;
					}

					for (l = 0; i+l < n && j+l < n && A[i+l][j+l] == A[i][j]; l++);
					if (l >= k) {
						ok[A[i][j]-'A'] = 1;
					}

					for (l = 0; i+l < n && j-l >= 0 && A[i+l][j-l] == A[i][j]; l++);
					if (l >= k) {
						ok[A[i][j]-'A'] = 1;
					}

					for (l = 0; i-l >= 0 && j+l < n && A[i-l][j+l] == A[i][j]; l++);
					if (l >= k) {
						ok[A[i][j]-'A'] = 1;
					}
				}
			}
		}
		int red = 'R' - 'A';
		int blue = 'B' - 'A';
		if (ok[red] && ok[blue]) {
			printf("Both\n");
		} else if (ok[red]) {
			printf("Red\n");
		} else if (ok[blue]) {
			printf("Blue\n");
		} else {
			printf("Neither\n");
		}
	}
	return 0;
}

