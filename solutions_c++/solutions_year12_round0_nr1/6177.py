#include<iostream>
using namespace std;
#include<string.h>
#include<stdio.h>

int decode(char e)
{
	char hash[255] = {0};
	
	
	hash [' '] = ' ';
	hash ['a'] = 'y';
	hash ['b'] = 'h';
	hash ['c'] = 'e';
	hash ['d'] = 's';
	hash ['e'] = 'o';
	hash ['f'] = 'c';
	hash ['g'] = 'v';
	hash ['h'] = 'x';
	hash ['i'] = 'd';
	hash ['j'] = 'u';
	hash ['k'] = 'i';
	hash ['l'] = 'g';
	hash ['m'] = 'l';
	hash ['n'] = 'b';
	hash ['o'] = 'k';
	hash ['p'] = 'r';
	hash ['q'] = 'z';
	hash ['r'] = 't';
	hash ['s'] = 'n';
	hash ['t'] = 'w';
	hash ['u'] = 'j';
	hash ['v'] = 'p';
	hash ['w'] = 'f';
	hash ['x'] = 'm';
	hash ['y'] = 'a';
	hash ['z'] = 'q';
	
	return hash[e];
}
	
	
int main()
{
	int T;
	char *G = new char [200];
	cin >> T;

	for(int i=0;i<T+1;i++)
	{
		int j;
		char *D = new char[200];
		cin.getline(G, 200,'\n');
		for  (j = 0; j < strlen(G); j++)
		{
			D[j] = decode(G[j]);
		}
		D[j] ='\0';
		if(i>0)
			cout<<"Case #"<<i<<": "<<D<<endl;
	}
}
