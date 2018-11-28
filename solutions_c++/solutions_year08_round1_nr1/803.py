#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
using namespace std;

bool natural(int one, int two) {
	return one < two;
}

bool unnatural(int one, int two) {
	return !natural(one, two);
}

int main(int argc, char const *argv[]) {
	int nCases;
	cin >> nCases;
	for (int n = 1; n <= nCases; n++) {
		int dimension;
		cin >> dimension;
		
		int first[dimension];
		for (int i = 0; i < dimension; i++) {
			cin >> first[i];
		}
		int second[dimension];
		for (int i = 0; i < dimension; i++) {
			cin >> second[i];
		}
		
		sort(first, first + dimension, natural);
		sort(second, second + dimension, unnatural);
		
		int sum = 0;
		for (int i = 0; i < dimension; i++) {
			sum += first[i] * second[i];
		}		
		
		cout << "Case #" << n << ": "
		     << sum << endl;
	}
	
	return 0;
}