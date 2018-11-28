#include<iostream>
#include<map>
#include<string>
using namespace std;

int main()
{
map <char,char> mapper;
mapper['a']='y';
mapper['b']='h';
mapper['c']='e';
mapper['d']='s';
mapper['e']='o';
mapper['f']='c';
mapper['g']='v';
mapper['h']='x';
mapper['i']='d';
mapper['j']='u';
mapper['k']='i';
mapper['l']='g';
mapper['m']='l';
mapper['n']='b';
mapper['o']='k';
mapper['p']='r';
mapper['q']='z';
mapper['r']='t';
mapper['s']='n';
mapper['t']='w';
mapper['u']='j';
mapper['v']='p';
mapper['w']='f';
mapper['x']='m';
mapper['y']='a';
mapper['z']='q';
mapper[' ']=' ';

int cases,i=1;
string input;
string::iterator it;
cin>>cases;
getline(cin,input);
while(cases--)
{
	getline(cin,input);
	cout<<"Case #"<<i<<": ";
	for( it=input.begin(); it < input.end(); it++)
	{
		cout<<mapper[*it];
	}
	cout<<endl;
	i++;

}

return 0;
}
