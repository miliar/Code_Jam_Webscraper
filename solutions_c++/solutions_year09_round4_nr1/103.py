#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


FILE *fin, *fout;
int a[50][50];

int main() {

	fin = fopen("A-large.in", "r");
	fout = fopen("aout.txt", "w");

	int T, n;
	fscanf(fin, "%d", &T);
	int last[50];

	char x;	
	for (int t = 1; t <= T; t++) {
		memset(a, 0, sizeof(a));
		int ans = 0;
		fscanf(fin, "%d", &n);
		memset(last, 0xff, sizeof(last));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				fscanf(fin, "%c", &x);
				while (x != '0' && x != '1')
					fscanf(fin, "%c", &x);

				a[i][j] = x - '0';
				if (a[i][j] == 1) {
					last[i] = j;
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = i; j < n; j++) {
				if (last[j] <= i) {
					int x = last[j];
					for (int k = j; k > i; k--) {
						last[k] = last[k-1];
					}
					last[i] = x;
					ans += (j - i);
					break;
				}
			}
		}
		fprintf(fout, "Case #%d: %d\n", t, ans);
	}


	return 0;
}
