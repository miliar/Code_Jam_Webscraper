
#include "genlib.h"
#include "simpio.h"
#include <iostream>
#include <fstream>
#include "lexicon.h"
#include "scanner.h"
#include "strutils.h"
#include "map.h"
#include "foreach.h"
const string Title = "C-small-attempt1.in";
const string Test = "test.txt";
int tenpower(int power);

int main() {
	Lexicon lexicon;	
	ifstream infile;
	ofstream offile;
	offile.open(Test.c_str());
	infile.open(Title.c_str());
	string str, conversion; 
	int num, A, B, space, length, test;
	getline(infile, str);
	num = 0;
	int lines = StringToInteger(str);
	for(int i = 0; i < lines; i++){
		num = 0;
		getline(infile, str);
		space = str.find(" ");
		length = (str.length() - 1)/2;
		//cout << length << endl;
		A = StringToInteger(str.substr(0, space));
		B = StringToInteger(str.substr(space + 1));
		//cout << A << "   " << B << endl;
		for(int j = A; j < B; j++){
			lexicon.clear();
			for(int k = 0; k < length; k++){
				test = (j%(tenpower(k)))*(tenpower(length - k)) + j/(tenpower(k));
				//cout << test << endl;
				if((test > j) && (test <= B) && (test >= A) && (!lexicon.containsWord(IntegerToString(test)))){
					num++;
					lexicon.add(IntegerToString(test));
				}
			}
		}
		cout << num << endl;
		offile << "Case #" << i + 1 << ": " << num << endl;
	}
	return 0;
}

int tenpower(int power){
	if(power == 0){
		return 1;
	} 
	return 10*tenpower(power - 1);
}
