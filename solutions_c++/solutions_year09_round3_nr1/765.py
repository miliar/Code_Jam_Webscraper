#include <iostream>
using namespace std;

#define LARGE

#ifndef LARGE

const int MAX_NUMBER_SIZE = 10;

#else

const int MAX_NUMBER_SIZE = 61;

#endif

//data
char number[MAX_NUMBER_SIZE];
long long result;
long long map[255];

void init() {
	for (int i = 0; i < 255; i++) {
		map[i] = -1;
	}
}

void compute() {
	char number2[MAX_NUMBER_SIZE];
	char * sign = number;
	int number_size = 0;
	long long digit = 0;
	while (*sign != '\0') {
		unsigned int index = (unsigned int) *sign;
		if (map[index] != -1) {
			number2[number_size] = map[index];
		} else {
			map[index] = digit++;
			if (map[index] == 1 || map[index] == 0) {
				map[index] = 1 - map[index];
			}
			number2[number_size] = map[index];
		}
		sign++;
		number_size++;
	}

	//number2[number_size] = '\0';
	//cout << "number2: " << number2 << "\n";

	if (digit == 1) {
		digit = 2;
	}
	result = 0;
	long long multiplier = 1;
	for (int i = number_size-1; i >= 0; i--) {
		result += number2[i] * multiplier;
		multiplier *= digit;
	}
}

int main() {
	cin.tie(NULL);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> number;
		init();
		compute();
		cout << "Case #" << i+1 << ": " << result << "\n";
	}

	cout.flush();

	return 0;
}
