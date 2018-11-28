// GCJ_QR_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

char translate(char s){
	char res;
	switch (s){
		case 'a':
			res = 'y';
			break;
		case 'b':
			res = 'h';
			break;
		case 'c':
			res = 'e';
			break;
		case 'd':
			res = 's';
			break;
		case 'e':
			res = 'o';
			break;
		case 'f':
			res = 'c';
			break;
		case 'g':
			res = 'v';
			break;
		case 'h':
			res = 'x';
			break;
		case 'i':
			res = 'd';
			break;
		case 'j':
			res = 'u';
			break;
		case 'k':
			res = 'i';
			break;
		case 'l':
			res = 'g';
			break;
		case 'm':
			res = 'l';
			break;
		case 'n':
			res = 'b';
			break;
		case 'o':
			res = 'k';
			break;
		case 'p':
			res = 'r';
			break;
		case 'q':
			res = 'z';
			break;
		case 'r':
			res = 't';
			break;
		case 's':
			res = 'n';
			break;
		case 't':
			res = 'w';
			break;
		case 'u':
			res = 'j';
			break;
		case 'v':
			res = 'p';
			break;
		case 'w':
			res = 'f';
			break;
		case 'x':
			res = 'm';
			break;
		case 'y':
			res = 'a';
			break;
		case 'z':
			res = 'q';
			break;
		case ' ':
			res = ' ';
			break;
	}
	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string InputStr, OutputStr;
	char o = 'a';
	InputStr += o;
	ifstream myReadFile;
	myReadFile.open("A-small-attempt2.in");
	ofstream myWriteFile;
	myWriteFile.open ("output.txt");
	int case_num = 0;
	bool first = true;
	int NumberCases = 0;
	if (myReadFile.is_open()) {
		while (!myReadFile.eof()) {
			if (first){
				getline(myReadFile,InputStr);
				NumberCases = atoi(InputStr.c_str());
				first = false;
			}
			else {
				case_num += 1;
				if (case_num <= NumberCases){
					getline(myReadFile,InputStr);
					OutputStr = "";
					for (int i =0; i < InputStr.length(); i++){
						OutputStr += translate(InputStr[i]);
					}
					myWriteFile << "Case #" << case_num << ": " << OutputStr << endl;
				}
				else getline(myReadFile,InputStr);
			}
		}
	}
	myReadFile.close();
	myWriteFile.close();
	system ("pause");
	return 0;
}

