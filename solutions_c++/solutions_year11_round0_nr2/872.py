
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int num_c_pairs, num_o_pairs, num_letters;
char *cpairs[40], *opairs[30], cresult[40];

vector<char> list;

void create_list(char letter) {
	char *ptr;
	int f1, f2;
	if (list.size() == 0) {
		list.push_back(letter);
	} else {
		if (num_c_pairs == 0 && num_o_pairs == 0) {
			list.push_back(letter);
		} else {
			cout << "COMBINATIONS" << endl;
			for (int c_ctr = 0; c_ctr < num_c_pairs; c_ctr++) {
				cout << list.back() << " " << letter << endl;
				if ( (cpairs[c_ctr][0] == list.back() && cpairs[c_ctr][1] == letter) ||
					(cpairs[c_ctr][1] == list.back() && cpairs[c_ctr][0] == letter) ) {
					/*
					 ptr = strchr(cpairs[c_ctr], list.back());
					 if (ptr != NULL) f1 = ptr - cpairs[c_ctr];
					 else f1 = 99;
					 ptr = strrchr(cpairs[c_ctr], letter);
					 if (ptr != NULL) f2 = ptr - cpairs[c_ctr];
					 else f2 = 99;
					 cout << f1 << " " << f2 << endl;
					 if (f1 < 2 && f2 < 2 && f1 != f2) {*/
					cout << "Found combination" << endl;
					list.pop_back();
					list.push_back(cresult[c_ctr]);
					return;
				}
			}
						
			if (num_o_pairs == 0) {
				list.push_back(letter);
			} else {
				cout << "OPPOSING" << endl;
				for (int ctr = 0; ctr < list.size(); ctr++) {
					for (int o_ctr = 0; o_ctr < num_o_pairs; o_ctr++) {
						cout << list[ctr] << " " << letter << endl;
						if ( (opairs[o_ctr][0] == list[ctr] && opairs[o_ctr][1] == letter) ||
							(opairs[o_ctr][1] == list[ctr] && opairs[o_ctr][0] == letter) ) {
							/*
							 ptr = strchr(opairs[o_ctr], list[ctr]);
							 if (ptr != NULL) f1 = ptr - opairs[o_ctr];
							 else f1 = 99;
							 ptr = strrchr(opairs[o_ctr], letter);
							 if (ptr != NULL) f2 = ptr - opairs[o_ctr];
							 else f2 = 99;
							 cout << f1 << " " << f2 << endl;
							 if (f1 < 2 && f2 < 2 && f1 != f2) {*/
							cout << "Found opposing" << endl;
							list.clear();
							return;
						}
					}
				}
				list.push_back(letter);
				return;
			}
		}
	}
	return;
}

int main () {
	ifstream in_file;
	ofstream out_file;
	
	string line[110];
	int num_cases, i = 0, num_terms;
	char *terms;
	
	/*
	in_file.open("input_B.txt");
	out_file.open("output_B.txt");
	*/
	
	in_file.open("B-large.in");
	out_file.open("B-large.out");
	
	
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
	
	for (int case_ctr = 1; case_ctr <= num_cases; case_ctr++) {
		terms = strtok((char*)(line[case_ctr].c_str()), " ");
		num_c_pairs = atoi(terms);
		cout << "Combination Pairs: " << num_c_pairs << endl;
		i = 0;
		for (int c_ctr = 0; c_ctr < num_c_pairs; c_ctr++) {
			terms = strtok (NULL, " ");
			cpairs[i] = (char*) malloc(2);
			strncpy(cpairs[i], terms, 2);
			cresult[i] = terms[2];
			// cout << cpairs[i] << " " << cresult[i] << endl;
			i++;			
		}
		terms = strtok (NULL, " ");
		num_o_pairs = atoi(terms);
		cout << "Opposing Pairs: " << num_o_pairs << endl;
		i = 0;
		for (int o_ctr = 0; o_ctr < num_o_pairs; o_ctr++) {
			terms = strtok (NULL, " ");
			opairs[i] = terms;
			// cout << opairs[i] << endl;
			i++;
		}
		terms = strtok (NULL, " ");
		num_letters = atoi(terms);
		cout << "Letters: " << num_letters << endl;
		i = 0;
		terms = strtok (NULL, " ");
		
		for (int l_ctr = 0; l_ctr < num_letters; l_ctr++) {			
			cout << terms[l_ctr] << endl;
			
			create_list(terms[l_ctr]);
		}
		
		if ( !list.empty() ) {
			cout << "Case #" << case_ctr << ": [";
			out_file << "Case #" << case_ctr << ": [";
			for (i = 0; i < list.size() - 1; i++) {
				cout << list[i] << ", ";
				out_file << list[i] << ", ";
			}
			cout << list.back() << "]" << endl;
			out_file << list.back() << "]" << endl;
			list.clear();
		} else {
			out_file << "Case #" << case_ctr << ": []" << endl;
		}
	}
	
	
	out_file.close();
	
	return (0);
}