#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

string translate(string wrd) {
		for (int i = 0; i < wrd.length(); i++) {
		switch(wrd[i]) {
			case 'a':	wrd[i] = 'y';
						break;
			case 'b':	wrd[i] = 'h';
						break;
			case 'c':	wrd[i] = 'e';
						break;
			case 'd':	wrd[i] = 's';
						break;
			case 'e':	wrd[i] = 'o';
						break;
			case 'f':	wrd[i] = 'c';
						break;
			case 'g':	wrd[i] = 'v';
						break;
			case 'h':	wrd[i] = 'x';
						break;
			case 'i':	wrd[i] = 'd';
						break;
			case 'j':	wrd[i] = 'u';
						break;
			case 'k':	wrd[i] = 'i';
						break;
			case 'l':	wrd[i] = 'g';
						break;
			case 'm':	wrd[i] = 'l';
						break;
			case 'n':	wrd[i] = 'b';
						break;
			case 'o':	wrd[i] = 'k';
						break;
			case 'p':	wrd[i] = 'r';
						break;
			case 'q':	wrd[i] = 'z';
						break;
			case 'r':	wrd[i] = 't';
						break;
			case 's':	wrd[i] = 'n';
						break;
			case 't':	wrd[i] = 'w';
						break;
			case 'u':	wrd[i] = 'j';
						break;
			case 'v':	wrd[i] = 'p';
						break;
			case 'w':	wrd[i] = 'f';
						break;
			case 'x':	wrd[i] = 'm';
						break;
			case 'y':	wrd[i] = 'a';
						break;
			case 'z':	wrd[i] = 'q';
						break;
			case ' ':	wrd[i] = ' ';
		}
	}
	return wrd;
}

int main() {
	ifstream fin("./A-small-attempt1.in");
	ofstream fout("./a.out");	
	
	int testCases;
	
	fin>>testCases;
	fin.ignore();
	
	for (int i = 0; i < testCases; i++) {
		string word;
		getline(fin,word);
		word = translate(word);
		fout<<"Case #" << i+1<< ": "<<word<<endl;
		
		
	}
}
