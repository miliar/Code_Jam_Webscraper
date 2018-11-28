#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <ctype.h>
#include <string>

using namespace std;

#define pb pus_back
#define sz(v) ((int)v.size())

int a, b;
int cnt;

inline void calc(int x) {
	int mod = 1,
		len = 0,
		y = x;
	set <int> Y;
	while (10 * mod <= x) {
		++len;
		mod *= 10;
	}
	for (; len; --len) {
		y = y / mod + (y % mod) * 10;
		//cnt += (y >= a && y < x);
		if (y >= a && y < x) 
			Y.insert(y);
	}
	cnt += sz(Y);
}


int cmp(int x, int y) {
	int X[4];
	X[3] = x % 10; x /= 10;
	X[2] = x % 10; x /= 10;
	X[1] = x % 10; x /= 10;
	X[0] = x % 10; 
	for (int r = 0; r < 4; ++r) {
		int tmp = X[3];
		X[3] = X[2];
		X[2] = X[1];
		X[1] = X[0];
		X[0] = tmp;
		if (y == 1000 * X[0] + 100 * X[1] + 10 * X[2] + X[3])
			return 1;
	}
	return 0;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	/*a = 1111, b = 2222;
	int cnt1 = 0;
	for (int i = a; i <= b; ++i) {
		for (int j = a; j < i; ++j) {
			cnt1 += cmp(i,j);
			if (cmp(i,j))
				cout << i << " " << j << " ok\n";
		}
		calc(i);
		if (cnt1 != cnt)
			int xxxx = 90;
	}
	cout << cnt;
	return 0;*/
	//---------------------------------
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cnt = 0;
		cin >> a >> b;
		for (int e = a; e <= b; ++e)
			calc(e);
		printf("Case #%d: %d\n",t, cnt);
	}
	return 0;
}