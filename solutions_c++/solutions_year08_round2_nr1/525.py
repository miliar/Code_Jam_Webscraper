#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

long long a[100000][2];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		long long n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		a[0][0] = x0;
		a[0][1] = y0;
		for (int j = 1; j < n; ++j) {
			a[j][0] = (A * a[j - 1][0] + B) % M;
			a[j][1] = (C * a[j - 1][1] + D) % M;
		}
		long long ans = 0;
		for (int ii = 0; ii < n; ++ii)
			for (int jj = ii + 1; jj < n; ++jj)
				for (int kk = jj + 1; kk < n; ++kk)
				{
					int x1, y1, x2, y2, x3, y3;
					x1 = a[ii][0];
					y1 = a[ii][1];
					x2 = a[jj][0];
					y2 = a[jj][1];
					x3 = a[kk][0];
					y3 = a[kk][1];
					if ((x1 + x2 + x3) % 3 == 0 && (y1 + y2 + y3) % 3 == 0)
						++ans;
				}
				cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}

