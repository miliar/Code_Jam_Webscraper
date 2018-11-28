#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

typedef pair<int, int> pii;

const int h = 20;

int T, n;
int a[h];

int main() {
	//ifstream in("input.txt");
	ifstream in("C-small.in");
	freopen("C-small.out", "w", stdout);
	in >> T;
	for (int t = 0; t < T; t++) {
		in >> n;
		for (int i = 0; i < n; i++)
			in >> a[i];
		int ans = -1;
		int N = 1 << n;
		for (int m = 1; m < N - 1; m++) {
			int A = 0, B = 0, s = 0;
			for (int i = 0; i < n; i++)
				if (m & (1 << i)) {
					B ^= a[i];
					s += a[i];
				} else
					A ^= a[i];
			if (A == B)
				ans = max(ans, s);
		}
		printf("Case #%d: ", t+1);
		if (ans == -1)
			puts("NO");
		else
			printf("%d\n", ans);
	}
}