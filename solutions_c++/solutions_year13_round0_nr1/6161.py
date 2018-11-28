// C_ConsoleApplication.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

string answ(int* sz, bool nc)
{
	for(int i = 0; i < 10 ; i++)
	{
		if(sz[i] == 4 || sz[i] == 8) return "X won";
		if(sz[i] == 32 || sz[i] == 36) return "O won";
	}
	return nc ? "Draw" : "Game has not completed";
}

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream outfile( "data.out" , ios::app );

	bool nc;
	int* sz = new int[10];
	for(int i = 0; i < 10; ++i) sz[i] = 0;

	string str;
    ifstream infile;
    infile.open ("data.in");
	getline(infile, str);
    int const cases = stoi(str);
	int n = 1;
	while(n <= cases)
	{
		int z = 0;
		nc = true;
		while(getline(infile, str) && z < 4) 
		{
			for(int i = 0; i < 4; ++i)
			{
				int num = 0;
				if(str[i] == 'T') num = 5;
				if(str[i] == 'O') num = 9;
				if(str[i] == 'X') num = 1;
				if(str[i] == '.') nc = false;
				
				switch ( z * 4 + i )
				{
					case 0:
						sz[0] += num;
						sz[1] += num;
						sz[2] += num;
					break;
					case 1:
						sz[0] += num;
						sz[6] += num;
					break;
					case 2:
						sz[0] += num;
						sz[7] += num;
					break;
					case 3:
						sz[0] += num;
						sz[8] += num;
						sz[9] += num;
					break;
					case 4:
						sz[2] += num;
						sz[3] += num;
					break;
					case 5:
						sz[1] += num;
						sz[3] += num;
						sz[6] += num;
					break;
					case 6:
						sz[3] += num;
						sz[7] += num;
						sz[9] += num;
					break;
					case 7:
						sz[3] += num;
						sz[8] += num;
					break;
					case 8:
						sz[2] += num;
						sz[4] += num;
					break;
					case 9:
						sz[4] += num;
						sz[6] += num;
						sz[9] += num;
					break;
					case 10:
						sz[1] += num;
						sz[4] += num;
						sz[7] += num;
					break;
					case 11:
						sz[4] += num;
						sz[8] += num;
					break;
					case 12:
						sz[2] += num;
						sz[5] += num;
						sz[9] += num;
					break;
					case 13:
						sz[5] += num;
						sz[6] += num;
					break;
					case 14:
						sz[5] += num;
						sz[7] += num;
					break;
					case 15:
						sz[1] += num;
						sz[5] += num;
						sz[8] += num;
					break;
					/*default:
						sz[0] = str[i];*/
				}
			}	
			++z;
		}
		outfile << "Case #" << n << ": " << answ(sz, nc) << endl;
		++n;
		for(int i = 0; i < 10; ++i) sz[i] = 0;
		//getline(infile, str);
	}
	infile.close();
	
	int i;
	//cin >> i;
	return 0;
}