#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

vector<string> GetStrings(ifstream &infile, int num_strings) {
	vector<string> list;
	for (int i = 0; i < num_strings; ++i) {
		string combination;
		infile >> combination;
		list.push_back(combination);
	}
	return list;
}

string checkCombination(string to_check, vector<string> &combinations) {
	string new_sequence;
	string reverse_check(to_check.rbegin(),to_check.rend());
	for (size_t i = 0; i < combinations.size(); ++i) {
		string cur_combination = combinations[i].substr(0,2);
		if (cur_combination.find(to_check) != string::npos || cur_combination.find(reverse_check) != string::npos) {
			new_sequence += combinations[i].at(2);
		}
	}
	return new_sequence;
}

bool oppositionExists(string cur_list, vector<string> &oppositions) {
	for (size_t i = 0; i < oppositions.size(); ++i) {
		string cur_op = oppositions[i];
		if (cur_list.find(cur_op[0]) != string::npos && cur_list.find(cur_op[1]) != string::npos) return true;
	}
	return false;
}

string GetFinalElementList(ifstream &infile, vector<string> &combinations, vector<string> &oppositions, int num_elements) {
	string init_list;
	int cur_string_index = 0;
	infile.get();
	for (int i = 0; i < num_elements; ++i) {
		init_list += infile.get();
		if (init_list.size() > 1) {
			string new_comb = checkCombination(init_list.substr(cur_string_index-1,2), combinations);
			if (!new_comb.empty()) {
				init_list.replace(cur_string_index-1,2,new_comb);
				cur_string_index--;
			} else if (oppositionExists(init_list,oppositions)) {
				init_list.clear();
				cur_string_index = -1;
			}
		}
		cur_string_index++;
	}
	return init_list;
}

int main() {
	string file_name = "/Users/sameerarya/Documents/CodeJamInput/B-large.in.txt";
	ifstream infile(file_name.c_str());
	ofstream outfile("magickaoutput.txt");
	if (!infile.is_open()) cout << "ERROR" << endl;
	size_t num_cases;
	infile >> num_cases;
	for (size_t i = 1; i <= num_cases; ++i) {
		int num_combinations, num_oppositions, num_elements;
		infile >> num_combinations;
		vector<string> combinations = GetStrings(infile, num_combinations);

		infile >> num_oppositions;
		vector<string> oppositions = GetStrings(infile, num_oppositions);
		infile >> num_elements;
		string final_list = GetFinalElementList(infile, combinations, oppositions, num_elements);
		//cout << "Final List: " << final_list << endl;
		outfile << "Case #" << i << ": [";
		for (size_t j = 0; j < final_list.size(); ++j) {
			if (j > 0) outfile << ", ";
			outfile << final_list[j];
		}
		outfile << "]" << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}
