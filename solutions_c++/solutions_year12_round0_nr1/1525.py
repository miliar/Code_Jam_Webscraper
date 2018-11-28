#include<iostream>
#include<string>
#include<map>
using namespace std;
int main(){
	map<char,char> c;
	c['a']='y';
	c['b']='h';
	c['c']='e';
	c['d']='s';
	c['e']='o';
	c['f']='c';
	c['g']='v';
	c['h']='x';
	c['i']='d';
	c['j']='u';
	c['k']='i';
	c['l']='g';
	c['m']='l';
	c['n']='b';
	c['o']='k';
	c['p']='r';
	c['q']='z';
	c['r']='t';
	c['s']='n';
	c['t']='w';
	c['u']='j';
	c['v']='p';
	c['w']='f';
	c['x']='m';
	c['y']='a';
	c['z']='q';
	int n;
	cin>>n;
	cin.ignore();
	int now=1;
	while(n--){
		string s;
		getline(cin,s);
		cout<<"Case #"<<now++<<": ";
		for(int i=0;i<s.size();i++){
			if(s[i]!=' ')
			cout<<c[s[i]];
			else
			cout<<' ';
		}
		cout<<endl;
	}
	return 0;
}