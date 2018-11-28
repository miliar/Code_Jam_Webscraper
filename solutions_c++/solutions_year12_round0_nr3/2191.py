//============================================================================
// Name        : recyled_numbers.cpp
// Author      : Yoram Versluis
//============================================================================
#include <iostream>
#include <fstream>

#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <cstring>

using namespace std;

int sizeOfInt(int i) {
	int tmp = i, size = 0;
	while (tmp > 0) {
		tmp /= 10;
		size++;
	}
	return size;
}

const unsigned int pow10[] = { 1, 10, 100, 1000, 10000, 100000, 1000000,
		10000000 };

int recycleVariations(unsigned int a, unsigned int b, int size) {
	assert(a != b);

	int tmp = a;
	int res=0;

	for (int i = 0; i < size - 1; i++) {
		unsigned int mod = tmp % 10;
		tmp /= 10;
		tmp = tmp + (mod * pow10[size - 1]);
		if (tmp == a) //stop if we meet ourself again
			break;
		if (tmp > a && tmp <= b)
		{
			res++;
		}
	}

	return res;
}

int main(int argc, char **argv) {

	if (argc < 2) {
		cerr << "Usage: " << argv[0] << " <input_file>" << endl;
		return 1;
	}

	ifstream input(argv[1]);
	if (!input.is_open()) {
		cerr << "error opening " << argv[1] << endl;
		return 1;
	}

	//now the real work
	int testCases = 0;
	int c = 0;
	input >> testCases;
	cerr << "testCases: " << testCases << endl;

	unsigned int A, B;
	while (input.good() && c < testCases) {
		c++;
		input >> A >> B;

		int result = 0;
		int size = sizeOfInt(A);

		for (unsigned int x = A; x < B; x++) {
			result += recycleVariations(x, B, size);
		}

		cout << "Case #" << c << ": " << result << endl;
	}



	return 0;
}


