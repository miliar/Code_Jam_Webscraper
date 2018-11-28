// Firstone.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in ("cj1c1.in");
	ofstream out ("cj1.out");
	int n;
	in >> n;
	//in.seekg(0,ios_base::cur);
	string s;
	char code[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	getline (in, s);

	for (int i=0; i < n; i++) {
		getline (in, s);
		s = s + '\0';

		out << "Case #" << i+1 << ": ";

		int j=0;
		while (s[j]) {
			if (s[j] == ' ') {
				out << ' ';
				j++;
				continue;
			}
			int offset = s[j] - 'a';
			out << code[offset];
			j++;
		}
		out << endl;

	}

	return 0;
}

