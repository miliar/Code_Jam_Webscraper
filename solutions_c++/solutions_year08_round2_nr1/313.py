#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long lint;
typedef unsigned long long ulint;

void tabulate(ulint coordinates[3][3], ulint X, ulint Y) {
	coordinates[X%3][Y%3]++;
}

ulint choose(ulint n, unsigned k) {
	ulint num = 1;
	ulint denom = 1;
	for (unsigned i = 1; i <= k; i++) {
		num *= n - i + 1;
		denom *= i;
	}
	return num / denom;
}

int main(int argc, char const *argv[]) {
	unsigned nCases;
	cin >> nCases;
	for (unsigned N = 1; N <= nCases; N++) {
		ulint n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		A %= M;
		B %= M;
		C %= M;
		D %= M;
		
		ulint coordinates[3][3];
		for (int i = 0; i < 9; i++) {
			coordinates[i/3][i%3] = 0;
		}
		ulint X = x0;
		ulint Y = y0;
		tabulate(coordinates, X, Y);
		X %= M;
		Y %= M;
		for (ulint i = 1; i < n; i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			tabulate(coordinates, X, Y);
		}
		
		ulint count = 0;
		for (unsigned row = 0; row < 3; row++) {
			count += coordinates[row][0] * coordinates[row][1] * coordinates[row][2];
			for (unsigned col = 0; col < 3; col++) {
				count += choose(coordinates[row][col], 3);
			}
		}
		for (unsigned col = 0; col < 3; col++) {
			count += coordinates[0][col] * coordinates[1][col] * coordinates[2][col];
		}
		for (unsigned row = 0; row < 3; row++) {
			count += coordinates[row][0] * (coordinates[(row + 1)%3][1] * coordinates[(row + 2)%3][2]);
			count += coordinates[row][0] * (coordinates[(row + 2)%3][1] * coordinates[(row + 1)%3][2]);
		}
		
		cout << "Case #" << N << ": "
		     << count << endl;
	}
	
	return 0;
}