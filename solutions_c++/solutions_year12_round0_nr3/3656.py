#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

/*
 * Hirakendu Das. Google Code Jam 2012.
 *
 */

int main(int argc, char *argv[])
{
	// Parse arguments.
	string input_file;
	string output_file;
	int verbose_level = 2;
	string arg;
	stringstream input_args;
	for (int i = 1; i != argc; ++i) {
		input_args << " " << argv[i];
	}
	while (!input_args.eof()) {
		input_args >> arg;
		if (arg == "-i") {
			input_args >> input_file;
		} else if (arg == "-o") {
			input_args >> output_file;
		} else if (arg == "-v") {
			input_args >> verbose_level;
		}  else if (arg != "") {
			cout << "Error parsing argument \"" << arg
					<< "\"." << endl;
			return 0;
		}
	}
	if (input_file == "") {
		input_file = "input.txt";
	}
	if (output_file == "") {
		output_file = "output.txt";
	}

	ifstream input_stream(input_file.c_str());
	ofstream output_stream(output_file.c_str());

	// Scan inputs, run the algorithm, store the output.
	int num_cases;
	input_stream >> num_cases;
	if (verbose_level >= 2) {
	    cout << "  Number of test cases: " << num_cases << endl;
	}
	for (int i_case = 0; i_case != num_cases; ++i_case) {
		if  (verbose_level >= 1) {
		    cout << "  Case #: " << i_case + 1 << endl;
		}
		// 1. Declare and fetch various input variables here.
		int A, B;
		input_stream >> A >> B;
		// 1.1 Print out scanned input.
		cout << "(A,B) = (" << A << "," << B << ")" << endl;

		// 2. Algorithm.
		int r = ceil(log(B)/log(10));
		cout << "r = " << r << endl;
		int count = 0;
		int *n_i = new int[r];
		for (int n = A; n < B; ++n) {
			int n_copy = n;
			for (int i = 0; i != r; i++) {
				n_i[i] = n_copy % 10;
				n_copy /= 10;
			}
//			cout << n << " ";
//			for (int i = 0; i != r; ++i) {
//				cout << n_i[i];
//			}
//			cout << endl;
			cout << n;
			for (int l = 1; l <= r - 1; ++l) {
				int m = 0;
				for (int i = l; i <= r - 1; ++i) {
					m = 10 * m + n_i[r-1-i];
				}
				for (int i = 0; i <= l - 1; ++i) {
					m = 10 * m + n_i[r-1-i];
				}
				cout << " " << m << " ";
				if ((m > n) && (m <= B)) {
					count++;
				}
			}
			cout << endl;
		}

		cout << "count = " << count << endl;

		// 3. Output.
		output_stream << "Case #" << i_case + 1 << ": " << count << endl;
	}



	// Regular cleanup.
	input_stream.close();
	output_stream.close();


	return 0;
}
