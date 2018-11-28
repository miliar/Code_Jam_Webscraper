// ProgramA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

#define fabc(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fa0c(a,b) fabc( a, 0, ( b ) )
#define for_i(a) fa0c( i, ( a ) )
#define for_j(a) fa0c( j, ( a ) )
#define for_k(a) fa0c( k, ( a ) )

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k;
	map<char, char> googlereseMap;

	fstream f_input, f_output;
	f_input.open(argv[1],fstream::in);
	f_output.open("ProgramAOut.txt",fstream::out);

	googlereseMap['y']='a';
	googlereseMap['n']='b';
	googlereseMap['f']='c';
	googlereseMap['i']='d';
	googlereseMap['c']='e';
	googlereseMap['w']='f';
	googlereseMap['l']='g';
	googlereseMap['b']='h';
	googlereseMap['k']='i';
	googlereseMap['u']='j';
	googlereseMap['o']='k';
	googlereseMap['m']='l';
	googlereseMap['x']='m';
	googlereseMap['s']='n';
	googlereseMap['e']='o';
	googlereseMap['v']='p';
	googlereseMap['z']='q';
	googlereseMap['p']='r';
	googlereseMap['d']='s';
	googlereseMap['r']='t';
	googlereseMap['j']='u';
	googlereseMap['g']='v';
	googlereseMap['t']='w';
	googlereseMap['h']='x';
	googlereseMap['a']='y';
	googlereseMap['q']='z';


	//read test cases
	int T = 0;
	f_input >> T;
	string inputString;
	getline(f_input,inputString);
	for_i(T)
	{
		getline(f_input,inputString);
		cout << "Case #" << i+1 <<": ";
		cout << inputString;
		cout << endl;
		cout << "Case #" << i+1 <<": ";
		f_output << "Case #" << i+1 <<": ";
		
		//cout << inputString;
		for_k(inputString.length())
		{
			if(inputString[k] == ' ')
			{
				cout << ' ';
				f_output << ' ';
			}
			else
			{
				cout << googlereseMap.find(inputString[k])->second;
				f_output << googlereseMap.find(inputString[k])->second;
			}
		}
		cout << endl;

		f_output << endl;
	}

	f_input.close();
	f_output.close();
	return 0;
}
