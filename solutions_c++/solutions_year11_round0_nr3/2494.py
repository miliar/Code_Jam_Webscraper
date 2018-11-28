#include <iostream>
#include <fstream>
#include <algorithm>
#include "next_combination.h"

using namespace std;

int patAdder(int a, int b) {
	int c = (a&b) << 1;
	return a + b - c;
}

int main(int argc, const char *argv[])
{
	// Exit if we dont have a filename
	if (argc != 2) return 1;
	
	int cases, candyNum, realMax, realVal1, realVal2, patVal1, patVal2;
	int* candy;
	
	ifstream input;
	input.open(argv[1]);

	input >> cases;

	for (int i = 0; i < cases; i++) {
		realMax = -1;

		input >> candyNum;
		candy = new int[candyNum];

		// read in candy vals
		for (int j = 0; j < candyNum; j++) {
			input >> candy[j];
		}

		sort(candy, candy+candyNum);

		for (int k = 1; k < candyNum/2+1; k++) {
				int z = 0;
			do {
				patVal1 = 0;
				z++;
				patVal2 = 0;
				realVal1 = 0;
				realVal2 = 0;

				for (int j = 0; j < candyNum; j++) {
					if (j < k) {
						patVal1 = patAdder(patVal1, candy[j]);
						realVal1 += candy[j];
					}
					else {
						patVal2 = patAdder(patVal2, candy[j]);
						realVal2 += candy[j];
					}
				}
				if (patVal1 == patVal2) {
					if (realVal1 > realMax) realMax = realVal1;
					if (realVal2 > realMax) realMax = realVal2;
				}
			} while (next_combination(candy, candy+k, candy+candyNum) && z < 500);
		}

		cout << "Case #" << i+1 << ": ";
		if (realMax == -1) {
			cout << "NO";
		}
		else {
			cout << realMax;
		}
		cout << endl;
		delete[] candy;
	}

	return 0;
}
