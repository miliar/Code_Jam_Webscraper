/*
 *  A.cpp
 *  
 *
 *  Created by Sameep Bagadia on 14/04/12.
 *  Copyright 2012 __MyCompanyName__. All rights reserved.
 *
 */


#include <iostream>
#include <string>
using namespace std;

char convertchar (char in) {
	switch (in) {
		case 'a':
			return 'y';
			break;
		case 'b':
			return 'h';
			break;
		case 'c':
			return 'e';
			break;
		case 'd':
			return 's';
			break;
		case 'e':
			return 'o';
			break;
		case 'f':
			return 'c';
			break;
		case 'g':
			return 'v';
			break;
		case 'h':
			return 'x';
			break;
		case 'i':
			return 'd';
			break;
		case 'j':
			return 'u';
			break;
		case 'k':
			return 'i';
			break;
		case 'l':
			return 'g';
			break;
		case 'm':
			return 'l';
			break;
		case 'n':
			return 'b';
			break;
		case 'o':
			return 'k';
			break;
		case 'p':
			return 'r';
			break;
		case 'q':
			return 'z';
			break;
		case 'r':
			return 't';
			break;
		case 's':
			return 'n';
			break;
		case 't':
			return 'w';
			break;
		case 'u':
			return 'j';
			break;
		case 'v':
			return 'p';
			break;
		case 'w':
			return 'f';
			break;
		case 'x':
			return 'm';
			break;
		case 'y':
			return 'a';
			break;
		case 'z':
			return 'q';
			break;
		case ' ':
			return ' ';
				break;
		default:
			return ' ';
			break;
	}
}

void convert(char* a) {
	for (int i = 0; a[i] != '\0' ; i++) {
		a[i] = convertchar(a[i]);
	}
	//return a;
}

int main() {
	int n;
	cin>>n;
	char arr[101];
	cin.getline(arr,101);
	//char mod[100];
	for (int i = 0; i < n; i++) {
		cin.getline(arr , 101);
		convert(arr);
		cout << "Case #"<<(i+1)<<": ";
		for (int j = 0; arr[j] != '\0'; j++) {
			cout << arr[j];
		}
		cout << endl;
	}
	return 0;
}