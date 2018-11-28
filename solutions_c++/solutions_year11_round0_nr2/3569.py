//============================================================================
// Name        : eldavojohn
// Author      : 
// Version     :
// Copyright   : Whoever wants it gets it for whatever reason!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main() {
	int case_count = 0, case_ind = 0;
	char *tokens, *combination, *opposition, *input_str;
	string rd_line;
	ifstream input_txt("B-large.in");
	ofstream output_txt("B-large.out");

	if (input_txt.is_open()) {

		// always assume at least one line with # of examples
		getline(input_txt, rd_line);
		case_count = atoi((char *) rd_line.c_str());

		// while the file is still good and the case count has not been maxxed
		while (input_txt.good() && case_count > case_ind) {
			int comb_count = 0, opp_count = 0, comb_ind = 0, opp_ind = 0,
					input_len = 0;
			int comb_seq[36][3] = { { 0 } }, opp_seq[28][2] = { { 0 } };
			getline(input_txt, rd_line);
			// tokenize string
			tokens = strtok((char *) rd_line.c_str(), " ");
			comb_count = atoi(tokens);
			// printf("We have %i combination strings.\n", comb_count);
			tokens = strtok(NULL, " ");
			while (comb_ind < comb_count) {
				// combination
				combination = tokens;
				tokens = strtok(NULL, " ");

				// load into master arrays
				// printf("combination string %i is %s\n", comb_ind, combination);
				comb_seq[comb_ind][0] = combination[0];
				comb_seq[comb_ind][1] = combination[1];
				comb_seq[comb_ind][2] = combination[2];
				comb_ind++;
			}
			opp_count = atoi(tokens);
			// printf("We have %i opposition strings.\n", opp_count);
			tokens = strtok(NULL, " ");
			while (opp_ind < opp_count) {
				// combination
				opposition = tokens;
				tokens = strtok(NULL, " ");

				// load into master arrays
				// printf("opposition string %i is %s\n", opp_ind, opposition);
				opp_seq[opp_ind][0] = opposition[0];
				opp_seq[opp_ind][1] = opposition[1];
				opp_ind++;
			}
			input_len = atoi(tokens);
			// printf("We have a string of length %i.\n", input_len);
			tokens = strtok(NULL, " ");
			input_str = tokens;
			// printf("And that string is %s.\n", input_str);

			int i = 1, iter = 0, str_iter = 0;
			string working_str = "";
			working_str.append(input_str, 0, 1);
			while (input_len > i) {
				working_str.append(input_str, i, 1);
				// check the total string against all combinations
				bool clean = false;
				while (!clean) {
					clean = true;
					for (iter = 0; iter < comb_count; iter++) {
						// does it match?
						if (working_str.length() > 1) {
							if ((comb_seq[iter][0]
									== (int) working_str[working_str.length()
											- 2] && comb_seq[iter][1]
									== (int) working_str[working_str.length()
											- 1]) || (comb_seq[iter][1]
									== (int) working_str[working_str.length()
											- 2] && comb_seq[iter][0]
									== (int) working_str[working_str.length()
											- 1])) {
								working_str[working_str.length() - 2]
										= (char) comb_seq[iter][2];
								working_str.erase(working_str.length() - 1);
								clean = false;
							}
						}
					}
				}

				for (iter = 0; iter < opp_count; iter++) {
					// does it match?
					if (working_str.length() > 1) {
						if (opp_seq[iter][0]
								== (int) working_str[working_str.length() - 1]) {
							for (str_iter = working_str.length() - 2; str_iter
									>= 0; str_iter--) {
								if ((int) working_str[str_iter]
										== opp_seq[iter][1]) {
									working_str.erase(0);
									clean = false;
								}
							}
						}
						if (opp_seq[iter][1]
								== (int) working_str[working_str.length() - 1]) {
							for (str_iter = working_str.length() - 2; str_iter
									>= 0; str_iter--) {
								if ((int) working_str[str_iter]
										== opp_seq[iter][0]) {
									working_str.erase(0);
									clean = false;
								}
							}
						}
					}
				}

				i++;
			}
			case_ind++;

			// format string for output
			string results = "";
			if (working_str.length() > 0) {
				results.append(working_str, 0, 1);
			}
			for (iter = 1; iter < (int) (working_str.length()) - 1; iter++) {
				results.append(", ", 0, 2);
				results.append(working_str, iter, 1);
			}
			if (working_str.length() > 1) {
				results.append(", ", 0, 2);
				results.append(working_str, working_str.length() - 1, 1);
			}

			printf("Case #%i: [%s]\n", case_ind, results.c_str());
			output_txt << "Case #" << case_ind << ": [" << results << "]\n";
		}
	}
	input_txt.close();
	output_txt.close();

	return 0;
}
