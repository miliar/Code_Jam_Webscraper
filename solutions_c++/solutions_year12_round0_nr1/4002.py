/*Speaking in Tongues*/

#include "scanner.h"
#include "strutils.h"
#include "genlib.h"
#include "simpio.h"
#include "vector.h"
#include <iostream>
#include <fstream>

/*Function prototypes */

int IntegerGetter(ifstream & infile);
string SolveTestCase(ifstream & infile);
void AddNextLetter(Vector<string> & solution, Vector<string> & eleminvoked, int i, Vector<Vector<string>> & basecombos, Vector<Vector<string>> & opposers, string & outputstr);
Vector<string> FindOutput(Vector<Vector<string>> & basecombos, Vector<Vector<string>> & opposers, Vector<string> & eleminvoked);

/*Main program*/

int main() {
	ifstream infile;
	ofstream outfile;
	infile.open("C:\\Users\\Alborz\\Desktop\\toungetests.txt");
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
		string solution = SolveTestCase(infile);
		outfile << "Case #" << i + 1 << ": " <<  solution << endl;
	}


	return 0;
}

int IntegerGetter(ifstream & infile) {
	string str;
	getline(infile, str);
	int num = StringToInteger(str);
	return num;
}

string SolveTestCase(ifstream & infile) {
	string input;
	string solution = "";
	getline(infile, input);
	for(int i = 0; i < input.length(); i++){
		if(input[i] == 'a'){
			solution += 'y';
		} else if (input [i] == 'b'){
			solution += 'h';
		} else if (input [i] == 'c'){
			solution += 'e';
		} else if (input [i] == 'd'){
			solution += 's';
		} else if (input [i] == 'e'){
			solution += 'o';
		} else if (input [i] == 'f'){
			solution += 'c';
		} else if (input [i] == 'g'){
			solution += 'v';
		} else if (input [i] == 'h'){
			solution += 'x';
		} else if (input [i] == 'i'){
			solution += 'd';
		} else if (input [i] == 'j'){
			solution += 'u';
		} else if (input [i] == 'k'){
			solution += 'i';
		} else if (input [i] == 'l'){
			solution += 'g';
		} else if (input [i] == 'm'){
			solution += 'l';
		} else if (input [i] == 'n'){
			solution += 'b';
		} else if (input [i] == 'o'){
			solution += 'k';
		} else if (input [i] == 'p'){
			solution += 'r';
		} else if (input [i] == 'q'){
			solution += 'z';
		} else if (input [i] == 'r'){
			solution += 't';
		} else if (input [i] == 's'){
			solution += 'n';
		} else if (input [i] == 't'){
			solution += 'w';
		} else if (input [i] == 'u'){
			solution += 'j';
		} else if (input [i] == 'v'){
			solution += 'p';
		} else if (input [i] == 'w'){
			solution += 'f';
		} else if (input [i] == 'x'){
			solution += 'm';
		} else if (input [i] == 'y'){
			solution += 'a';
		} else if (input [i] == 'z'){
			solution += 'q';
		} else if (input [i] == ' ') {
			solution += ' ';
		}
	}
	return solution;
}
