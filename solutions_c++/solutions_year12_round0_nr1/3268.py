#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string map[26] = {"y","h","e","s","o","c","v","x","d","u","i","g","l","b","k","r","z","t","n","w","j","p","f","m","a","q"};

int main() {
    ofstream fout ("QA.out");
    ifstream fin ("QA.in");
	int T;
	fin >> T;
	string derp;
	getline(fin,derp);
	for (int t = 1; t <= T; t++) {
		string input;
		getline(fin,input);
		string output = "";
		for (int i = 0; i < input.size(); i++) {
			if (input[i] == 32) output+=" ";
			else output+=map[(int)input[i]-97];
		}
		fout << "Case #" << t << ": " << output << endl;
	}
    return 0;
}