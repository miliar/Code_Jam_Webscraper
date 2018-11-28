//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// obtaining file size
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
using namespace std;

string convert_line(string input);

int main ()
{
	int caseCount = 0;
	string line = "";
	ifstream myfile ("A-small-attempt0.in");
	ofstream myfile_out ("A-small-attempt0.out");

	if( myfile.good()) getline(myfile, line);
	caseCount = atoi(line.c_str());
//	cout << line << " lines.\n";

	for ( int i=1; i<=caseCount; i++)
	{
		getline(myfile, line);
//		cout << "Case #" << i << ": " << line << endl;
		myfile_out << "Case #" << i << ": " << convert_line(line) << endl;
	}
	myfile.close();
	myfile_out.close();
	return 0;
}


string convert_line(string input)
{
//	char alpha_r[30] = "abcdefghijklmnopqrstuvwxyz";
	char alpha_c[30] = "yhesocvxduiglbkrztnwjpfmaq";
	size_t length = input.length();
	for( unsigned i=0; i< length; i++)
	{
		if( input[i] == ' ')continue;
		input[i] = alpha_c[input[i]-'a'];
	}

	return input;
}
