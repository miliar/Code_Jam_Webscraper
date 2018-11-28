#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> set_elems;
vector<int>::iterator it;

int num_tries = 0;

int main () {
	ifstream in_file;
	ofstream out_file;
	
	string line[220];
	int num_cases, i = 0, num_elems;
	char *elems;
	
	/*
	in_file.open("input_D.txt");
	out_file.open("output_D.txt");
	*/ 
	
	in_file.open("D-large.in");
	out_file.open("D-large.out");
	
	
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
	
	cout << num_cases << endl;
	for (int case_ctr = 1, line_ctr = 1; case_ctr <= num_cases; case_ctr++, line_ctr +=2) {
		num_elems = atoi(line[line_ctr].c_str());
		elems = strtok((char*)(line[line_ctr+1].c_str()), " ");				
		while (elems != NULL) {
			// cout << values << endl;
			set_elems.push_back(atoi(elems));
			elems = strtok (NULL, " ");				
		}
		
		
		out_file << "Case #" << case_ctr << ": ";
		cout << "Case #" << case_ctr << ": ";
		
		for (int index = 1; index <= num_elems; index++) {
			if (index ^ set_elems[index-1]) num_tries ++;
		}
		
		out_file << num_tries << endl;
		cout << num_tries << endl;
		
		num_tries = 0;
		set_elems.clear();
	}
	
	
	out_file.close();
	
	return (0);
}