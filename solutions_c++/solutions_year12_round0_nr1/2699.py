// SpeakinginTongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>

using namespace std;

inline char translate(char c)
{
	switch (c)
	{
	case 'a': return 'y';
	case 'b': return 'h';
	case 'c': return 'e';
	case 'd': return 's';
	case 'e': return 'o';
	case 'f': return 'c';
	case 'g': return 'v';
	case 'h': return 'x';
	case 'i': return 'd';
	case 'j': return 'u';
	case 'k': return 'i';
	case 'l': return 'g';
	case 'm': return 'l';
	case 'n': return 'b';
	case 'o': return 'k';
	case 'p': return 'r';
	case 'q': return 'z';
	case 'r': return 't';
	case 's': return 'n';
	case 't': return 'w';
	case 'u': return 'j';
	case 'v': return 'p';
	case 'w': return 'f';
	case 'x': return 'm';
	case 'y': return 'a';
	case 'z': return 'q';
	case ' ': return ' ';
	}
}

int main(int argc, char* argv[])
{
	int t;
	char c;
	cin>>t;
	getchar();
	for (int i = 1; i <= t; i++)
	{
		cout<<"Case #"<<i<<": ";
		while ((c = getchar()) && c > 96 && c < 123 || c == 32)
			cout<<translate(c);
		cout<<endl;
	}
	return 0;
}

