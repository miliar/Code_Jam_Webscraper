#include<iostream>
#include<sstream>
using namespace std;



int main(){

	char M[1000];
	M['a']='y';
	M['b']='h';
	M['c']='e';
	M['d']='s';
	M['e']='o';
	M['f']='c';
	M['g']='v';
	M['h']='x';
	M['i']='d';
	M['j']='u';
	M['k']='i';
	M['l']='g';
	M['m']='l';
	M['n']='b';
	M['o']='k';
	M['p']='r';
	M['q']='z';
	M['r']='t';
	M['s']='n';
	M['t']='w';
	M['u']='j';
	M['v']='p';
	M['w']='f';
	M['x']='m';
	M['y']='a';
	M['z']='q';
	M[' ']=' ';
	int cases;
	cin>>cases;
	getchar();
	for(int kases=1;kases<=cases;kases++){
		char s[10000];
		cin.getline(s, 10000);
		for(int j=0;s[j]!='\n';j++)
			s[j]=M[s[j]];
		cout<<"Case #"<<kases<<": "<<s<<endl;
	}
	return 0;
}
