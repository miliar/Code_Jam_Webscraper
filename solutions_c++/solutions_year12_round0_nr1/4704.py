#include<map>
#include <stdio.h>
#include <stdlib.h>
#include<iostream>

using namespace std;
int main()
{
	map <char,char> dict;
	dict['a']= 'y';
	dict['b'] = 'h';
	dict['c'] = 'e';
	dict['d']='s';
	dict['e']='o';
	dict['f']='c';
	dict['g']='v';
	dict['h']='x';
	dict['i']='d';
	dict['j']='u';
	dict['k']='i';
	dict['l']='g';
	dict['m']='l';
	dict['n']='b';
	dict['o']='k';
	dict['p']='r';
	dict['q']='z';
	dict['r']='t';
	dict['s']='n';
	dict['t']='w';
	dict['u']='j';
	dict['v']='p';
	dict['w']='f';
	dict['x']='m';
	dict['y']='a';
	dict['z']='q';

	int t,j;
	scanf("%d", &t);
	for(j=0;j<t;j++)
	{
		char ch;
		char str[110];
		scanf("%[\n]",&ch);
		scanf("%[^\n]",str);

		cout<<"Case #"<<j+1<<": ";
		int i =0;
		while(str[i]!='\0')
		{
			if(str[i] == ' ')
				cout << " ";
			else
				cout <<dict[str[i]];
			i++;
		}
		cout << endl;
	}
	return 0;
}
