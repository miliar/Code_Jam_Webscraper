#include <iostream>
#include <fstream>
#include<string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("M.out");
	int N;
	cin >> N;
	string text;
	getline(cin, text);
	for(int L = 1; L <= N; L++)
	{
		getline(cin, text);
		int i;
		for(i=0;i<text.size();i++)
		{
			switch(text[i]){
			case 'y':text[i]='a';break;
			case 'n':text[i]='b';break;
			case 'f':text[i]='c';break;
			case 'i':text[i]='d';break;
			case 'c':text[i]='e';break;
			case 'w':text[i]='f';break;
			case 'l':text[i]='g';break;
			case 'b':text[i]='h';break;
			case 'k':text[i]='i';break;
			case 'u':text[i]='j';break;
			case 'o':text[i]='k';break;
			case 'm':text[i]='l';break;
			case 'x':text[i]='m';break;
			case 's':text[i]='n';break;
			case 'e':text[i]='o';break;
			case 'v':text[i]='p';break;
			case 'z':text[i]='q';break;
			case 'p':text[i]='r';break;
			case 'd':text[i]='s';break;
			case 'r':text[i]='t';break;
			case 'j':text[i]='u';break;
			case 'g':text[i]='v';break;
			case 't':text[i]='w';break;
			case 'h':text[i]='x';break;
			case 'a':text[i]='y';break;
			case 'q':text[i]='z';break;
			default :break;
			}
		}
		cout<<"Case #"<<L<<": "<<text<<endl;		
	}
}