
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char arr[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}; 


int _tmain(int argc, _TCHAR* argv[])
{
	int n = 1;
	int i,j;
	int temp;
	char s[200];

	ifstream fin;
	ofstream fout;

	fout.open("output.txt");

	fin.open("A-small-attempt0.in");
	fin >> n;
	fin.getline(s,200);

	for ( i = 0; i < n; ++i)
	{
		fout << "Case #" << i+1 << ": ";
		fin.getline(s, 200);

		for ( j = 0; j < strlen(s); ++j)
		if (s[j] == ' ')
			fout << " ";
		else
		{
			temp = int(s[j]);
			if ( temp < 97)
				temp = temp + 32;

			fout << arr[temp - 97];
		}
		fout << endl;
	}

	fin.close();

	fout.close();	
	
	return 0;
}

