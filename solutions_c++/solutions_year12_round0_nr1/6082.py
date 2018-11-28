//============================================================================
// Name        : gcj2012.cpp
// Author      : Ravi
// Version     :
// Copyright   : Copyright notice, it wasn't me!!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

void convert1(string inp, string **out)
{
	int len = inp.length();
	string *output;
	output = new string();
	char inpchar;
	char outchar;

	cout << "Number of input characters " << len;
	for(int i = 0; i < len; i++) {
		inpchar = inp.at(i);
		switch(inpchar){
		case 'a':
			outchar = 'y';
			break;
		case 'b':
			outchar = 'h';
			break;
		case 'c':
			outchar = 'e';
			break;
		case 'd':
			outchar = 's';
			break;
		case 'e':
			outchar = 'o';
			break;
		case 'f':
			outchar = 'c';
			break;
		case 'g':
			outchar = 'v';
			break;
		case 'h':
			outchar = 'x';
			break;
		case 'i':
			outchar = 'd';
			break;
		case 'j':
			outchar = 'u';
			break;
		case 'k':
			outchar = 'i';
			break;
		case 'l':
			outchar = 'g';
			break;
		case 'm':
			outchar = 'l';
			break;
		case 'n':
			outchar = 'b';
			break;
		case 'o':
			outchar = 'k';
			break;
		case 'p':
			outchar = 'r';
			break;
		case 'q':
			outchar = 'z';
			break;
		case 'r':
			outchar = 't';
			break;
		case 's':
			outchar = 'n';
			break;
		case 't':
			outchar = 'w';
			break;
		case 'u':
			outchar = 'j';
			break;
		case 'v':
			outchar = 'p';
			break;
		case 'w':
			outchar = 'f';
			break;
		case 'x':
			outchar = 'm';
			break;
		case 'y':
			outchar = 'a';
			break;
		case 'z':
			outchar = 'q';
			break;
		case ' ':
			outchar = ' ';
			break;
		}

		output->insert(i, 1, outchar);
	}
	*out = output;
	cout << "Number of output characters " << output->length();
}

void solvea()
{
	ifstream inpfile;
		ofstream outfile;
		string inp;
		string *out = NULL;
		int linecount = 1;
		int inpLC = 0;

		inpfile.open("D:\\sw\\workspaces\\gcj2012\\data\\A-small-attempt4.in");
		if(!inpfile.is_open()) {
			cout << "Unable to open input file\n";
			return;
		}

		outfile.open("D:\\sw\\workspaces\\gcj2012\\data\\out.txt");
		if(!outfile.is_open()) {
			cout << "Unable to open output file\n";
			return;
		}
		std::getline(inpfile, inp);
		while(!inpfile.eof()) {
			std::getline(inpfile, inp);

			cout << "input " << inp << endl;

			convert1(inp, &out);

			cout << "output " << *out << endl;
			cout << "out length " << out->length();

			outfile << "Case #" << linecount << ": " << *out;

			//if(linecount < inpLC) {
				outfile << "\n";
			//}
			linecount++;
		}
}

int main() {

	solvea();

	return 0;
}
