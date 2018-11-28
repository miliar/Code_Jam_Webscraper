
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include<map>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( strcmp((char*)a , (char*)b) );
}

int main () {
	map<char, char> letra;
	letra['o']='e';
letra['e']='o';
letra['j']='u';
letra['p']='r';
letra['m']='l';
letra['y']='a';
letra['s']='n';
letra['l']='g';
letra['j']='u';
letra['y']='a';
letra['l']='g';
letra['c']='e';
letra['k']='i';
letra['d']='s';
letra['k']='i';
letra['x']='m';
letra['v']='p';
letra['e']='o';
letra['d']='s';
letra['d']='s';
letra['k']='i';
letra['n']='b';
letra['m']='l';
letra['c']='e';
letra['r']='t';
letra['e']='o';
letra['j']='u';
letra['s']='n';
letra['i']='d';
letra['c']='e';
letra['p']='r';
letra['d']='s';
letra['r']='t';
letra['y']='a';
letra['s']='n';
letra['i']='d';
letra['r']='t';
letra['b']='h';
letra['c']='e';
letra['p']='r';
letra['c']='e';
letra['y']='a';
letra['p']='r';
letra['c']='e';
letra['r']='t';
letra['t']='w';
letra['c']='e';
letra['s']='n';
letra['r']='t';
letra['a']='y';
letra['d']='s';
letra['k']='i';
letra['h']='x';
letra['w']='f';
letra['y']='a';
letra['f']='c';
letra['r']='t';
letra['e']='o';
letra['p']='r';
letra['k']='i';
letra['y']='a';
letra['m']='l';
letra['v']='p';
letra['e']='o';
letra['d']='s';
letra['d']='s';
letra['k']='i';
letra['n']='b';
letra['k']='i';
letra['m']='l';
letra['k']='i';
letra['r']='t';
letra['k']='i';
letra['c']='e';
letra['d']='s';
letra['d']='s';
letra['e']='o';
letra['k']='i';
letra['r']='t';
letra['k']='i';
letra['d']='s';
letra['e']='o';
letra['o']='k';
letra['y']='a';
letra['a']='y';
letra['k']='i';
letra['w']='f';
letra['a']='y';
letra['e']='o';
letra['j']='u';
letra['t']='w';
letra['y']='a';
letra['s']='n';
letra['r']='t';
letra['r']='t';
letra['e']='o';
letra['u']='j';
letra['j']='u';
letra['d']='s';
letra['r']='t';
letra['l']='g';
letra['k']='i';
letra['g']='v';
letra['c']='e';
letra['j']='u';
letra['v']='p';
letra['z']='q';
letra['q']='z';

char x;
char y[110];
int n;
cin>>n;
for(int i=0;i<n;i++){
	cout<<"Case #"<<i+1<<": ";
	while((x=getchar())=='\n');
	while(true){

		 if(x!=' ')
			cout<<letra[x];
		else cout<<" ";
		x=getchar();
		if(x=='\n')break;
	}
	cout<<'\n';
}
	


	return 0;
}
