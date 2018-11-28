#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

typedef map<char,char> mymap;

int main(void){
	freopen("input.in","r",stdin);
	freopen("ouput.out","w",stdout);
	mymap m;
	m['a']='y';m['b']='h';m['c']='e';m['d']='s';m['e']='o';
	m['f']='c';m['g']='v';m['h']='x';m['i']='d';m['j']='u';
	m['k']='i';m['l']='g';m['m']='l';m['n']='b';m['o']='k';
	m['p']='r';m['q']='z';m['r']='t';m['s']='n';m['t']='w';
	m['u']='j';m['v']='p';m['w']='f';m['x']='m';m['y']='a';
	m['z']='q';m[' ']=' ';
	string s;
	int t;
	scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		getline(cin,s);
		for(int j=0;j<s.size();j++){
			s[j] = m[s[j]];
		}
		cout<<"Case #"<<i<<": "<<s<<endl;
		s.clear();
	}
	return 0;
}