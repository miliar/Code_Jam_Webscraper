/*
 * qualify.cpp
 *
 *  Created on: May 7, 2011
 *      Author: Zeng
 */

#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

#include "qualify.h"
using namespace std;

void bot_trust() {
	ifstream infile;
	ofstream outfile;

	infile.open("A-large.in");
	outfile.open("A-large-out.txt");
	int case_num, pair_num;
	infile >> case_num;

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
				} else {
					total_time += (dist - (total_time - time_o)) + 1;
				}

				pos_o = button_num;
				time_o = total_time;
			} else {
				int dist = abs(button_num - pos_b);
				if ((total_time - time_b) > dist) {
					total_time++;
				} else {
					total_time += (dist - (total_time - time_b)) + 1;
				}

				pos_b = button_num;
				time_b = total_time;
			}

			//			cout << robot << " " << button_num << endl;
		}

		//		cout << "total_time " << total_time << endl;
		outfile << "Case #" << i + 1 << ": " << total_time << endl;
	}
	infile.close();
	outfile.close();
}

void magicka() {
	ifstream infile;
	ofstream outfile;

//	infile.open("B-large.in");
//	outfile.open("B-large-out.txt");
	infile.open("B-small-attempt1.in");
	outfile.open("B-small-out1.txt");
	int case_num;
	infile >> case_num;

//	1 SFU 1 SF 10 FSSSWWWWRF
//	[U, S, S, W, W, W, W, R, F]

	for (int i = 0; i < case_num; i++) {
		int combine_num, opp_num, character_num;
		string combine, opp, characters;
		combine = opp = characters = "";
		vector<char> char_vec;
		int clear_pos = -1;

		infile >> combine_num;
		if (combine_num != 0) {
			infile >> combine;
		}
		infile >> opp_num;
		if (opp_num != 0) {
			infile >> opp;
		}

		infile >> character_num;
		infile >> characters;
		char_vec.push_back(characters[0]);
		if (opp_num != 0) {
			if (characters[0] == opp[0] || characters[0] == opp[1]) {
				clear_pos = 0;
			}
		}

		for (int j = 1; j < character_num; j++) {
			char_vec.push_back(characters[j]);

			// check combine
			if (combine_num != 0) {
				int last = char_vec.size() - 1;
				if ( (char_vec[last-1] == combine[0] && char_vec[last] == combine[1]) ||
					 (char_vec[last-1] == combine[1] && char_vec[last] == combine[0])	) {
					char_vec.pop_back();
					char_vec.pop_back();
					char_vec.push_back(combine[2]);
					// reset clear_pos
					if (clear_pos == last-1) {
						clear_pos = -1;
					}
					characters[j] = combine[2];
				}
			}

			// check clear
			if (opp_num != 0) {
				if (clear_pos != -1) {
					if ( (char_vec[clear_pos] == opp[0] && char_vec.back() == opp[1]) ||
						 (char_vec[clear_pos] == opp[1] && char_vec.back() == opp[0]) ) {
						char_vec.clear();
						clear_pos = -1;
					}
				}
				else if (characters[j] == opp[0] || characters[j] == opp[1]) {
					clear_pos = char_vec.size() - 1;
				}
			}
		}

		// print the output
		cout << "Case #" << i+1 << ": " << "[";
		outfile << "Case #" << i+1 << ": " << "[";
		for (int g = 0; g < (int)char_vec.size(); ++g) {
			if (g == (int)char_vec.size()-1) {
				cout << char_vec[(int)char_vec.size()-1];
				outfile << char_vec[(int)char_vec.size()-1];
			}
			else {
				cout << char_vec[g] << ", ";
				outfile << char_vec[g] << ", ";
			}
		}
		cout << "]" << endl;
		outfile << "]" << endl;
	}
	infile.close();
	outfile.close();
}

void candy_split() {
	ifstream infile;
	ofstream outfile;

	infile.open("C-large.in");
	outfile.open("C-large-out.txt");
	int case_num, candy_num;
	infile >> case_num;

	for (int i = 0; i < case_num; i++) {
		infile >> candy_num;
		int candies[candy_num];
		int xor_sum = 0;
		for (int j = 0; j < candy_num; j++) {
			infile >> candies[j];
			xor_sum ^= candies[j];
		}

		if (xor_sum != 0) {
			cout << "Case #" << i + 1 << ": " << "NO" << endl;
			outfile << "Case #" << i + 1 << ": " << "NO" << endl;
		}
		else {
			// algorithm applies here
			std::sort(candies, candies + candy_num);
			int sean_maxsum = 0;
			for (int k = candy_num-1; k >=1; k--) {
				sean_maxsum += candies[k];
			}
			cout << "Case #" << i + 1 << ": " << sean_maxsum << endl;
			outfile << "Case #" << i + 1 << ": " << sean_maxsum << endl;
		}
	}
	infile.close();
	outfile.close();
}
