#include<vector>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
// #include <cstdlib>

#include<algorithm>
#include<map>
#include<iostream>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	string combinestr;
	fin.open("A-small-attempt0.in");
	fout.open("results.txt");
	
	map<char,char> rep;
	rep['a']='y';
	rep['b']='h';
	rep['c']='e';
	rep['d']='s';
	rep['e']='o';
	rep['f']='c';
	rep['g']='v';
	rep['h']='x';
	rep['i']='d';
	rep['j']='u';
	rep['k']='i';
	rep['l']='g';
	rep['m']='l';
	rep['n']='b';
	rep['o']='k';
	rep['p']='r';
	rep['q']='z';
	rep['r']='t';
	rep['s']='n';
	rep['t']='w';
	rep['u']='j';
	rep['v']='p';
	rep['w']='f';
	rep['x']='m';
	rep['y']='a';
	rep['z']='q';
	

	int total;
	//fin>>total;
	string str;
	
	getline(fin,str);
	total=atof(str.c_str());
	
	
	//cout<<str;
	cout<<total<<endl;
	for(int i=0;i<total;i++){
		getline(fin,str);
		for(int count=0;count<str.size();count++){
			str[count]=rep[str[count]];
		}
		fout<<"Case #"<<i+1<<": "<<str<<endl;
	}
	
	system("pause");




}