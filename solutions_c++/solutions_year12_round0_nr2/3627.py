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
		int N, S, p;
		input_stream >> N >> S >> p;
		int *t = new int[N];
		for (int i = 0; i != N; ++i) {
			input_stream >> t[i];
		}
		// 1.1 Print out scanned input.
		cout << N << "\t" << S << "\t" << p << "\t" << endl;
		for (int i = 0; i != N; ++i) {
			cout << t[i] << "\t";
		}
		cout << endl;

		// 2. Algorithm.
		int *max_score = new int[N];
		int num_good = 0, num_good_nosurprising = 0, num_bad_surprising_good = 0,
				num_bad_surprising_bad = 0;
		for (int i = 0; i != N; i++) {
			if (t[i] % 3 == 0) {
				max_score[i] = t[i] / 3;
			} else {
				max_score[i] = t[i] / 3 + 1;
			}
			if (max_score[i] >= p) {
				num_good++;
				if ((t[i] <= 1) && (t[i] >= 29)) {
					num_good_nosurprising++;
				}
			}

			if (max_score[i] < p) {
				// Its bad.
				if ((max_score[i] + 1 >= p) && (t[i] >= 2) && (t[i] <= 28)
						&& (t[i] % 3 != 1)) {
					num_bad_surprising_good++;
				}
			}

		}

		int num_good_all = num_good + min(S, num_bad_surprising_good);
		cout << "good: " << num_good << endl;
		cout << "min(S,bad_surprising_good): "
				<< min(S, num_bad_surprising_good) << endl;
		cout << num_good_all << endl;


		// 3. Output.

		output_stream << "Case #" << i_case + 1 << ": "
				<< num_good_all << endl;
		// 3.1 Cleanup.
		//delete[] var3;
	}



	// Regular cleanup.
	input_stream.close();
	output_stream.close();


	return 0;
}
