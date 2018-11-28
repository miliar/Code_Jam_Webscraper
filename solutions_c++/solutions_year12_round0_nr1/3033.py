#include <iostream>
#include <fstream>
#include <string>

using namespace std;
char ReplaceChar(char c);

void main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	int n;
	in>>n;

	string *s = new string[n];
	getline(in,s[0]);
	for(int i=0;i<n;i++)
	{
		getline(in,s[i]);

		
	}
	for(int i=0;i<n;i++)
	{
		out<<"Case #"<<i+1<<": ";
		for(int j=0;j<s[i].length();j++)
			out<<ReplaceChar(s[i][j]);
		out<<endl;
	}

}

char ReplaceChar(char c)
{
	char r=c;
	switch(c)
	{
		case'a':r='y';
		break;
		case'b':r='h';
		break;
		case'c':r='e';
		break;
		case'd':r='s';
		break;
		case'e':r='o';
		break;
		case'f':r='c';
		break;
		case'g':r='v';
		break;
		case'h':r='x';
		break;
		case'i':r='d';
		break;
		case'j':r='u';
		break;
		case'k':r='i';
		break;
		case'l':r='g';
		break;
		case'm':r='l';
		break;
		case'n':r='b';
		break;
		case'o':r='k';
		break;
		case'p':r='r';
		break;
		case'q':r='z';
		break;
		case'r':r='t';
		break;
		case's':r='n';
		break;
		case't':r='w';
		break;
		case'u':r='j';
		break;
		case'v':r='p';
		break;
		case'w':r='f';
		break;
		case'x':r='m';
		break;
		case'y':r='a';
		break;
		case'z':r='q';
		break;
	}
	return r;
}