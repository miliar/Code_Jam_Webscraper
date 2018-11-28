#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int helper(string phrase, string test) {
	string original = phrase;
	string phrase1 = phrase;
	string test1 = test;
	if (test != "") {
		if (phrase1[0] == test1[0] && phrase1 == "m") {
			test1.erase(0,1);
			return 1 + helper(original, test1);
		} else if (phrase1[0] == test1[0] && phrase1 != "m") {
			phrase1.erase(0,1);
			test1.erase(0,1);
			return helper(phrase1, test1) + helper(original, test1);
		} else {
			test1.erase(0,1);
			return helper(original, test1);
		}
	} else return 0;
}

int main() {
	string line;
	ifstream myfile;
	FILE* out = fopen("answer.txt", "w");
	myfile.open("D:\\Downloads\\C-small-attempt2(2).in");
	string phrase = "welcome to code jam"; 
	if (myfile.is_open()) {
		getline(myfile,line);
		int cases = atoi(line.c_str());
		for(int i = 0; i < cases; i++) {
			getline(myfile,line);
			int count = 0;
			count = helper(phrase, line);
			fprintf(out, "Case #%i: ", i+1);
			if (count / 1000 == 0)
				fprintf(out, "0");
			if (count / 100 == 0)
				fprintf(out, "0");
			if (count / 10 == 0)
				fprintf(out, "0");
			fprintf(out, "%i\n", count);
		}
		myfile.close();
	} else cout << "Unable to open file.";
	return 0;
}
