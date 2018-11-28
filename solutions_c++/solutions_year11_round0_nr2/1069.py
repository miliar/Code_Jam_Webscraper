#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

const int ASCII_CONVERSION_CONSTANT = 65;
class MagickaRules {
public:
	int combine_rules[26][26]; // indices A = 0, B = 1; but values are 'A', 'B',...
	bool destroy_rules[26][26]; // indices A = 0, B = 1; but values are 0, 1
	vector<char> stack;
	
	MagickaRules() {
		for (int i = 0; i < 26; i++) {
			for (int j = 0; j < 26; j++) {
				combine_rules[i][j] = 0; //
				destroy_rules[i][j] = false; // no destroy
			}
		}
	}
	
	void process_combination(string s) {
		int from1 = s[0]-ASCII_CONVERSION_CONSTANT;
		int from2 = s[1]-ASCII_CONVERSION_CONSTANT;
		char to = s[2];
		combine_rules[from1][from2] = to;
		combine_rules[from2][from1] = to;
	}
	
	void process_opposition(string s) {
		int char1 = s[0]-ASCII_CONVERSION_CONSTANT;
		int char2 = s[1]-ASCII_CONVERSION_CONSTANT;
		destroy_rules[char1][char2] = true;
		destroy_rules[char2][char1] = true;
	}
	
	bool check_combination_and_replace(char c1, char c2) {
		int i1 = c1-ASCII_CONVERSION_CONSTANT;
		int i2 = c2-ASCII_CONVERSION_CONSTANT;
		if (combine_rules[i1][i2] != 0) {
			stack.pop_back();
			stack.pop_back();
			stack.push_back(combine_rules[i1][i2]);
			return true;
		}
		return false;
	}
		
	void check_opposition() {
		int last = stack[stack.size()-1] - ASCII_CONVERSION_CONSTANT;
		for (int i = 0; i < stack.size() - 1; i++) {
			int curr = stack[i] - ASCII_CONVERSION_CONSTANT;
			if (destroy_rules[last][curr]) {
				stack.clear();
				break;
			}
		}
	}
	
	// note: we know there will be NO chain reactions because of the given problem statement
	string process_input(string in) {
		for (int i = 0; i < in.length(); i++) {
			stack.push_back(in[i]);
			int size = stack.size();
			if (size >= 2) {
				if (check_combination_and_replace(stack[size-2], stack[size-1])) {
					// no need to check for chain reaction
				} else {
					check_opposition();
				}
			}
		}
		
		string output = "[";
		for (int i = 0; i < stack.size(); i++) {
			//cout << stack[i] << endl;
			
			output.push_back(stack[i]);
			output = output + ", ";
		}
		if (stack.size() != 0) {
			output = output.substr(0, output.size()-2);
		}
		
		output = output + "]";
		return output;
		
	}
	
};

int main(int argc, const char* argv[])  {
    ofstream fout ("magicka.out");
    ifstream fin ("magicka.in");

	int trials;
	fin >> trials;
	
	for (int i = 1; i <= trials; i++) {
		MagickaRules mr;
		
		int num_combinations;
		fin >> num_combinations;
		
		for (int j = 1; j <= num_combinations; j++) {
			string next_combination;
			fin >> next_combination;
			
			mr.process_combination(next_combination);
		}
				
		int num_oppositions;
		fin >> num_oppositions;
		
		for (int j = 1; j <= num_oppositions; j++) {
			string next_oppositions;
			fin >> next_oppositions;
			
			mr.process_opposition(next_oppositions);
		}
		
		int input_length;
		fin >> input_length; // kind of useless
		
		string input;
		fin >> input;
		string output = mr.process_input(input);
		
		cout << "Case #" << i << ": " << output << endl;
		fout << "Case #" << i << ": " << output << endl;
	}

}
