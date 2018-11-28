// GoogleCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <conio.h>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	long t;
	int len;
	//scanf("%ld",&t);
	ifstream myinput ("A-small-attempt0.in");
	ofstream myoutput("output.txt");
	myinput >> t;
	string str;
	getline(myinput,str);
	for(long i=0;i<t;i++)
	{
		getline(myinput,str);
		len = str.length();
		for(int j=0;j<len;j++)
		{
			switch(str[j])
			{
			case 'a': str[j] = 'y'; break;
			case 'b': str[j] = 'h'; break;
			case 'c': str[j] = 'e'; break;
			case 'd': str[j] = 's'; break;
			case 'e': str[j] = 'o'; break;
			case 'f': str[j] = 'c'; break;

			case 'g': str[j] = 'v'; break;
			case 'h': str[j] = 'x'; break;
			case 'i': str[j] = 'd'; break;
			case 'j': str[j] = 'u'; break;
			case 'k': str[j] = 'i'; break;

			case 'l': str[j] = 'g'; break;
			case 'm': str[j] = 'l'; break;
			case 'n': str[j] = 'b'; break;
			case 'o': str[j] = 'k'; break;
			case 'p': str[j] = 'r'; break;

			case 'q': str[j] = 'z'; break;
			case 'r': str[j] = 't'; break;
			case 's': str[j] = 'n'; break;
			case 't': str[j] = 'w'; break;
			case 'u': str[j] = 'j'; break;
			case 'v': str[j] = 'p'; break;
			case 'w': str[j] = 'f'; break;
			case 'x': str[j] = 'm'; break;
			case 'y': str[j] = 'a'; break;
			case 'z': str[j] = 'q'; break;
			default : break ;
			}
		}
		myoutput<<"Case #"<<(i+1)<<": "<<str<<"\n";
	}
	myinput.close();
	myoutput.close();
	//getch();
	//getch();
	return 0;
}

