#include<iostream>
//#include <string.h>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;


char charMap[26];


string str;

int main()
{
	charMap['a'] = 'y';	
	charMap['b'] = 'h';	
	charMap['c'] = 'e';	
	charMap['d'] = 's';	
	charMap['e'] = 'o';	
	charMap['f'] = 'c';	
	charMap['g'] = 'v';	
	charMap['h'] = 'x';	
	charMap['i'] = 'd';	
	charMap['j'] = 'u';	
	charMap['k'] = 'i';	
	charMap['l'] = 'g';	
	charMap['m'] = 'l';	
	charMap['n'] = 'b';	
	charMap['o'] = 'k';	
	charMap['p'] = 'r';	
	charMap['q'] = 'z';	
	charMap['r'] = 't';	
	charMap['s'] = 'n';	
	charMap['t'] = 'w';	
	charMap['u'] = 'j';	
	charMap['v'] = 'p';	
	charMap['w'] = 'f';	
	charMap['x'] = 'm';	
	charMap['y'] = 'a';	
	charMap['z'] = 'q';
	ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
//	freopen("in.txt","r",stdin);
	int T;
	//scanf("%d\n",&T);
	in>>T;
	int i=0;
	for(;i<=T;i++)
	{
		getline(in,str);
		if(i == 0)
			continue;		
		int j=0;
		for(;j<str.length();j++)
		{
			if(str[j] == ' ')
				continue;
			str[j] = charMap[str[j]];
		}
		out<<"Case #"<<i<<": "<<str<<endl;
	}
//	fclose(stdin);
	return 0;
}