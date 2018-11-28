#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

void solve(int pno)
{
	int R, C, D;
	
	cin >> R >> C >> D;
	
	long long B[R][C];
	
	string x;
	for (int i = 0; i < R; ++i) {
		cin >> x;
		for (int j = 0; j < C; ++j) {
			B[i][j] = x[j] - '0' + D;
		}
	}
	
	int ans = 0;
	// odd
	for (int i = 1; i < R - 1; ++i) {
		for (int j = 1; j < C - 1; ++j) {
			int d = 0;
			long long wx = 0, wy = 0;
			while (1) {
				++d;
				if (i - d < 0 || i + d == R || j - d < 0 || j + d == C) break;
				for (int ii = i - d + 1; ii < i + d; ++ii) {
					wx += B[ii][j - d] * (ii - i);
					wy += B[ii][j - d] * (-d);
					wx += B[ii][j + d] * (ii - i);
					wy += B[ii][j + d] * (d);
				}
				for (int jj = j - d + 1; jj < j + d; ++jj) {
					wx += B[i - d][jj] * (-d);
					wy += B[i - d][jj] * (jj - j);
					wx += B[i + d][jj] * (d);
					wy += B[i + d][jj] * (jj - j);
				}
				if (d > 1) {
					wx += B[i - d + 1][j - d + 1] * (d - 1) * (-1);
					wy += B[i - d + 1][j - d + 1] * (d - 1) * (-1);
					wx += B[i + d - 1][j - d + 1] * (d - 1);
					wy += B[i + d - 1][j - d + 1] * (d - 1) * (-1);
					wx += B[i - d + 1][j + d - 1] * (d - 1) * (-1);
					wy += B[i - d + 1][j + d - 1] * (d - 1);
					wx += B[i + d - 1][j + d - 1] * (d - 1);
					wy += B[i + d - 1][j + d - 1] * (d - 1);
				}
				if (wx == 0 && wy == 0) {
					ans = max(ans, 2 * d + 1);
					//printf("(%d, %d) - %d\n", i, j, 2 * d + 1);
				}
			}
		}
	}

	// even
	for (int i = 0; i < R - 1; ++i) {
		for (int j = 0; j < C - 1; ++j) {
			int d = 1;
			long long wx = 0, wy = 0;
			while (1) {
				++d;
				if (i - d < -1 || i + d == R || j - d < -1 || j + d == C) break;
				for (int ii = i - d + 2; ii < i + d; ++ii) {
					wx += B[ii][j - d + 1] * ( (ii - i) * 2 - 1);
					wy += B[ii][j - d + 1] * (-2 * d + 1);
					wx += B[ii][j + d] * ( (ii - i) * 2 - 1);
					wy += B[ii][j + d] * (d * 2 - 1);
				}
				for (int jj = j - d + 2; jj < j + d; ++jj) {
					wx += B[i - d + 1][jj] * (-2 * d + 1);
					wy += B[i - d + 1][jj] * ( (jj - j) * 2 - 1);
					wx += B[i + d][jj] * (d * 2 - 1);
					wy += B[i + d][jj] * ( (jj - j) * 2 - 1);
				}
				if (d > 1) {
					wx += B[i - d + 2][j - d + 2] * ( (d - 1) * 2 -1) * (-1);
					wy += B[i - d + 2][j - d + 2] * ( (d - 1) * 2 -1) * (-1);
					wx += B[i + d - 1][j - d + 2] * ( (d - 1) * 2 -1);
					wy += B[i + d - 1][j - d + 2] * ( (d - 1) * 2 -1) * (-1);
					wx += B[i - d + 2][j + d - 1] * ( (d - 1) * 2 -1) * (-1);
					wy += B[i - d + 2][j + d - 1] * ( (d - 1) * 2 -1);
					wx += B[i + d - 1][j + d - 1] * ( (d - 1) * 2 -1);
					wy += B[i + d - 1][j + d - 1] * ( (d - 1) * 2 -1);
				}
				if (wx == 0 && wy == 0) {
					ans = max(ans, 2 * d);
					//printf("(%d, %d) - %d\n", i, j, 2 * d);
				}
			}
		}
	}
	if (ans < 3) printf("Case #%d: IMPOSSIBLE\n", pno);
	else printf("Case #%d: %d\n", pno, ans);
	cout.flush();
	
}

int main()
{
	int T;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}