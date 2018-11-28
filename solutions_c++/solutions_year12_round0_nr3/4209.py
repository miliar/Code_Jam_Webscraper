#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <math.h>

using namespace std;

int minBound;
int maxBound;

int countPair(int num) {
	int temp = num;
	int length = 0;
	int prev = num;
	int curr = -1;
	int counter = 0;
	if (num < 10)
		return 0;
	
	while (temp > 0) {
		temp /= 10;
		length ++;
	}

	while (prev != num || curr < 0) {
		if (prev / (int)pow(10.0, length - 1) == 0) {
			curr = prev * 10;
		}
		else {
			curr = (prev % (int)pow(10.0, length - 1)) * 10 + prev / (int)pow(10.0, length - 1);
		}

		if (curr <= maxBound && curr >= minBound && curr > num) {
			counter ++;
		}
		prev = curr;
	}

	return counter;
}

int main() {
	int tests;
	cin >> tests;
	int round = 0;
	int * result = new int[tests];

	while(round < tests) {
		cin >> minBound;
		cin >> maxBound;

		int total = 0;
		for (int i = minBound; i <= maxBound; i ++) {
			total += countPair(i);
		}

		result[round] = total;
		round ++;
	}

	for (int i = 0 ; i < round; i ++) {
		cout << "Case #" << (i + 1) << ": " << result[i] << endl;
	}

	delete[] result;
	system("PAUSE");
	return 0;
}