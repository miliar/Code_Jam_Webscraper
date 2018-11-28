#include <cstdio>
#include <iostream>
using namespace std;

int gcd(int a, int b)  {
	return b == 0 ? a : gcd(b, a%b);
}

int main() {
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++) {
		long long N;
		int pd, pg;
		bool possible;
		cin >> N >> pd >> pg;
		if(pd == 0)
			possible = pg < 100;
		else if(pd == 100)
			possible = pg > 0;
		else if(pg == 0 || pg == 100)
			possible = false;
		else {
			int g = gcd(pd, 100);
			int m = 100/g;
			possible = m <= N;
		}
		if(possible)
			cout << "Case #" << z << ": Possible\n";
		else
			cout << "Case #" << z << ": Broken\n";
	}
	return 0;
}