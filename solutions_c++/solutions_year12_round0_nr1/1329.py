#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

int num_trials;

char code[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};


char convert_char(char c) {
	return code[c-97];
}

string convert_line(string line) {
	string converted = "";
	for (int i = 0; i < line.size(); i++) {
		if (line[i] == ' ') {
			converted = converted + ' ';
		} else {
			converted = converted + convert_char(line[i]);
		}
	}
	return converted;
}

char raw_line[100];
string line;

int main(int argc, const char* argv[])  {
    ofstream fout ("a.out");
    ifstream fin ("a.in");

	fin >> num_trials;
	fin.get(); //yikes!
	
	cout << num_trials << endl;
	
	
	
	
	
	for (int trial = 1; trial <= num_trials; trial++) {
		fin.getline(raw_line,101);
		line = raw_line;
		fout << "Case #" << trial << ": " << convert_line(line) << endl;
	}
	
}
