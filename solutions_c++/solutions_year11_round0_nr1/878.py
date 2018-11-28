// basic IO

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int total_time = 0;
int prev_o_button = 1, prev_b_button = 1;
int o_time = 0, b_time = 0, o_step = 0, b_step = 0, b_total = 0, o_total = 0;
char robot;
int button;

void count_time () {
	// cout << button << " " << prev_b_button << endl;
	switch (robot) {
		case 'O':
			o_step = fabs((int)(button - prev_o_button));
			if (o_step > b_total)
				o_time = o_step - b_total + 1;
			else 
				o_time = 1;
			o_total += o_time;
			total_time += o_time;
			b_total = 0;
			prev_o_button = button;
			break;
		case 'B':
			b_step = fabs((int)(button - prev_b_button));
			if (b_step > o_total)
				b_time = b_step - o_total + 1;
			else
				b_time = 1;
			b_total += b_time;
			total_time += b_time;
			o_total = 0;
			prev_b_button = button;
			break;
		default:
			break;
	}
	cout << o_time << " " << b_time << " " << total_time << endl;
	return;
}

int main () {
	ifstream in_file;
	ofstream out_file;

	string line[150];
	
	/*
	in_file.open("input.txt");
	out_file.open("output.txt");
	*/
	
	
	in_file.open("A-large.in");
	out_file.open("A-large.out");
	
	
	int i = 0;
	char *terms;
	int num_terms;
	
	if (in_file.is_open()) {
		while(in_file.good()) {
			getline(in_file, line[i]);
			// cout << line[i] << endl;
			i++;
		}
		// cout << "Number of lines in the file: " << i << endl;
		// cout << "Number of cases: " << atoi(line[0].c_str()) << endl;
		
		for (int case_ctr = 1; case_ctr <= atoi(line[0].c_str()); case_ctr++) {
			terms = strtok((char*)(line[case_ctr].c_str()), " ");
			num_terms = atoi(terms);
			// cout << "Number of terms: " << num_terms << endl;
			terms = strtok (NULL, " ");
			while (terms != NULL) {				
				robot = terms[0];
				terms = strtok(NULL, " ");
				button = atoi(terms);
				switch (robot) {
					case 'O':
						// cout << "O: " << button << endl;
						count_time();
						break;
					case 'B':
						// cout << "B: " << button << endl;
						count_time();
						break;
					default:
						break;
				}
				terms = strtok(NULL, " ");
			}
			out_file << "Case #" << case_ctr << ": " << total_time << endl;
			cout << "Total time taken: " << total_time << endl;
			o_time = 0;
			o_step = 0;
			b_time = 0;
			b_step = 0;
			total_time = 0;
			b_total = 0;
			o_total = 0;
			prev_o_button = 1;
			prev_b_button = 1;
		}
	} else {
		cout << "Unable to open file";
	}
	in_file.close();
	out_file.close();

	return(0);
}