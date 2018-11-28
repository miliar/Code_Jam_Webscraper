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
#include <algorithm>

using namespace std;

long candy_value[1000];
int binary_x[1000], binary_y[1000];
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

int decimal_to_binary(long x, int* bin)
{
//	int x = tp;
	int i;
	for(i = 0; i < 1000 && x > 0; i++) {
		*(bin + i) = x%2;
		x = x/2;
	}
	return i;
	/*int k = --i;
	cout<< "binary of " << tp << " is ";
	for(; i >= 0; i--)
		cout<< *(bin+i);
	cout << endl;
	//return size
	return k;*/
}

long binary_to_decimal(int* bin, int size)
{
	long decimal = 0;
	for(int i = 0; i < size; i++)
		decimal += (*(bin+i))*pow(2,i);		//2^i
	return decimal;
}

int my_xor(int a, int b)
{
  return (a || b) && !(a && b);
}

long PatrickAdds(long x, long y)
{
	int sizeOf_x, sizeOf_y;
	int binary_sum[1000];

	sizeOf_x = decimal_to_binary(x,binary_x);
	sizeOf_y = decimal_to_binary(y,binary_y);
	int i;
	for(i = 0; i < sizeOf_x && i < sizeOf_y; i++)
		binary_sum[i] = my_xor(binary_x[i], binary_y[i]);
	for(; i < sizeOf_x; i++)
		binary_sum[i] = binary_x[i];
	for(; i < sizeOf_y; i++)
		binary_sum[i] = binary_y[i];
	return binary_to_decimal(binary_sum, i);
}

void compute(string& input, int testCase)
{
	vector<string> tokens;
	string delim = " \n";
	tokenize(input, tokens, delim);
	vector<string>::iterator iterator = tokens.begin();
	int i;
	for(i = 0;iterator != tokens.end(); iterator++, i++)
		candy_value[i] = string_to_digits<long>(*iterator);

	std::sort(candy_value, candy_value+i);

	long sum = 0;
	for(i = 0; i < N ; i++)
		sum = PatrickAdds(sum,candy_value[i]);

	if(sum)
		*output<< "Case #" << testCase << ": NO" << endl;
	else {
		sum = 0;
		//Leave the smallest element & rest add
		for(i = 1; i < N ; i++)
			sum += candy_value[i];
		*output<< "Case #" << testCase << ": " << sum << endl;
	}
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
		for(int i = 0; !ifs.eof(); i++ ) {
			getline( ifs, line );
			if(i%2)
				compute(line, test_case++);
			else
				N = string_to_digits<int>(line);
		}
	}

	output->close();
	return 0;
}
