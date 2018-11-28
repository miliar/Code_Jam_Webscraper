//============================================================================
// Name        : codejam11.cpp
// Author      : Jiaan
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream infile;
	ofstream outfile;

	infile.open("A-large.in");
	outfile.open("A-large-out.txt");
	int case_num, pair_num;
	infile >> case_num;

//	O 2 B 1 B 2 O 4

	int total_time, pos_o, pos_b, time_o, time_b;
	for (int i = 0; i < case_num; i++) {
		total_time = 0;
		pos_o = pos_b = 1;
		time_o = time_b = 0;

		infile >> pair_num;
		for (int j = 0; j < pair_num; j++) {
			string robot;
			int button_num;
			infile >> robot;
			infile >> button_num;

			// the algorithm applies here
			if (robot == "O") {
				int dist = abs(button_num - pos_o);
				if ((total_time - time_o) > dist) {
					total_time++;
				}
				else {
					total_time += (dist - (total_time - time_o)) + 1;
				}

				pos_o = button_num;
				time_o = total_time;
			}
			else {
				int dist = abs(button_num - pos_b);
				if ((total_time - time_b) > dist) {
					total_time++;
				}
				else {
					total_time += (dist - (total_time - time_b)) + 1;
				}

				pos_b = button_num;
				time_b = total_time;
			}

//			cout << robot << " " << button_num << endl;
		}

//		cout << "total_time " << total_time << endl;
		outfile << "Case #" << i+1 << ": " << total_time << endl;
	}
	return 0;
}
