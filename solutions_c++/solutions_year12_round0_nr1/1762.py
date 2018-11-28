// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<vector>
#include<string>
#include<cassert>
using namespace std;
int map[256];
int _tmain(int argc, _TCHAR* argv[])
{
  for(int i=0;i<256;++i){
    map[i]=i;
  }
  map['a']='y';
  map['b']='h';
  map['c']='e';
  map['d']='s';
  map['e']='o';
  map['f']='c';
  map['g']='v';
  map['h']='x';
  map['i']='d';
  map['j']='u';
  map['k']='i';
  map['l']='g';
  map['m']='l';
  map['n']='b';
  map['o']='k';
  map['p']='r';
  map['q']='z';
  map['r']='t';
  map['s']='n';
  map['t']='w';
  map['u']='j';
  map['v']='p';
  map['w']='f';
  map['x']='m';
  map['y']='a';
  map['z']='q';

  int t;
  cin >> t;
  cin.ignore(1023,'\n');
  for(int i=0;i<t;++i){
    string a;
    getline(cin,a);
    cerr << "String A:" << a << endl;
    for(int j=0;j<a.length();++j){
      a[j]=map[a[j]];
    }
    cout << "Case #" << (i+1) << ": " << a << endl;
  }
	return 0;
}

