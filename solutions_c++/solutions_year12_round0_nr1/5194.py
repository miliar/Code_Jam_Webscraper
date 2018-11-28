
#include "genlib.h"
#include "simpio.h"
#include <iostream>
#include <fstream>
#include "lexicon.h"
#include "scanner.h"
#include "strutils.h"
#include "map.h"
#include "foreach.h"
const string Title = "firsttest.txt";
const string Test = "test.txt";

int main() {
	
	ifstream infile;
	ofstream offile;
	offile.open(Test.c_str());
	infile.open(Title.c_str());
	string str, conversion; 
	char convert[26];
	
	string code = "yhesocvxduiglbkrztnwjpfmaq";
	
	getline(infile, str);
	char temp;
	int lines = StringToInteger(str);
	for(int i = 0; i < lines; i++){
		getline(infile, str);
		cout << str << endl;
		conversion = "";
		for(int j = 0; j < str.length(); j++){
			cout << str[j] << endl;
			if(str[j] == ' '){
				conversion += " ";
				cout << " " << endl;
			} else {
				temp = str[j];
				conversion += (code[(temp - 'a')]);
				cout << (code[(temp - 'a')]) << endl;
			}
		}
		offile << "Case #" << i + 1 << ": " << conversion << endl;
	}
	
	return 0;
}
