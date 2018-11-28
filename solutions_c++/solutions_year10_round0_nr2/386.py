#include <iostream>
#include <cmath>
using namespace std;

int gcd(int a, int b) {return b?gcd(b,a%b):a;}

int main() {
	freopen("G:\\B-small-attempt1.in", "r", stdin);
	freopen("G:\\B-small-attempt1.out", "w", stdout);
	int t1,t2,t3;
	int n;
	int c;
	cin >> c;

	while(c > 0) {
		c--;
		cin >> n;
		if (n == 2) {
			cin >> t1 >> t2;
			int m = t1 > t2 ? t1 - t2 : t2 - t1;
			int r = m;
			while(r >= 1) {
				if(m % r) continue;
				int n1 = (r - t1 % r) % r;
				int n2 = (r - t2 % r) %r;
				int nn = n1 > n2 ? n1 - n2 : n2 - n1;
				if (nn % r == 0) {
					cout << (n1 > n2 ? n1 : n2) << endl;
					break;
				}
				r--;
			}
		} else {
			cin >> t1 >> t2 >> t3;
			int m1 = t1 > t2 ? t1 - t2 : t2 - t1;
			int m2 = t2 > t3 ? t2 - t3 : t3 - t2;
			int m = gcd(m1, m2);
			int r = m;
			while(r >= 1) {
				int n1 = (r - t1 % r) % r;
				int n2 = (r - t2 % r) %r;
				int n3 = (r - t3 % r) % r;
				if( (abs(n2 - n1)%r) == 0 && (abs(n3 - n2)%r) == 0) {
					cout << max(n1, max(n2, n3)) << endl;
					break;
				}
				r--;
			}
		}
	}
	return 0;
}
