// Author: Sridhar Krishnan (sridharkritha@gmail.com)

#include "stdafx.h" // Needed only for Visual studio IDE

#include<iostream>
#include<vector>
#include<map>
#include<string>
#include <limits>
using namespace std;

//ejp mysljylc kd kxveddknmc re jsicpdrysi
//our language is impossible to understand

int main()
{
	freopen("q1.in", "r", stdin);
    freopen("a1.out", "w", stdout);

	map<char,char>m;
	
	m[' ']=' ';
	m['e']='o';
	m['j']='u';
	m['p']='r';

	m['m']='l';
	m['y']='a';
	m['s']='n';
	m['l']='g';
	m['j']='u';
	m['y']='a';
	m['l']='g';
	m['c']='e';

	m['k']='i';
	m['d']='s';

	m['k']='i';
	m['x']='m';
	m['v']='p';
	m['e']='o';
	m['d']='s';
	m['d']='s';
	m['k']='i';
	m['n']='b';
	m['m']='l';
	m['c']='e';

	m['r']='t';
	m['e']='o';
	

	m['j']='u';
	m['s']='n';
	m['t']='w';
	m['c']='e';
	m['p']='r';
	m['d']='s';
	m['b']='h';
	m['y']='a';
	m['s']='n';
	m['i']='d';
	m['h']='x';
	m['w']='f';
	m['f']='c';
	m['o']='k';
	m['a']='y';
	m['u']='j';
	m['g']='v';
	m['z']='q';
	m['q']='z';

	string str;
	int n;
	cin>>n;
	cin.clear();
	cin.ignore(numeric_limits<streamsize>::max(), '\n'); 

	for(int j=1;j<=n;j++)
	{

	getline (cin,str);   
	cout<<"Case #"<<j<<": ";
	for(unsigned int i=0; i<str.length();i++)
		cout<<m[str[i]];
	cout<<endl;
	}
	


	
	return 0;	
}