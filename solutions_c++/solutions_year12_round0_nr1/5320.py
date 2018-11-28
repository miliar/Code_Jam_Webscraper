#include<iostream>
#include<map>
#include<string>
using namespace std;
map<char,char>Letters;
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("out.txt","w",stdout);
	Letters['a']='y';
Letters['b']='h';
Letters['c']='e';
Letters['d']='s';
Letters['e']='o';
Letters['f']='c';
Letters['g']='v';
Letters['h']='x';
Letters['i']='d';
Letters['j']='u';
Letters['k']='i';
Letters['l']='g';
Letters['m']='l';
Letters['n']='b';
Letters['o']='k';
Letters['p']='r';
Letters['q']='z';
Letters['r']='t';
Letters['s']='n';
Letters['t']='w';
Letters['u']='j';
Letters['v']='p';
Letters['w']='f';
Letters['x']='m';
Letters['y']='a';
Letters['z']='q';

	int cases;
	cin>>cases;
	cin.ignore();
	string input;
	for(int i=1;i<=cases;++i)
	{
		getline(cin,input);
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<input.size();++j)
			cout<<(input[j] == ' ' ? ' ' : Letters[input[j]]);
		cout<<endl;
	}
	return 0;
}