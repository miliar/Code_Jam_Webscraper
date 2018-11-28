#include <iostream>
#include <fstream>
#include <limits>
using namespace std;

int main()
{
	ifstream infile("C-large.in");
	ofstream outfile("output.txt");

	int test_cases = 0;
	infile >> test_cases;
	for (int round = 0; round < test_cases; round++) {
		int numbers[1000];
		int size = 0;
		int sum = 0;
		int xor_sum = 0;
		int min = std::numeric_limits<int>::max();

		infile >> size;
		for (int i = 0; i < size; i++) {
			infile >> numbers[i];
			sum += numbers[i];
			xor_sum = xor_sum ^ numbers[i];
			if (numbers[i] < min)
				min = numbers[i];
		}

		if (xor_sum != 0) {
			outfile << "Case #" << round+1 << ": NO" << endl;
		}
		else {
			outfile << "Case #" << round+1 << ": " << sum-min << endl;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}


