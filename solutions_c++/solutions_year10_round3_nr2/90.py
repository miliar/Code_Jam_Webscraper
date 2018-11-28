#include <iostream>
using namespace std;

typedef long long ll;

int main() {
	int nt, it;
	
	for (cin >> nt, it = 0; it < nt; it++) {
		ll l, p, c, i, r;
		
		cin >> l >> p >> c;
		for (i = 0; l * c < p; i++) l *= c;
		for (r = 0; i; r++) i /= 2;
		
		cout << "Case #" << it + 1 << ": " << r << '\n';
	}
	
	return 0;
}
