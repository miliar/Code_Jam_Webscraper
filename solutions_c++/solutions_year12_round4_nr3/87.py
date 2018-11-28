#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Mountain View
int height[2003];

int doit(int cur, int end, int dec, vector <int> &x)
{
	if (cur == end) {
		return 0;
	}
	if (x[cur] > end) {
		return -1;
	}
	int ret = doit(x[cur], end, dec, x);
	height[cur] = height[x[cur]] + dec * (x[cur] - cur);
	ret |= doit(cur + 1, x[cur], dec - 1, x);
	return ret;
}

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		vector <int> x(N + 1, 0);
		for (int i = 1; i < N; i++) {
			cin >> x[i];
		}
		height[N] = 0;
		if (doit(1, N, 0, x)) {
			cout << "Case #" << caseno << ": Impossible" << endl;
			continue;
		}
		cout << "Case #" << caseno << ":";
		int base = *min_element(height + 1, height + N + 1);
		for (int i = 1; i <= N; i++) {
			cout << " " << (height[i] - base + 1);
		}
		cout << endl;
	}

	return 0;
}
