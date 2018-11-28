#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream infile("file.txt");
	int testCases;
	infile >> testCases;
	for (int i = 1; i <= testCases; i++) {
		int googlers;
		int surprising;
		int p;
		infile >> googlers;
		infile >> surprising;
		infile >> p;
		int junk = p-1;
		if (junk < 0) junk = 0;
		int minLegal = p + 2*junk;
		junk = p-2;
		if (junk < 0) junk = 0;
		int minStrange = p + 2*junk;
		int result = 0;
		for (int j = 0; j < googlers; j++) {
			int score;
			infile >> score;
			if (score >= minLegal) result++;
			else if (surprising && score >= minStrange) {
				result++;
				surprising--;
			}
		}
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
