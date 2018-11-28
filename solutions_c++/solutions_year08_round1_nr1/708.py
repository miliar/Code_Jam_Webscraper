#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char** argv) {
	ifstream infile(argv[1]);

	int num_cases;
	infile >> num_cases;

	for(int i = 0; i < num_cases; i++) {
		int length;
		infile >> length;
		vector<int> v(length);
		vector<int> y(length);
		for(int j = 0; j < length; j++) {
			infile >> v[j];
		}
		for(int j = 0; j < length; j++) {
			infile >> y[j];
		}
		sort(v.begin(), v.end());
		sort(y.begin(), y.end());
		int sum = 0;
		for(int j = 0; j < length; j++) {
			sum += v[j]*y[length - j - 1];
		}
		cout << "Case #" << i + 1 << ": " << sum << endl;
	}

	return 0;
}
