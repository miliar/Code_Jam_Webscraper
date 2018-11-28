// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <streambuf>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <ctype.h>

using namespace std;

typedef struct {
	pair<char, char> from;
	char to;
} Combination;

int _tmain(int argc, _TCHAR* argv[])
{
	vector<string> tests;
	string line;
	ifstream file_input("input.txt");
	bool skip_first = false;
	while(!file_input.eof()) {
		getline(file_input, line);
		if (skip_first)
			tests.push_back(line);
		else
			skip_first = true;
	}
	file_input.close();

	string output;

	int test_number = 1;
	for (vector<string>::iterator i = tests.begin(); i != tests.end(); ++i) {
		string test = *i;
		vector<pair<char, char>> opposed;
		vector<Combination> combines;
		vector<char> invokes;
		cout << endl <<  test << endl;

		int value = 0;
		int combinations = -1;
		int oppositions = -1;
		int read_number = false;
		Combination comb;
		comb.from.first = comb.from.second = comb.to = '~';
		pair<char, char> opp;
		opp.first = opp.second = '~';

		for (int c = 0; c < test.length(); c++) {
			if (isdigit(test[c])) {
				value = 10 * value + test[c] - 48;
				read_number = true;
			} else if (read_number && test[c] == ' ' && combinations == -1) {
				combinations = value;
				cout << "com: " << combinations << endl;
				value = 0;
				read_number = false;
			} else if (read_number && test[c] == ' ' && oppositions == -1) {
				oppositions = value;
				cout << "oppo: " << oppositions << endl;
				value = 0;
				read_number = false;
			} else if (isalpha(test[c])) {
				if (combinations > 0) {
					if (comb.from.first == '~') comb.from.first = test[c];
					else if (comb.from.second == '~') comb.from.second = test[c];
					else if (comb.to == '~') {
						comb.to = test[c];
						combines.push_back(comb);
						comb.from.first = comb.from.second = comb.to = '~';
						combinations--;
					}
				} else if (oppositions > 0) {
					if (opp.first == '~') opp.first = test[c];
					else if (opp.second == '~') {
						opp.second = test[c];
						opposed.push_back(opp);
						opp.first = opp.second = '~';
						oppositions--;
					}
				} else {
					invokes.push_back(test[c]);
				}
			}
		}

		vector<char> pool;
		for (vector<char>::iterator i = invokes.begin(); i != invokes.end(); ++i) {
			char invoke = *i;
			
			bool was_combined;
			do {
				was_combined = false;
				if (pool.size() == 0) {
					pool.push_back(invoke);
					continue;
				}

				// check if the last in pool combines with invoke
				for (vector<Combination>::iterator c = combines.begin(); c != combines.end(); ++c) {
					if ((c->from.first == pool.back() && c->from.second == invoke)
					 || (c->from.second == pool.back() && c->from.first == invoke)) {
						pool.pop_back();
						invoke = c->to; // repeat the cycle with the new element
						was_combined = true;
						break;
					}

					// check if the invoked combines
					// check if any in pool is opposite
				}
				if (was_combined) continue;

				bool was_opposed = false;
				// check if any in pool is opposite
				for (vector<pair<char, char>>::iterator c = opposed.begin(); c != opposed.end(); ++c) {
					for (vector<char>::iterator d = pool.begin(); d != pool.end(); ++d) {
						if ((c->first == *d && c->second == invoke)
						 || (c->second == *d && c->first == invoke)) {
							// clear pool
							 pool.clear();
							 was_opposed = true;
							 break;
						}
					}
					if (was_opposed) break;
				}
				if (was_opposed) continue;

				pool.push_back(invoke);
			} while (was_combined);
		}

		cout << "Case #: [";
		char buffer[2048];
		sprintf(buffer, "Case #%d: [", test_number);
		output += buffer;
		for (vector<char>::iterator i = pool.begin(); i != pool.end(); ++i) {
			cout << *i;
			output += *i;
			if (i + 1 != pool.end()) {
				cout <<  ", ";
				output += ", ";
			}
		}
		cout << "]" << endl;
		output += "]\n";
		test_number++;
	}
	


	cout << output;
	ofstream myfile;
	myfile.open ("output.txt");
	myfile << output;
	myfile.close();

	getchar();
	getchar();
	return 0;
}

