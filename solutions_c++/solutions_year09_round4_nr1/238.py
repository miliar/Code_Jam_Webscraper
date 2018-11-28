#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int T;

fstream in, out;

int N;

int vals[40];

void swap(int x, int y) {
	int temp = vals[x];
	vals[x] = vals[y];
	for (int i = y; i > x+1; i--) {
		vals[i] = vals[i-1];
	}
	vals[x+1] = temp;
}

int main() {
	in.open("prob1.in", fstream::in);
	out.open("prob1.out", fstream::out);
	in >> T;

	char temp;
	int last;
    for (int i = 0; i < T; i++) {
		in >> N;
		for (int j = 0; j < N; j++) {
			last = -1;
			for (int k = 0; k < N; k++) {
				in >> temp;
				if (temp == '1') {
					last = k;
				}
			}
			vals[j] = last;
		}

		int ans = 0;
		for (int x = 0; x < N; x++) {
			for (int y = x; y < N; y++) {
				if (vals[y] <= x) {
					ans += y - x;
					if (x != y) {
						swap(x, y);
					}
					y = N + 1;
				}
			}
		}

		out << "Case #" << i + 1 << ": " << ans << endl;
    }
    
	in.close();
	out.close();

	return 0;
}
