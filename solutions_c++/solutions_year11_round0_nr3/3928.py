#include <iostream>
#include <cmath>
#include <map>
#include <vector>

using namespace std;

int v[1000];

int calc(int xorA, int xorB, int sumA, int sumB, int n) {
	if (n < 0 && xorA && xorB && xorA == xorB) {
		return max(sumA, sumB);
	} else if (n < 0) {
		return 0;
	} else {
		int giveA = calc(xorA ^ v[n], xorB, sumA + v[n], sumB, n-1);
		int giveB = calc(xorA, xorB ^ v[n], sumA, sumB + v[n], n-1);
		return max(giveA, giveB);
	}
}

int main() {
	int cases;
	cin >> cases;
	
	for (int c = 1; c <= cases; c++) {
		int candies, current;
		cin >> candies;
		
		for (int i = 0; i < candies; i++)
			cin >> v[i];
		
		int better = calc(0, 0, 0, 0, candies-1);
		
		if (better)
			cout << "Case #" << c << ": " << better << endl;
		else
			cout << "Case #" << c << ": NO" << endl;
	}
	
	return 0;
}
