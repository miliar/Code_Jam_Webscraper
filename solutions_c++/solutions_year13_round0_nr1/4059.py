//============================================================================
// Name        : TicTacToe.cpp
// Author      : Jitesh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <boost/numeric/ublas/matrix.hpp>

using namespace std;
using namespace boost::numeric::ublas;

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

int game(string selections)
{
	char winner = '.';
	matrix<char> m (4, 4);
	//cerr << selections << endl;
	for(int i = 0, j = 0, k = 0; i < selections.size(); ++i)
	{
		//cerr << "i = " << i << ", j = " << j << ", k = " << k << endl;
		m(j, k) = selections[i];
		k = (++k)%4;
		if(!k)
			++j;
	}

	for(int i = 0; i < 4; ++i){
		bool flag = true;
		char ch = m(i, 0);
		if(ch == 'T' && m(i, 1) != '.') {
			ch = m(i, 1);
		} else if((ch == 'T' && m(i, 1) == '.') || (ch == '.'))  {
			flag = false;
		}
		for(int j = 1; j < 4; ++j) {
			if(!((m(i, j) == ch) || (m(i, j) == 'T')))
				flag = false;
		}
		if(flag) {
			cerr << "Row: Line: " << i << endl << "we have a winner = " << ch << endl;
			winner = ch;
		}
	}

	for(int i = 0; i < 4; ++i){
		bool flag = true;
		char ch = m(0, i);
		if(ch == 'T' && m(1, i) != '.') {
			ch = m(1, i);
		} else if((ch == 'T' && m(1, i) == '.') || (ch == '.'))  {
			flag = false;
		}
		for(int j = 1; j < 4; ++j) {
			if(!((m(j, i) == ch) || (m(j, i) == 'T')))
				flag = false;
		}
		if(flag) {
			cerr << "Column: Line: " << i << endl << "we have a winner = " << ch << endl;
			winner = ch;
		}
	}

	char ch = m(0, 0);
	bool flag = true;
	if(ch == 'T' && m(1, 1) != '.') {
		ch = m(1, 1);
	} else if((ch == 'T' && m(1, 1) == '.') || (ch == '.'))  {
		flag = false;
	}
	if(ch != '.')  {
		for(int i = 1; i < 4; ++i){
			if(!((m(i, i) == ch) || (m(i, i) == 'T')))
				flag = false;
		}
		if(flag) {
			cerr << "Diagonal 1" << endl << "we have a winner = " << ch << endl;
			winner = ch;
		}
	}

	ch = m(0, 3);
	flag = true;
	if(ch == 'T' && m(1, 2) != '.') {
		ch = m(1, 2);
	} else if((ch == 'T' && m(1, 2) == '.') || (ch == '.'))  {
		flag = false;
	}
	if(ch != '.')  {
		for(int i = 1; i < 4; ++i){
			if(!((m(i, 3-i) == ch) || (m(i, 3-i) == 'T')))
				flag = false;
		}
		if(flag) {
			cerr << "Diagonal 2" << endl << "we have a winner = " << ch << endl;
			winner = ch;
		}
	}

	if(winner == 'O') {
		return 0;
	} else if (winner == 'X'){
		return 1;
	} else if(winner == '.') {
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(m(i,j) == '.')
					return 3;
	}
	return 2;
}

int main() {
	ofstream* output;
	string filename = "input.in";
	string line;
	std::ifstream ifs(filename.c_str());
	string output_file = "output.op";
	output = new ofstream(output_file.c_str());

	string str = "";

	int T = 0, testCase = 1;
	if ( ifs.is_open() ) {
		if( !ifs.eof() ) {
			getline( ifs, line );
			T = string_to_digits<int>(line);
		}

		for(int i = 0; !ifs.eof() && T > 0; i++, testCase++, T-- ) {
			for(int j = 0; j < 4; ++j) {
				getline( ifs, line );
				str += line;
				cerr << line << endl;
				//*output << "Case #" << testCase << ": " << compute(line) << endl;
			}
			int value = game(str);
			*output << "Case #" << i + 1 << ": ";
			switch(value) {
				case 0:
					*output << "O won" << endl;
					break;
				case 1:
					*output << "X won" << endl;
					break;
				case 2:
					*output << "Draw" << endl;
					break;
				case 3:
					*output << "Game has not completed" << endl;
					break;
			}
			str = "";
			getline(ifs, line);
			cerr << endl;
		}
	}
	cerr << line << endl;
	output->close();

	return 0;
}
