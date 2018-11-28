#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
map<char,char> mp;
void init()
{
	mp['a']='y';	mp['b']='h';	mp['c']='e';	mp['d']='s';	mp['e']='o';
	mp['f']='c';	mp['g']='v';	mp['h']='x';	mp['i']='d';	mp['j']='u';
	mp['k']='i';	mp['l']='g';	mp['m']='l';	mp['n']='b';	mp['o']='k';
	mp['p']='r';	mp['q']='z';	mp['r']='t';	mp['s']='n';	mp['t']='w';
	mp['u']='j';	mp['v']='p';	mp['w']='f';	mp['x']='m';	mp['y']='a';
	mp['z']='q';mp[' ']=' ';

}
int main()
{
	init();
	ifstream cin("A-small-attempt4.in");
	ofstream cout("data.out");
	char s[10000];
	int k=1,N;
	char ch;
	cin>>N;
	cin.getline(s,100000);
	while(N--)
	{
		cin.getline(s,10000);
		cout<<"Case #"<<k++<<": "; 
		for(int i=0;s[i]!='\0';i++)
			cout<<mp[s[i]];
		cout<<endl;
	}
	return 0;
}