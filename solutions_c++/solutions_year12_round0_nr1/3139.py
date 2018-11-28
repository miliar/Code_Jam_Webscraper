// cj1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w",stdout); 
    int T; 
        string str; 
		char x[26];
		x['y'-97] = 'a';
		x['n'-97] = 'b';
		x['f'-97] = 'c';
		x['i'-97] = 'd';
		x['c'-97] = 'e';
		x['w'-97] = 'f';
		x['l'-97] = 'g';
		x['b'-97] = 'h';
		x['k'-97] = 'i';
		x['u'-97] = 'j';
		x['o'-97] = 'k';
		x['m'-97] = 'l';
		x['x'-97] = 'm';
		x['s'-97] = 'n';
		x['e'-97] = 'o';
		x['v'-97] = 'p';
		x['z'-97] = 'q';
		x['p'-97] = 'r';
		x['d'-97] = 's';
		x['r'-97] = 't';
		x['j'-97] = 'u';
		x['g'-97] = 'v';
		x['t'-97] = 'w';
		x['h'-97] = 'x';
		x['a'-97] = 'y';
		x['q'-97] = 'z';

        cin >> T;
		getline(cin, str);
        for(int tc=1;tc<=T;tc++) 
        { 
			getline(cin, str);
			for( int i =0; i < str.length();++i)
			{
				if(str[i] != ' ')
				 str.replace(i,1,1, x[str[i]-97]);
			}
			cout << "Case #"<<tc<<": "<< str <<endl; 
        } 
	fclose(stdin);
	fclose(stdout);
	return 0;
}

