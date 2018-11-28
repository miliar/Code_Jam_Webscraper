#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	int array[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	ifstream fin("a.in");
	ofstream fout("a.out");
	int T;
	fin >> T;
	string temp2;
	getline(fin, temp2);
	for (int t = 0; t < T; t++) {
		string line;
		getline(fin, line);
		string trans = "";
		for (int i = 0; i < line.length(); i++) {
			if (line[i] == ' ') {
				trans += ' ';
				continue;
			}
			trans += array[(int)line[i] - 97];
		}
		fout << "Case #" << (t + 1) << ": " << trans << endl;
	}
}
		