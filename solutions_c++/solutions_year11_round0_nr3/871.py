#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

vector<int> set_values;
vector<int>::iterator it;

// set<int> s_set, p_set;
int s_xor, p_xor, set_xor;
bool sol_exists;
int best_solution = 0;


void get_xor(int index) {
	it = set_values.begin() + index;
	set_xor = *it;
	for (it = set_values.begin()+index+1; it != set_values.end(); it++) {
		set_xor ^= *it;
	}
	// cout << set_xor << endl;
	return;
}


int main () {
	ifstream in_file;
	ofstream out_file;
	
	string line[2010];
	int num_cases, i = 0, num_candies;
	char *values;
	
	/*
	in_file.open("input_C.txt");
	out_file.open("output_C.txt");
	 */
	
	in_file.open("C-large.in");
	out_file.open("C-large.out");
	
	
	if (in_file.is_open()) {
		while(in_file.good()) {
			getline(in_file, line[i]);
			// cout << line[i] << endl;
			i++;
		}
	} else {
		cout << "Unable to open file";
	}
	in_file.close();
	
	num_cases = atoi(line[0].c_str());
	for (int case_ctr = 1, line_ctr = 1; case_ctr <= num_cases; case_ctr++, line_ctr +=2) {
		num_candies = atoi(line[line_ctr].c_str());
		values = strtok((char*)(line[line_ctr+1].c_str()), " ");				
		while (values != NULL) {
			// cout << values << endl;
			set_values.push_back(atoi(values));
			values = strtok (NULL, " ");				
		}
		get_xor(0);
		out_file << "Case #" << case_ctr << ": ";
		cout << "Case #" << case_ctr << ": ";
		if (set_xor != 0) {
			out_file << "NO" << endl;
			cout << "NO" << endl;
		} else {
			sort(set_values.begin(), set_values.end());
			get_xor(1);
			// cout << set_xor << endl;
			
			if (set_xor == set_values[0]) {
				for (int i = 1; i < set_values.size(); i++)
					best_solution += set_values[i];
				out_file << best_solution << endl;
				cout << best_solution << endl;
			}
		}
		best_solution = 0;		
		set_values.clear();
	}
	
	
	out_file.close();
	
	return (0);
}