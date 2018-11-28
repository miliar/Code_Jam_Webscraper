/*
 * 1---Speaking in Tongues(small).cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: fjywade
 */

#include <iostream>
#include <fstream>
using namespace std;

//string dict = "aybncfdiecfwglhbikjukolmmxnsoepvqzrpsdtrujvgwtxhyazq";
string dict = "aybhcedseofcgvhxidjukilgmlnbokprqzrtsntwujvpwfxmyazq";

int main()
{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small-attempt2.out", ios::app);
	int caseNum, count = 1;
	fin >>caseNum;
	while(!fin.eof()) {
		char letter;
		fin.get(letter);
		if(letter == '\n') {
			if(count != 1 && count <= caseNum) fout <<endl;
			if(count <= caseNum) fout <<"Case #" <<count++ <<": ";
		} else if(letter == ' ') {
			fout <<letter;
		} else {
			fout << dict[2*(letter-'a')+1];
		}
	}
	fout.close();
	fin.close();

	return 0;
}

