#include "strutils.h"
#include "genlib.h"
#include "vector.h"
#include "simpio.h"
#include "genlib.h"
#include <iostream>
#include <fstream>
#include "scanner.h"

/*Store Credit program*/

//Functions

int SolveTestCase(ifstream & infile);
int IntegerGetter(ifstream & infile);


//main

int main() {
	ifstream infile;
	ofstream outfile;
	int solution;
	infile.open("C:\\Users\\Alborz\\Desktop\\harmonysmall.txt");
	if(infile.fail()){
		cout << "Didn't work" << endl;
	} else {
		cout << "Opened" << endl;
	}
	outfile.open("C:\\Users\\Alborz\\Desktop\\Codejamtest.txt");
	if(outfile.fail()){
		cout << "Didn't work" << endl;
	} else {
		cout << "Opened" << endl;
	}
	int numcases = IntegerGetter(infile);
	for(int i = 0; i < numcases; i++){
		solution = SolveTestCase(infile);
		if(solution < 0) {
			outfile << "Case #" << i + 1 << ": " << "NO" <<endl;
		} else {
			outfile << "Case #" << i + 1 << ": " << solution <<endl;
		}
		
	}
	return 0;
}

int SolveTestCase(ifstream & infile) {
	int final = 0;
	string str;
	Scanner scanner;
	Scanner scannertwo;
	Vector<int> vec;
	getline(infile, str);
	scanner.setInput(str);
	scanner.setSpaceOption(Scanner::IgnoreSpaces);
	string peoplestr = scanner.nextToken();
	int totalpeople = StringToInteger(peoplestr);
	string lowstr = scanner.nextToken();
	int lownote = StringToInteger(lowstr);
	string highstr = scanner.nextToken();
	int highnote = StringToInteger(highstr);
	getline(infile, str);
	scannertwo.setInput(str);
	string dummy;
	int dummyint;
	scannertwo.setSpaceOption(Scanner::IgnoreSpaces);
	for(int i = 0; i < totalpeople; i++) {
		dummy = scannertwo.nextToken();
		dummyint = StringToInteger(dummy);
		vec.add(dummyint);
	}
	bool test = false;
	bool itbroke = false;
	bool gotone = false;
	for(int i = lownote; i <= highnote; i++){
		for(int j = 0; j < vec.size(); j++) {
			if(!((i % vec[j] == 0) || (vec[j] % i == 0))) {
				itbroke = true;
				break;
			} 
		}

		if(itbroke){
			itbroke = false;
		} else {
			final = i;
			gotone = true;
			break;
		}
	} 

	if(gotone) {
		return final;
	} else {
		final = -1;
		return final;
	}

}

int IntegerGetter(ifstream & infile) {
	string str;
	getline(infile, str);
	int num = StringToInteger(str);
	return num;
}



