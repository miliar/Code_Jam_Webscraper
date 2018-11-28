#include <iostream>
#include <cmath>

using namespace std;

int T, A, B, n, m, dig, tens1, tens2, newN, result;

int digits(int x) {
	if(x/10 == 0) return 1;
	return 1+digits(x/10);
}

bool recycled() {
	dig = digits(n);
	for(int i=1; i<dig; ++i) {
		tens1 = (int)pow((double)10, i);
		tens2 = (int)pow((double)10, dig-i);
		newN = (n%tens1)*tens2 + (n/tens1);
		if(newN == m) return true;
	}
	return false;
}

int main() {
	cin >> T;
	for(int t=1; t<=T; ++t) {
		result = 0;
		cin >> A >> B;
		for(n=A; n<B; ++n) {
			for(m=n+1; m<=B; ++m) {
				if(recycled()) { /*cout << n << " " << m << endl;*/ ++result; }
			}
		}
		cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}