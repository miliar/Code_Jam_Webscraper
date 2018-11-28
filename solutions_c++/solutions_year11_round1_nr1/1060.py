#include <iostream>

using namespace std;

long long gcd (long long a, long long b) {
	return b == 0 ? a : gcd(b,a%b);
}

int main() {
	long long cases;
	cin >> cases;
	for (long long caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ": ";
		
		long long n,pd,pg;
		bool ans;
		cin >> n >> pd >> pg;
		
		if (pd == 100) {
			if (pg == 0) {
				ans = false;
			} else {
				ans = true;
			}
		} else if (pd == 0) {
			if (pg == 100) {
				ans = false;
			} else {
				ans = true;
			}
		} else if (pg == 0 || pg == 100) {
			ans = false;
		} 
		
		
		else {
			long long gd = 100;
// 			cout << pd << ' ' << gd << ' ';
			long long x = gcd(pd,gd);
			pd = pd/x;
			gd = gd/x;
			
// 			cout << pd << ' ' << gd << ' ' << x << ' ';
			
			ans = gd <= n;
		}
		
		if (ans) {
			cout << "Possible" << endl;
		} else {
			cout << "Broken" << endl;
		}
		
	}
}