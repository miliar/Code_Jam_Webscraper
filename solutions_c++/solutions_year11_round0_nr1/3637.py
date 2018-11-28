//============================================================================
// Name        : CodeJam.cpp
// Author      : Jitesh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iomanip>
#include <sstream>
#include <ios>
#include <istream>
#include <fstream>
#include <math.h>

#include <vector>

using namespace std;

/* O 2 B 1 B 2 O 4 */
typedef struct robo {
	int robo_id;	//orange = 1 Otherwise blue = 2
	int pos_time;
}ROBO;

ROBO rList[100];
int T, N;
ofstream* output;

void tokenize(string& str, vector<string>& tokens, const string& delimiters)
{
    size_t lastPos = str.find_first_not_of(delimiters, 0);
    size_t pos = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        lastPos = str.find_first_not_of(delimiters, pos);
        pos = str.find_first_of(delimiters, lastPos);
    }
}

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

void compute(string& input, int testCase)
{
//	cout<< "------------------------------ LINE ------------------------------" << endl;
	int orange_current_pos = 1, blue_current_pos = 1;
	bool it_is_orange = false;

	vector<string> tokens;
	string delim = " \n";
	tokenize(input, tokens, delim);
	vector<string>::iterator iterator = tokens.begin();
	if( iterator != tokens.end() ) {
		N = string_to_digits<int>(*iterator);
//		cout<< "N = " << N << endl;
		iterator++;
	}
	else
		return;
	int i, position;
	for(i = 0;iterator != tokens.end(); iterator++, i++) {
//		cout<<*iterator << "::";
//		cout<< " i = " << i << " & iterator = " << *iterator<<endl;
		if(!(i % 2)) {
			if( (*iterator).compare("O") == 0 )
				it_is_orange = true;
			else
				it_is_orange = false;
		}
		else {
			position = string_to_digits<int>(*iterator);
			if(it_is_orange) {
				rList[i/2].robo_id = 1;
				rList[i/2].pos_time = fabs(position - orange_current_pos) + 1;
				orange_current_pos = position;
			}
			else {
				rList[i/2].robo_id = 2;
				rList[i/2].pos_time = fabs(position - blue_current_pos) + 1;
				blue_current_pos = position;
			}
		}
	}

	int orange_current_time = 0, blue_current_time = 0, current_time = 0, time_taken = 0;
	for(int i = 0; i < N; i++) {
		if(rList[i].robo_id == 1) {
//			cout<< "O .. " ;
			time_taken = rList[i].pos_time + orange_current_time;
			if(time_taken > current_time)
				orange_current_time = current_time = time_taken;
			else
				orange_current_time = current_time = current_time + 1;
		}
		else {
//			cout<< "B .. " ;
			time_taken = rList[i].pos_time + blue_current_time;
			if(time_taken > current_time)
				blue_current_time = current_time = time_taken;
			else
				blue_current_time = current_time = current_time + 1;
		}
//		cout<< "C : " << current_time << endl;
	}
	*output<< "Case #" << testCase << ": " << current_time << endl;
//	cout<< "------------------------------ LINE ------------------------------" << endl;
}

int main() {
	string filename = "input.in";
	string line;
	int test_case;

	string output_file = "output.op";
	output = new ofstream(output_file.c_str());

	std::ifstream ifs(filename.c_str());

	if ( ifs.is_open() ) {
		if( !ifs.eof() ) {
			getline( ifs, line );
			T = string_to_digits<int>(line);
//			cout<<"T = " << T << endl;
		}
		test_case = 1;
		while ( !ifs.eof() ) {
			getline( ifs, line );
			compute(line, test_case++);
		}
	}
	output->close();
	return 0;
}
