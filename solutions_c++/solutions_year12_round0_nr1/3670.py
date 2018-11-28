#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	map<char,char> al,a;
	al['a']='y';
	al['b']='n';
	al['c']='f';
	al['d']='i';
	al['e']='c';
	al['f']='w';
	al['g']='l';
	al['h']='b';
	al['i']='k';
	al['j']='u';
	al['k']='o';
	al['l']='m';
	al['m']='x';
	al['n']='s';
	al['o']='e';
	al['p']='v';
	al['q']='z';
	al['r']='p';
	al['s']='d';
	al['t']='r';
	al['u']='j';
	al['v']='g';
	al['w']='t';
	al['x']='h';
	al['y']='a';
	al['z']='q';
	a[' ']=' ';
	for(char c='a'; c<='z';c++){
		a[al[c]]=c;
	}
	int n;
	cin >> n;
	string s;
	getline(cin,s);
	for(int i=0;i<n;i++){
		getline(cin,s);
		cout << "Case #" << i+1 << ": ";
		for(int j=0;j<s.size();j++){
			cout << a[s[j]];
		}
		cout << endl;
	}
	return 0;
}