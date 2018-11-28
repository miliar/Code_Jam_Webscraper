#include <iostream>

using namespace std;

int gcd(int x, int y) {
	int r;
	while(y != 0) {
		r = x % y;
		x = y;
		y = r;
	}
	return x;
}

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int index = 1; index <= t; index++) {
		long long n;
		int pd, pg;
		cin >> n >> pd >> pg;
		int d = 100 / gcd(100,pd);
		if (d > n || pg == 100 && pd != 100 || pg == 0 && pd != 0) cout << "Case #" << index << ": Broken" << endl;
		else cout << "Case #" << index << ": Possible" << endl;
	}
	return 0;
}