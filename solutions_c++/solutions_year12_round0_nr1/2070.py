//============================================================================
// Name        : Tongues.cpp
// Author      : Jitesh Nambiar
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>

using namespace std;

//Map from Googlerese to English, letter taken from hint
char gMap[27] = {"\0\0\0\0o\0\0\0\0\0\0\0\0\0\0\0z\0\0\0\0\0\0\0a\0"};

template<class T>
T string_to_digits(std::string& str)
{
	T value;
	std::string parsedStr;
	std::string::const_iterator iterator;
	for(iterator = str.begin(); iterator != str.end(); iterator++)
		if((*iterator) != ',')
			parsedStr += *iterator;
	std::istringstream myFloat(parsedStr);
	myFloat >> value;
	return value;
}

//From Googlerese to English
void createReverseMapping() {
	//Sample Input/Output String
	string sampleIn = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string sampleOp = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	//Compute the map
	for(int i = 0; i < sampleIn.length(); ++i) {
		if(sampleIn[i] != ' ') {
			gMap[sampleIn[i] - 97] = sampleOp[i];
		}
	}

	int sumOfKnownLetters = 0;
	for(int j = 0; j < 26; ++j)
		if(gMap[j] != '\0')
			sumOfKnownLetters += gMap[j];

	int sumOfAllLetters = 0;
	for(int i = 0; i < 26; ++i)
		sumOfAllLetters += 'a' + i;

	char unknown = (char)(sumOfAllLetters -sumOfKnownLetters);
	for(int i = 0; i < 26; ++i)
		if(gMap[i] == '\0') {
			gMap[i] = unknown;
			break;
		}
}

//Convert 2 English from Googlerese
string convert2Eng(string& str){
	string op;
	for(int i = 0; i < str.length(); ++i) {
		char ch = str[i];
		if(ch == ' ')
			op += ch;
		else
			op += gMap[ch - 97];
	}
	return op;
}

int main() {
	createReverseMapping();

	ofstream* output;
	string filename = "input.in";
	string line;
	std::ifstream ifs(filename.c_str());
	string output_file = "output.op";
	output = new ofstream(output_file.c_str());

	int T = 0, testCase = 1;
	if ( ifs.is_open() ) {
		if( !ifs.eof() ) {
			getline( ifs, line );
			T = string_to_digits<int>(line);
		}
		for(int i = 0; !ifs.eof() && T > 0; i++, testCase++, T-- ) {
			getline( ifs, line );
			*output << "Case #" << testCase << ": " << convert2Eng(line) << endl;
		}
	}
	output->close();
	return 0;
}
