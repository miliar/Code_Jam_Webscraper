#include <cstdio>
#include <iostream>
using namespace std;

int getmul(int x) {
	int d = 1;
	while (x) {
		x /= 10; d *= 10; 
	}
	return d / 10;
}

int count(int x, int upper) {
	int l = getmul(x);
	int y = x;
	int ans = 0;
	do {
		int z = y % 10;	
		y = y / 10 + z * l;
		if (y > x && y <= upper) ans ++;
	} while (y != x);
	return ans;
}

int main() {

	int T;
	cin >> T;
	for (int _t = 1; _t <= T; _t ++) {
		int A, B;
		cin >> A >> B;
		int ans = 0;
		for (int i = A; i <= B; i ++)
			ans += count(i, B);
		printf("Case #%d: %d\n", _t, ans);
	}
}
