#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
using namespace std;
int main()
{
	map<char,char> arr;
	  arr['y']='a';
	  arr['n']='b';
	  arr['f']='c';
	  arr['i']='d';
	  arr['c']='e';
	  arr['w']='f';
	  arr['l']='g';
	  arr['b']='h';
	  arr['k']='i';
	  arr['u']='j';
	  arr['o']='k';
	  arr['m']='l';
	  arr['x']='m';
	  arr['s']='n';
	  arr['e']='o';
	  arr['v']='p';
	  arr['z']='q';
	  arr['p']='r';
	  arr['d']='s';
	  arr['r']='t';
	  arr['j']='u';
	  arr['g']='v';
	  arr['t']='w';
	  arr['h']='x';
	  arr['a']='y';
	  arr['q']='z';
	int n;
	cin>>n;
	for(int caseno=1;caseno<=n;caseno++)
	{
		char in[1000];
		scanf(" %[^\n] ",in);
		for(int i=0;i<strlen(in);i++)
			if(in[i]>='a'&&in[i]<='z')
				in[i]=arr[in[i]];
		cout<<"Case #"<<caseno<<": "<<in<<endl;
	}
}                        
