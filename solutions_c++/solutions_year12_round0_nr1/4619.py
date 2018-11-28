#include<iostream>
using namespace std;

int main(){
	char map[128];
	map[' ']=' ';
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
	
	int t,i;
	cin>>t;
	char a[1];
	cin.getline(a,1);
	for(i=1;i<=t;i++){
		char g[200];
		cin.getline(g,200);
		int l=cin.gcount()-1;
		int j;
		cout<<"Case #"<<i<<": ";
		for(j=0;j<l;j++)
			cout<<map[g[j]];
		cout<<endl;
	}
	return 0;
}
