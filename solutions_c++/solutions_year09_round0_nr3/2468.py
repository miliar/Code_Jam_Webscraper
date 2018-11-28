//============================================================================
// Name        : WelcometoCodeJam.cpp
// Author      : Peter
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

char *code = "welcome to code jam";
const unsigned int code_len = 19;
int rt = 0;

void match_code(string &input,unsigned int pos, unsigned int index){
	while((pos = input.find_first_of(code[index],pos)) != string::npos){
		++pos;
		unsigned int index2= index + 1;
		if(index2 < code_len)
			match_code(input, pos, index2);
		else{
			rt ++;
			if(rt >= 10000)
				rt-=10000;
		}
	}
}

int main() {
	ifstream infile("C-small.in");
	ofstream outfile("C-small.out");

	int case_num;
	char c;
	infile >> case_num;
	infile.get(c);						//skip the '\n'
//	cout << case_num << endl;
	for(int case_index=0; case_index<case_num; case_index++){
		string input;
		while(infile.get(c)){
			if(c !='\n'){
				input+=c;
			}
			else{
				break;
			}
		}
		rt = 0;
//		cout << input << endl;
		match_code(input,0,0);

		outfile << "Case #" << case_index+1 << ": " << setfill('0')<< setw(4)<< rt << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}
