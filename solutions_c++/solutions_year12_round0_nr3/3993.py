#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

vector<int> p10;

int digits(int num) {
	int d = 0;
	while(num != 0) {
		num /= 10;
		d++;
	}
	return d;
}
inline int back_to_front(int n, int m){
	return (n%p10[m])*p10[digits(n)-m]+n/p10[m];
}

int main(int argc, char *argv[])
{
	p10 = vector<int> (7);
	for (int i = 0; i < 7;  ++i) {
		p10[i] = pow(10, i);
	}
	int T;
	cin >> T;
	for (int caso = 1; caso <= T; ++caso) {
		int a, b;
		cin >> a >> b;
		int cont = 0;

		for (int k = a; k <= b; ++k) {
			vector<int> v(digits(k));
			bool repe = false;
			int parejas = 0;
			for (int d = 1; d < digits(k); ++d) {
				int NUM = back_to_front(k, d);
				if (NUM > k and NUM <= b ) {
					if (parejas > 0) {
						for (int l = 0; l < parejas; ++l) {
							if (NUM == v[l]) repe = true;							
						}
					}
					if (not repe) {
						v[parejas] = back_to_front(k, d);
						parejas++;					
						cont++;
					}
					else repe = false;
				}
			}
		}
		cout << "Case #" << caso << ": " << cont << endl;
	}
	return 0;    
}
