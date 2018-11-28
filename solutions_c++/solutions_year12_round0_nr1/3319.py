#include<iostream>
#include<map>
using namespace std;
map<char,char>M;
void init()
{
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
	M['z']='q';
	M['y']='a';
	M[' ']=' ';
	M['\n']='\n';
	M['\r']='\r';
}
string text;
int solve(int n)
{
	string res(text);
	//cout<<res<<endl;
	for(int i=0;i<text.length();i++)
	{
		res[i] = M[text[i]];
	}
	cout<<"Case #"<<n<<": "<<res<<endl;
}
int main()
{
	init();
	int t;
	cin>>t;
	getline(cin,text);
	for(int i=0;i<t;i++)
	{
		getline(cin,text);
		//cout<<text<<endl;
		solve(i+1);
	}
}

