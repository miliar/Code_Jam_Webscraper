#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

fstream in, out;

int t, a1, a2, b1, b2;

int win[3000][3000];

__int64 ans;

void write(int a, int b, int c) {
	if (a < 3000 && b < 3000) {
		win[a][b] = c;
	}
}

int val(int a, int b) {
	if (a >= 3000 || b >= 3000 || win[a][b] == -1) {
		if (a == b) {
			write(a, b, 0);		
			return 0;
		} else {
			if (a < b) {
				if (b <= 2*a) {
					write(a, b, 1-val(a, b - a));
					return 1-val(a, b - a);
				} else {
					write(a, b, 1);
					return 1;
				}
			} else {
				if (a <= 2*b) {
					write(a, b, 1-val(b, a - b));
					return 1-val(b, a - b);
				} else {
					write(a, b, 1);
					return 1;
				}
			}
		}
	} else {
		return win[a][b];
	}
	return 1;
}

int main() {
	in.open("prob3.in", fstream::in);
	out.open("prob3.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		in >> a1 >> a2 >> b1 >> b2;
		
		for (int j = 0; j < 3000; j++) {
			for (int k = 0; k < 3000; k++) {
				win[j][k] = -1;
			}
		}
		ans = 0;

		for (int x = a1; x <= a2; x++) {
			for (int y = b1; y <= b2; y++) {
				if (val(x, y) == 1) {
					ans++;
				}
			}
		}
		
		char asdf[50];
		_i64toa(ans, asdf, 10);
		out << "Case #" << i + 1 << ": ";
		out << asdf << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
