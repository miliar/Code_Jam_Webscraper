#include <vector>
#include <string>
#include <algorithm>
#include <stdio.h>
using namespace std;

int runTest() {
	int N;
	char buf[64];
	scanf("%d", &N);
	fgets(buf, 64, stdin);
	vector<string> m(N);
	vector<int> minRow(N, 0);
	for (int i=0; i<N; i++) {
		fgets(buf, 64, stdin);
		m[i] = buf;
	}

	for (int i=0; i<N; i++)
		for (int j=0; j<N; j++)
			if (m[i][j]=='1')
				minRow[i] = j;

	int res = 0;
	for (int row=0; row<N; row++) {
		if (minRow[row]>row) {
			int next = row;
			do {
				next++;
			} while (minRow[next]>row);
			for (int i=next; i>row; i--) {
				swap(minRow[i-1], minRow[i]);
				swap(m[i-1], m[i]); // for debug purposes
				res++;
			}
		}
	}
	return res;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
		printf("Case #%d: %d\n", t, runTest());
	return 0;
}
