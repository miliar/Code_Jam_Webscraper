#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;


float multiply_members(float p[], int len) {
	int iter = 0;
	float res = 1;
	for (iter=0; iter < len; iter++) {
		res = res * p[iter];
	}
	//cout << "------   " << res << "   ----" <<  endl;
	return res;
}



float solve_case(int A, int B, float probs[]) {
	double amount_permutations = 2^A;

	float expected_keep_typing = 0.0;
  float all_correct_prob = multiply_members(probs, A);
	float some_error_prob = 1 - all_correct_prob;
	double remaining_chars = B-A+1;
	double stupid_typing = remaining_chars + B + 1;

	//cout << remaining_chars << " * " << all_correct_prob << " ::: " << stupid_typing << "*" << some_error_prob << endl;

	expected_keep_typing = (remaining_chars * all_correct_prob) + (stupid_typing * some_error_prob); // <<<
	
	float expected_enter = B+2; // <<<

	float expected_with_backspace_OK[A];
	float expected_with_backspace[A];
	float expected_with_backspace_stupid[A];

	float min_backspace = -1;
	int x = 1;
	for(x = 1; x <= A; x++) {
		// I've typed A characters already.
		// Their probabilities to be correct are stored in probs[]
		// I hit x backspaces.
		// P1 P2 P3 P4 P5
		// TT TT TT 
		// Prob of having all right: P1+P2+P3

		int typed_chars = A;
		expected_with_backspace[x] = x ; // I hit the backspaces
		typed_chars -= x;
		expected_with_backspace[x] += (B - typed_chars) + 1; // Then fill the password and ENTER

		//cout << " >> Typing " << x << " backspaces... ";
		// expected_with_backspace[x] happens with some probabiliy...
			int tmpz = 0;
			float sum_cleared = 1;
			float sum_stupid = 0;
			int tmp_typed = A-x;
			//cout << " [clear=0..." << tmp_typed << "] ";
			if (tmp_typed > 0) {
				for(tmpz=0; tmpz < tmp_typed; tmpz++) {
					sum_cleared *= probs[tmpz];
				}
			}
			sum_stupid = 1 - sum_cleared;

		// Did I leave some wrong chars without deleting? I need to type B chars and Enter
		expected_with_backspace_stupid[x] = expected_with_backspace[x];
		expected_with_backspace_stupid[x] += B+1;
		//cout << "Got rid of errors?: " << expected_with_backspace[x] << " strokes (" << sum_cleared << ")" << endl;
		//cout << " _ _ _ Still errors?" << expected_with_backspace_stupid[x] << " strokes (" << sum_stupid << ")" << endl;

		expected_with_backspace_OK[x] = (expected_with_backspace[x] * sum_cleared) + (expected_with_backspace_stupid[x] * sum_stupid);

		if (min_backspace == -1) { 
			min_backspace = expected_with_backspace_OK[x];
		} else {
			if (expected_with_backspace_OK[x] < min_backspace) {
				min_backspace = expected_with_backspace_OK[x];
			}
		}

	}
	
	float ret = min_backspace;
	if (expected_keep_typing < ret) {
		 ret = expected_keep_typing;
	}

	if (expected_enter < ret) {
		 ret = expected_enter;
	}
	return ret;
}

int main(int argc, char* argv[]) {
	// Init vars
	char szInput [256];
	fgets ( szInput, 256, stdin );

	// Load number of test cases
	int iCases = atoi(szInput);

	// Iterate through test cases:
	int i = 0;
	for(i = 0; i < iCases; i++) {

		// Get the current line
		string cur_line;
		int typed_chars, total_chars;

		// Parse the case parameters
		getline(cin, cur_line);
		istringstream iss(cur_line);
			iss >> typed_chars;
			iss >> total_chars;

		// Parse the probabilities for this test case:
		getline(cin, cur_line);
		istringstream iss2(cur_line);
		float probabilities[typed_chars];
		int x = 0;
	 	float tmp = 0.0;

		for(x = 0; x < typed_chars; x++) {
			iss2 >> tmp;
			probabilities[x] = tmp;
		}

		// Solve case 
		float res;
		res = solve_case(typed_chars, total_chars, probabilities);

		// Build the output
		cout << "Case #" << (i+1) << ": ";
		cout.precision(6);
		cout.setf(ios::fixed,ios::floatfield); // floatfield set to fixed
		cout << res;
		//cout << " -- " << cur_line;
		cout << "\n";
	}
}
