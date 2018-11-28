#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<string>


using namespace std;

int main()
{
	ifstream infile;
	infile.open ("A-small-attempt1.in", ifstream::in);
	
	ofstream outfile;
	outfile.open("A-small-attempt1.out", ofstream::out);

    int nQuestion;
    vector<string> vInputString;
	map<char, char> mAlphaMapping;

	mAlphaMapping['y'] = 'a';
	mAlphaMapping['n'] = 'b';
	mAlphaMapping['f'] = 'c';
	mAlphaMapping['i'] = 'd';
	mAlphaMapping['c'] = 'e';
	mAlphaMapping['w'] = 'f';
	mAlphaMapping['l'] = 'g';
	mAlphaMapping['b'] = 'h';
	mAlphaMapping['k'] = 'i';
	mAlphaMapping['u'] = 'j';
	mAlphaMapping['o'] = 'k';
	mAlphaMapping['m'] = 'l';
	mAlphaMapping['x'] = 'm';
	mAlphaMapping['s'] = 'n';
	mAlphaMapping['e'] = 'o';
	mAlphaMapping['v'] = 'p';
	mAlphaMapping['z'] = 'q';
	mAlphaMapping['p'] = 'r';
	mAlphaMapping['d'] = 's';
	mAlphaMapping['r'] = 't';
	mAlphaMapping['j'] = 'u';
	mAlphaMapping['g'] = 'v';
	mAlphaMapping['t'] = 'w';
	mAlphaMapping['h'] = 'x';
	mAlphaMapping['a'] = 'y';
	mAlphaMapping['q'] = 'z';
	mAlphaMapping[' '] = ' ';

/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/
	char aCount[10];
	infile.getline(aCount, 10);
	nQuestion = atoi( aCount );
    for( int i=0; i<nQuestion; i++ ){
         char aInput[101];
		 infile.getline(aInput, 101);
		 string sInput = aInput;
         vInputString.push_back(sInput);
    }

	for( int i=0; i<nQuestion; i++){
		outfile << "Case #" << i+1 << ": ";
		const string& sInput = vInputString.at(i);
		for( int j=0; j< sInput.length(); j++ ){
			outfile << mAlphaMapping[ sInput[j] ];
		}

		outfile << endl;
	}

	infile.close();
	outfile.close();
}
