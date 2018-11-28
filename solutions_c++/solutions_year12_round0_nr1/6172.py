//============================================================================
// Name        : Googlerese.cpp
// Author      : Cristian Atehortúa
// Version     : 2.0
// Copyright   : Open Source
// Description : Problem A. Speaking in Tongues - Google CodeJam 2012
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

string translate(string s) {

	string ret = "";
	for (int i=0; i < s.length(); i++) {

		switch (s.at(i)) {
		case 'a':
			ret = ret + "y";
			break;
		case 'b':
			ret = ret + "h";
			break;
		case 'c':
			ret = ret + "e";
			break;
		case 'd':
			ret = ret + "s";
			break;
		case 'e':
			ret = ret + "o";
			break;
		case 'f':
			ret = ret + "c";
			break;
		case 'g':
			ret = ret + "v";
			break;
		case 'h':
			ret = ret + "x";
			break;
		case 'i':
			ret = ret + "d";
			break;
		case 'j':
			ret = ret + "u";
			break;
		case 'k':
			ret = ret + "i";
			break;
		case 'l':
			ret = ret + "g";
			break;
		case 'm':
			ret = ret + "l";
			break;
		case 'n':
			ret = ret + "b";
			break;
		case 'o':
			ret = ret + "k";
			break;
		case 'p':
			ret = ret + "r";
			break;
		case 'q':
			ret = ret + "z";
			break;
		case 'r':
			ret = ret + "t";
			break;
		case 's':
			ret = ret + "n";
			break;
		case 't':
			ret = ret + "w";
			break;
		case 'u':
			ret = ret + "j";
			break;
		case 'v':
			ret = ret + "p";
			break;
		case 'w':
			ret = ret + "f";
			break;
		case 'x':
			ret = ret + "m";
			break;
		case 'y':
			ret = ret + "a";
			break;
		case 'z':
			ret = ret + "q";
			break;
		case ' ':
			ret = ret + ' ';
			break;
		default:
			break;
		}

	}
	return ret;
}

int main() {
	int T;
	string S[30];
	char aux[101];
	ifstream fin("C:\\eclipse\\Workspace\\Googlerese\\Debug\\A-small-attempt1.in");
	ofstream fout("C:\\eclipse\\Workspace\\Googlerese\\Debug\\A-small-attempt1.txt");

	fin >> T;

	if (T < 1 || T > 30) {
		printf("\nERROR: the number of cases should be in [1, 30]\n");
	} else  {

		fin.getline(aux, 101);

		S[0] = aux;

		S[0] = translate(S[0]);

		for (int i=1; i<=T; i++) {

			fin.getline(aux, 101);

			S[i-1] = aux;

			S[i-1] = translate(S[i-1]);

		}

		for (int i=0; i<T; i++) {

			fout << "Case #" << i+1 << ": " << S[i]<< endl;
		}

	}

	return 0;
}
