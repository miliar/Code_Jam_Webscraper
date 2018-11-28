#include <numeric>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

const int N = 200;

int a[N][N], b[N][N];
int x1, y1, x2, y2;
int n, k, ans, t, s;

int main() {

	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		in >> n;
		k = 0; s = 0;
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; ++i) {
			in >> x1 >> y1 >> x2 >> y2;
			for (int ii = x1; ii <= x2; ++ii)
				for (int jj = y1; jj <= y2; ++jj) 
					if (a[ii][jj] == 0) a[ii][jj] = 1;
		}
		ans = 0; k = 1;
		while (k != 0) {
			memset(b, 0, sizeof(b));
			for (int i = 1; i < N; ++i)
				for (int j = 1; j < N; ++j) {
					if (!a[i][j])
						if (a[i - 1][j] && a[i][j - 1]) b[i][j] = 1;
					if (a[i][j]) 
						if (a[i - 1][j] || a[i][j - 1]) b[i][j] = 1;
				}
			k = 0;
			for (int i = 1; i < N; ++i)
				for (int j = 1; j < N; ++j) {
					a[i][j] = b[i][j];
					k += b[i][j];
				}
			ans++;
		}
		out << "Case #" << tt + 1 << ": ";
		out << ans << endl;
	}

	return 0;
}
