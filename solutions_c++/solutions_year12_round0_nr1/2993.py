#include<iostream>
#include<map>
#include<string>
#include<iostream>
#include<fstream>
#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>

using namespace std;


int main()
{
	map<char, char> Direct;
	Direct['a']='y';
	Direct['b']='h';
	Direct['c']='e';
	Direct['d']='s';
	Direct['e']='o';
	Direct['f']='c';
	Direct['g']='v';
	Direct['h']='x';
	Direct['i']='d';
	Direct['j']='u';
	Direct['k']='i';
	Direct['l']='g';
	Direct['m']='l';
	Direct['n']='b';
	Direct['o']='k';
	Direct['p']='r';
	Direct['q']='z';
	Direct['r']='t';
	Direct['s']='n';
	Direct['t']='w';
	Direct['u']='j';
	Direct['v']='p';
	Direct['w']='f';
	Direct['x']='m';
	Direct['y']='a';
	Direct['z']='q';
	Direct[' ']=' ';

	ifstream file1("A-small-attempt1.in");
    ofstream file2("A-small-attempt1.out");
	string T;
	//file1>>T;
	getline(file1,T);
	for(int i=1;i<=atoi(T.c_str());i++)
	{


		string qline,str;

		getline(file1,qline);

		for(int i=0;i<qline.size();i++)
		{
			str.append(1,Direct[qline.at(i)]);
		}
				file2<<"Case"<<" "<<"#"<<i<<": "<<str<<endl;

	}

	file1.close();
    file2.close();

	return 0;
}