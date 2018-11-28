#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

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
	string to_clear;
	getline(input_stream, to_clear);
	if (verbose_level >= 2) {
	    cout << "  Number of test cases: " << num_cases << endl;
	}
	for (int i_case = 0; i_case != num_cases; ++i_case) {
		if  (verbose_level >= 1) {
		    cout << "  Case #: " << i_case + 1 << endl;
		}
		// 1. Declare and fetch various input variables here.

		int var1 = 0;
		double var2 = 0;
		double *var3 = new double[5];
		double *var4 = new double[5 * 10];
		for (int i = 0; i != 5; i++) {
			// input_stream >> var3[i];
			for (int j = 0; j != 10; ++j) {
				// input_stream >> var4[i * 10 + j];
			}
		}
		string goog_line;
		getline(input_stream, goog_line);

		// 1.1 Print out scanned input.
		cout << goog_line << endl;
		// cout << var1 << "\t" << var2 << endl;
		for (int i = 0; i != 5; i++) {
			// cout << var3[i];
			for (int j = 0; j != 10; ++j) {
				// cout << var4[i][j];
			}
		}

		// 2. Algorithm.
		string trans_line(goog_line);
		int code[26] = {
				'y', //a
				'h', //b
				'e', //c
				's', //d
				'o', //e
				'c', //f
				'v', //g
				'x', //h
				'd', //i
				'u', //j
				'i', //k
				'g', //l
				'l', //m
				'b', //n
				'k', //o
				'r', //p
				'z', //q
				't', //r
				'n', //s
				'w', //t
				'j', //u
				'p', //v
				'f', //w
				'm', //x
				'a', //y
				'q', //z

		};
		for (int i = 0; i < goog_line.length(); i++) {
			if (goog_line[i] != ' ') {
				trans_line[i] = code[goog_line[i] - 'a'];
			}
		}
		cout << goog_line << endl;
		cout << trans_line << endl;
		cout << endl;



		// 3. Output.
		output_stream << "Case #" << i_case + 1 << ": "<< trans_line << endl;
		for (int i = 0; i < 5; i++) {
			// output_stream << var3[i] << endl;
			// cout << var3[i] << endl;
			for (int j = 0; j != 10; ++j) {
				// output_stream << var4[10 * i + j] << "\t";
				// cout << var4[10 * i + j] << "\t";
			}
			// output_stream << endl;
			// cout << endl;
		}
		// 3.1 Cleanup.
		delete[] var3;
		delete[] var4;
	}



	// Regular cleanup.
	input_stream.close();
	output_stream.close();


	return 0;
}
