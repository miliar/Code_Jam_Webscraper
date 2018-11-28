#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
#include <math.h>

using namespace std;
int map[128];

void OpenFiles(ifstream &in, ofstream &out) {
	in.open("A-small-attempt1.in");
	out.open("result.txt");
	
	if(in.fail() || out.fail())
		cout << "Failed to open input or output file." << endl;
}

int main (int argc, char * const argv[]) {
    ifstream in;
	ofstream out;
	OpenFiles(in, out);
    int numCases;
	in >> numCases;
	in.get();
	
	for (int numCase = 0; numCase < numCases; ++numCase) {
		for (int i = 0; i < 128; ++i) {
			map[i] = -1;
		}
		int ch;
		int sum = 0;
		int curval = 2;
		int numUniques = 2;
		bool doneSecond = false;
		int firstChar;
		string line;
		getline(in, line);
//		cout << "line: " << line << endl;

		int length = line.length();
		
//		cout << "length: " << length << endl;
		for (int i = length; i > 0; --i) {
			ch = line[length-i];
			
			// first one
			if (i == length) {
				map[ch] = 1;
				firstChar = ch;
//				cout << "assigned first one (1): " << (char)ch << endl;
			}
			// second one
			if (!doneSecond && (ch != firstChar)) {
				map[ch] = 0;
				doneSecond = true;
//				cout << "assigned second one (0): " << (char)ch << endl;
			}
			
			if (map[ch] == -1) {
				map[ch] = curval++;
				++numUniques;
//				cout << "assigned one (" << curval-1 << "): " << (char)ch << endl;

			}
		}
		
//		cout << "numuniques: " << numUniques << endl;
		// sum it
//		cout << "looks like: ";
		for (int i = 0; i < length; ++i) {
//			cout << map[line[i]];
			sum += map[line[i]] * pow(numUniques, length-1-i);
		}
		
		out << "Case #" << numCase+1 << ": " << sum << endl;
	}
	
    return 0;
}
