#include <cstdlib>
#include <iostream>

using namespace std;

int gcd(int a, int b) {
	while (1) {
		a = a%b;
		if (a == 0) return b;
		b = b%a;
		if (b == 0) return a;
	}
}

int main() {

	int T;

	cin >> T;

	for (int t = 1; t <= T; ++t) {
	
		unsigned long N;
		int pd, pg;
		bool c = true;

		cin >> N >> pd >> pg;

		if ( pg == 100 && pd < 100 )
			c = false;

		if ( pg == 0 && pd > 0 )
			c = false;

		int num = 100 / gcd(pd, 100);

		//cout << "n:" << num << endl;

		if ( N < num )
			c = false;

		if (c)
			cout << "Case #" << t << ": Possible"  << endl;
		else
			cout << "Case #" << t << ": Broken" << endl;

	}

}


