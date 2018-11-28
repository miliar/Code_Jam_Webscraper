#include <iostream>
#include <fstream>
#include <map>
#include <string>
using namespace std;

int main() {
	int numCase = 1;
	ifstream mapStream("map.txt");
	map<char, char> mapping;
	for (int i = 0; i < 27; i++) {
		string line;
		getline(mapStream, line);
		mapping[line[0]] = line[1];
	}
	mapStream.close();
	
	ifstream infile;
	infile.open("test.txt");
	int number;
	infile >> number;
	string junk;
	getline(infile, junk);
	for (int i = 0; i < number; i++) {
		string line;
		string result = "";
		getline(infile, line);
		int size = line.size();
		for (int j = 0; j < size; j++) {
			result += mapping[line[j]];
		}
		cout << "Case #" << numCase << ": " << result << endl;
		numCase++;
	}
	return 0;
}
