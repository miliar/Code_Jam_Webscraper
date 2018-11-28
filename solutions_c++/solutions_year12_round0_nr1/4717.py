/*
ID: mitstud1
PROG: beads
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<map>
using namespace std;

char conv(char ch)
{
	switch(ch)
	{
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case 'm':
		return 'l';
	case 'n':
		return 'b';
	case 'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case 't':
		return 'w';
	case 'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	default:
		return ' ';
	}
}

int main()
{
	ifstream fin ("A-small-attempt1.in");
	ofstream fout ("A-small-attempt1.out");
	int n;
	fin>>n;
	string temp;
	getline(fin, temp);
	for(int i=0; i<n; i++)
	{
		string str, out;
		getline(fin, str);
		for(int j=0; j<str.length(); j++)
			out.push_back(conv(str[j]));
		fout<<"Case #"<<i+1<<": "<<out<<endl;
	}
	//fout<<out<<endl;
	
}