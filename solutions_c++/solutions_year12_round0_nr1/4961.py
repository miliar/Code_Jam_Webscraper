#include <stdio.h>
#include <iostream>
using namespace std;
#include <algorithm>
#include <map>


int main()
{
	map<char,char> google;
    map<char,char>::iterator it;

	google['a'] = 'y';
	google['b'] = 'h';
	google['c'] = 'e';
	google['d'] = 's';
	google['e'] = 'o';
	google['f'] = 'c';
	google['g'] = 'v';
	google['h'] = 'x';
	google['i'] = 'd';
	google['j'] = 'u';
	google['k'] = 'i';
	google['l'] = 'g';
	google['m'] = 'l';
	google['n'] = 'b';
	google['o'] = 'k';
	google['p'] = 'r';
	google['q'] = 'z';
	google['r'] = 't';
	google['s'] = 'n';
	google['t'] = 'w';
	google['u'] = 'j';
	google['v'] = 'p';
	google['w'] = 'f';
	google['x'] = 'm';
	google['y'] = 'a';
	google['z'] = 'q';
	google[' '] = ' ';

	int nol;
	scanf("%d\n",&nol);
	int c=0;
	while(nol)
	{	c++;
		nol--;	
		cout<<"Case #"<<c<<": ";
		string input,output;
		getline(cin,input);
		//cout<<input<<endl;
		for(int i=0;i<input.length();i++)
		{	//cout<<input[i]<<endl;
			cout<<google[input[i]];
		}
		cout<<endl;

	} 

}