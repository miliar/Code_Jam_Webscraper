/*
 * A.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: msaber


#include "A.h"

A::A() {
	// TODO Auto-generated constructor stub

}

A::~A() {
	// TODO Auto-generated destructor stub
}
*/

#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	map <char , char> alp ;
	alp['a']='y';
	alp['b']='h';
	alp['c']='e';
	alp['d']='s';
	alp['e']='o';
	alp['f']='c';
	alp['g']='v';
	alp['h']='x';
	alp['i']='d';
	alp['j']='u';
	alp['k']='i';
	alp['l']='g';
	alp['m']='l';
	alp['n']='b';
	alp['o']='k';
	alp['p']='r';
	alp['q']='z';
	alp['r']='t';
	alp['s']='n';
	alp['t']='w';
	alp['u']='j';
	alp['v']='p';
	alp['w']='f';
	alp['x']='m';
	alp['y']='a';
	alp['z']='q';
	alp[' ']=' ';
	int n;
	cin>>n;
	string s="";
	getline(cin , s);
	for(int i=1; i<=n ; i++)
	{
		string str ="";
		getline(cin , str);
		string result="";
		for(int j=0 ; j<str.length() ; j++)
		{
			result+=alp[str[j]];
		}
		//if(i!=0)
			cout<<"Case #"<<i<<": "<<result<<endl;
	}
}
