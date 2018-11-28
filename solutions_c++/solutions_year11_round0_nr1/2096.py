/**
 *Bot Trust
 */
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");

	int test_cases = 0;

	infile >> test_cases;
	for (int round = 0; round < test_cases; round++) {
		int length;
		int seq[100];
		char robot[100];
		infile >> length;
		for (int i = 0; i < length; i++) {
			infile >> robot[i] >> seq[i];
		}

		int pos_o = 1;
		int pos_b = 1;
		int time_count = 0;
		char last_robot;
		int last_time = 0;

		if (robot[0] == 'O') {
			time_count += seq[0] - pos_o + 1;
			pos_o = seq[0];
			last_robot = 'O';
			last_time = time_count;
		}
		else {
			time_count += seq[0] - pos_b + 1;
			pos_b = seq[0];
			last_robot = 'B';
			last_time = time_count;
		}
		int i = 1;
		while (i < length) {
			if (robot[i] == 'O') {
				int waste = 0;
				if (last_robot == 'B') {
					waste = std::abs(seq[i] - pos_o) - last_time > 0 ?
						abs(seq[i] - pos_o) - last_time : 0;
					waste += 1;
					last_time = waste;
				}
				else {
					waste = abs(seq[i] - pos_o) + 1;
					last_time += waste;
				}
				pos_o = seq[i];
				time_count += waste;
				last_robot = 'O';
			}
			else {
				int waste = 0;
				if (last_robot == 'O') {
					waste = abs(seq[i] - pos_b) - last_time > 0 ?
						abs(seq[i] - pos_b) - last_time : 0;
					waste += 1;
					last_time = waste;
				}
				else {
					waste = abs(seq[i] - pos_b) + 1;
					last_time += waste;
				}
				pos_b = seq[i];
				time_count += waste;
				last_robot = 'B';
			}
			i++;
		}

		outfile << "Case #" << round + 1 << ": " << time_count << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}



