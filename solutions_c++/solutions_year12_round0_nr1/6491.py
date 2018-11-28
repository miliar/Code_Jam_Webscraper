// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	char mappings[] = {
			'y', //a
			'h', //b
			'e', //c
			's', //d
			'o', //e
			'c', //f
			'v', //g
			'x', //h
			'd', //i
			'u', //j
			'i', //k
			'g', //l
			'l', //m
			'b', //n
			'k', //o
			'r', //p
			'z', //q
			't', //r
			'n', //s
			'w', //t
			'j', //u
			'p', //v
			'f', //w
			'm', //x
			'a', //y
			'q', //z
	};
	char original[101],output[101];
	int cases = 0;
	int y;
	unsigned int index;
	ofstream fout;
	ifstream fin;
	fin.open("in.txt",ios::in);
	if (!fin)
	{
		cout<<"Error opening input file\n";
		return 0;
	}

	fout.open("answer.txt");
	if (!fout.is_open())
	{
		cout<<"Error opening output file\n";
		return 0;
	}
	fin.getline(original,100,'\n');
	cases = atoi(original);
	for(int x = 0; x < cases; x++)
	{
		memset(original,0,100);
		memset(output,0,100);
		fin.getline(original,101,'\n');
		cout<<"read: "<<original<<endl;
		for(y = 0;;y++)
		{
			if (!original[y])
				break;
			else if (original[y] == ' ')
			{
				output[y] = ' ';
				continue;
			}

			index = original[y] - 97;
			if (index < 26)
				output[y] = mappings[index];
			else
				cout<<"Invalid character read in pos "<<y<<" ("<<original[y]<<")"<<endl;
		}
		output[y] = 0;
		cout<<"Deciphered: "<<output<<endl;
		fout<<"Case #"<<x+1<<": "<<output<<endl;
	}

	cout<<"Done.";
	fout.close();
	fin.close();
	getchar();
	return 0;
}

