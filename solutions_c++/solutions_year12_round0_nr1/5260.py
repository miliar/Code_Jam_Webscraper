#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
#include<sstream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
	int h,i;
	char r[256]={};
	r['a']='y';r['b']='h';r['c']='e';r['d']='s';r['e']='o';r['f']='c';r['g']='v';r['h']='x';r['i']='d';r['j']='u';r['k']='i';r['l']='g';r['m']='l';r['n']='b';r['o']='k';r['p']='r';r['q']='z';r['r']='t';r['s']='n';r['t']='w';r['u']='j';r['v']='p';r['w']='f';r['x']='m';r['y']='a';r['z']='q';r[' ']=' ';
	freopen("i","r",stdin);
	freopen("o","w",stdout);
	int t;
	cin>>t;
	string s;
	getline(cin,s);	
	for(h=1;h<=t;++h){
		getline(cin,s);
		int ln=s.length();
		for(i=0;i<ln;++i)
			s[i]=r[s[i]];
		cout<<"Case #"<<h<<": "<<s<<endl;
	}
}