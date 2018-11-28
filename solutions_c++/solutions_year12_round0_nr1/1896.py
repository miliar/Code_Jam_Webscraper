/* Speaking in Tongues */
/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com
 */


#include <string>
using std::string;

#include <iostream>
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;

#include <map>
#include <utility>
using namespace std;

int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
    
	int total_cases;
	input_file >> total_cases;
	
	map<char, char> language;
	
	language['y'] = 'a';
	language['n'] = 'b';
	language['f'] = 'c';
	language['i'] = 'd';
	language['c'] = 'e';
	language['w'] = 'f';
	language['l'] = 'g';
	language['b'] = 'h';
	language['k'] = 'i';
	language['u'] = 'j';
	language['o'] = 'k';
	language['m'] = 'l';
	language['x'] = 'm';
	language['s'] = 'n';
	language['e'] = 'o';
	language['v'] = 'p';
	language['z'] = 'q';
	language['p'] = 'r';
	language['d'] = 's';
	language['r'] = 't';
	language['j'] = 'u';
	language['g'] = 'v';
	language['t'] = 'w';
	language['h'] = 'x';
	language['a'] = 'y';
	language['q'] = 'z';
	language[' '] = ' ';

	
	string str;

	getline(input_file, str);
	for (size_t i = 1; i <= total_cases; ++i) {
		getline(input_file, str);
		
		string converted = "";
		for (size_t index = 0; index < str.length(); ++index) {
			converted += language.find(str[index])->second;
		}

		output_file << "Case #" << i << ": " << converted;
		if (i != total_cases) {
			output_file << endl;
		}
		
	}
			
	
    input_file.close();
    output_file.close();
	return 0;
}