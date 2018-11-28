#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

void Move(int which_robot[], vector<size_t> &orange, vector<size_t> &blue, size_t total_buttons, size_t &buttons_left, size_t &orange_pos, size_t &blue_pos) {
	int robot_to_move = which_robot[total_buttons-buttons_left];
	if (robot_to_move == 0) {
		if (orange_pos != orange[0]) {
			if (orange[0] > orange_pos) orange_pos++;
			else orange_pos--;
		} else {
			buttons_left--;
			orange.erase(orange.begin());
		}
		if (blue.size() > 0) {
			if (blue_pos != blue[0]) {
				if (blue[0] > blue_pos) blue_pos++;
				else blue_pos--;
			}
		}
	} else {
		if (blue_pos != blue[0]) {
			if (blue[0] > blue_pos) blue_pos++;
			else blue_pos--;
		} else {
			buttons_left--;
			blue.erase(blue.begin());
		}
		if (orange.size() > 0) {
			if (orange_pos != orange[0]) {
				if (orange[0] > orange_pos) orange_pos++;
				else orange_pos--;
			}
		}
	}
}

int SolveProgram(int which_robot[], vector<size_t> orange, vector<size_t> blue) {
	size_t buttons_left = orange.size()+blue.size();
	size_t total_buttons = buttons_left;
	size_t orange_pos = 1, blue_pos = 1;
	int seconds = 0;
	while (buttons_left > 0) {
		Move(which_robot,orange,blue,total_buttons,buttons_left,orange_pos,blue_pos);
		seconds++;
	}
	return seconds;
}

int GetInstructions(ifstream &infile, size_t num_instructions) {
	int which_robot[num_instructions]; //0 for O, 1 for B
	vector<size_t> orange, blue;
	for (size_t i = 0; i < num_instructions; ++i) {
		char bot;
		size_t button;
		infile >> bot >> button;
		if (bot == 'O') {
			which_robot[i] = 0;
			orange.push_back(button);
		} else {
			which_robot[i] = 1;
			blue.push_back(button);
		}
	}
	return SolveProgram(which_robot,orange,blue);
}

int main () {
	string file_name = "/Users/sameerarya/Documents/A-large.in.txt";
    ifstream infile(file_name.c_str());
    ofstream outfile("bottrustoutput.txt");
	if (!infile.is_open()) cout << "ERROR" << endl;
	size_t num_cases;
	infile >> num_cases;

	for (size_t i = 1; i <= num_cases; ++i) {
		size_t num_instructions;
		infile >> num_instructions;
		int seconds = GetInstructions(infile, num_instructions);
		outfile << "Case #" << i << ": " << seconds << endl;
	}

    return 0;
}
