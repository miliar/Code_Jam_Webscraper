/*
 * codeJam.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: fu4ny
 */

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string seed("welcome to code jam");
string line;
long result;
void count(int,int);
int main() {
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	int testCase;
	ifs >> testCase;

	ifs.ignore(1,'\n');
	for (int t=1; t<=testCase; t++) {
		getline(ifs,line);
		result = 0;
		count(0,0);
		result = result % 1000;
		ofs<<"Case #"<<t<<": ";
		if ( result < 10 ) ofs << "000" << result << endl;
		else if ( result < 100 )ofs << "00" << result << endl;
		else if ( result < 1000 )ofs << "0" << result << endl;
		else ofs << result << endl;
	}


	ofs.close();
	ifs.close();
}

void count(int seed_i, int pos ) {
	if ( seed_i == seed.length() ) {
		result ++;
		return;
	}
	int found;
	fflush(stdout);
	while ( (found=line.find(seed[seed_i],pos)) != string::npos ) {

		count(seed_i+1,found+1);
		pos = found + 1;
	}
}
