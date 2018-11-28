// Bot Trust.cpp : Defines the entry point for the console application.
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


using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	string input;
	string line;
	ifstream file_input("input.txt");
	while(!file_input.eof()) {
		getline(file_input, line);
		input += line + "\n";
	}
	file_input.close();

	int count_tests = 0;
	count_tests = atoi(input.c_str());

	vector<string> tests;
	string test;
	bool skipped_first = false;
	bool insert = false;
	for (int i = 0; i < input.length(); i++) {
		if (input[i] != '\n') {
			test += input[i];
			insert = false;
		} else {
			insert = true;
		}
		
		if (insert || i + 1 == input.length()) {
			if (skipped_first) {
				tests.push_back(test);
			} else {
				skipped_first = true;
			}
			test = "";
		}
	}

	string output;
	int case_number = 1;
	for (vector<string>::iterator i = tests.begin(); i != tests.end(); ++i) {
		string test = (*i);
		//cout << "\n\nTESTING >>" << test << "<<" << endl;

		vector<int> queue_blue, queue_orange;
		vector<bool> queue;
		int pos_blue = 1, pos_orange = 1;
		int steps = 0;

		bool orange = true;
		int value = 0;
		int count_buttons = 0;
		bool counting = true;
		bool insert = false;

		for (int i = 0; i < test.length(); i++) {
			

			if (counting && test[i] != ' ') {
				count_buttons = 10 * count_buttons + test[i] - 48;
				continue;
			}
			counting = false;

			if (test[i] == 'O') {
				orange = true;
			} else if (test[i] == 'B') {
				orange = false;
			} else if (test[i] != ' ') { // == number
				value = 10 * value + test[i] - 48;
				insert = i + 1 == test.length();
			} else {
				insert = true;
			}

			if (insert && value != 0) {
				if (orange) {
					queue_orange.push_back(value);
					queue.push_back(true);
				} else {
					queue_blue.push_back(value);
					queue.push_back(false);
				}
				value = 0;
			}
		}
		bool pressed;
		do {
			pressed = false;
			//cout << "orange: ";
			if (queue_orange.size() > 0) {
				if (queue[0] && pos_orange == queue_orange[0]) {
					//cout << "push button" << queue_orange[0] << " | ";
					queue_orange.erase(queue_orange.begin());
					queue.erase(queue.begin());
					pressed = true;
				} else if (pos_orange != queue_orange[0]) {
					if (pos_orange > queue_orange[0]) {
						pos_orange--;
					} else {
						pos_orange++;
					}
					//cout << "move to " << pos_orange << " | ";
				} else {
					//cout << "stay" << " | ";
				}
			} else {
				//cout << "stay" << " | ";
			}

			//cout << "blue: ";
			if (queue_blue.size() > 0) {
				if (!queue[0] && !pressed && pos_blue == queue_blue[0]) {
					//cout << "push button " << queue_blue[0] << endl;
					queue_blue.erase(queue_blue.begin());
					queue.erase(queue.begin());
				} else if (pos_blue != queue_blue[0]) {
					if (pos_blue > queue_blue[0]) {
						pos_blue--;
					} else {
						pos_blue++;
					}
					//cout << "move to " << pos_blue << endl;
				} else {
					//cout << "stay" << endl;
				}
			} else {
				//cout << "stay" << endl;
			}

			steps++;
		} while (queue.size() > 0);


		char buffer[1024];
		sprintf(buffer, "Case #%d: %d\n", case_number, steps);
		output += buffer;
		case_number++;
	}

	ofstream myfile;
	myfile.open ("output.txt");
	myfile << output;
	myfile.close();
	return 0;

	getchar();
	getchar();
	return 0;
}

