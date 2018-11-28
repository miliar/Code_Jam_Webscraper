#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>

using namespace std;

int calculateTime(queue<int> &primary, queue<int> &secondary, int &primary_pos, int &secondary_pos) {
	int time = 0;
	time = abs(primary.front() - primary_pos) + 1;
	primary_pos = primary.front();
	primary.pop();
	if (secondary_pos < secondary.front()) {
		if (secondary_pos + time > secondary.front()) {
			secondary_pos = secondary.front();
		} else {
			secondary_pos += time;
		}
	} else {
		if (secondary_pos - time < secondary.front()) {
			secondary_pos = secondary.front();
		} else {
			secondary_pos -= time;
		}
	}
	
	return time;
}

int main() {
	/* Input data file. */
	string filename;
	getline(cin, filename);
	ifstream inputFile;
	inputFile.open(filename.c_str(), ios::in);
	
	/* Output stored in gcjoutput.txt */
	ofstream outputFile;
	outputFile.open("gcjoutput.txt", ios::out);
	
	int T;
	inputFile >> T;
	for (int i = 0; i < T; i++) {
		int N;
		inputFile >> N;
		queue<char> sequence;
		queue<int> queueForOrange;
		queue<int> queueForBlue;
		char ch;
		int x;
		for (int j = 0; j < N; j++) {
			inputFile >> ch >> x;
			sequence.push(ch);
			if (ch == 'O') {
				queueForOrange.push(x);
			} else {
				queueForBlue.push(x);
			}
		}
		
		int currOrange = 1;
		int currBlue = 1;
		int time = 0;
		
		while (!sequence.empty()) {
			if (sequence.front() == 'O') {
				time += calculateTime(queueForOrange, queueForBlue, currOrange, currBlue);
			} else {
				time += calculateTime(queueForBlue, queueForOrange, currBlue, currOrange);
			}
			sequence.pop();
		}
		
		outputFile << "Case #" << i + 1 << ": " << time << endl;
	}
	
	/* Clearing file stream. */
	inputFile.close();
	outputFile.close();
	
	return 0;
}