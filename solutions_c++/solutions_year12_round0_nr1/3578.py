#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <fstream>
using namespace std;
void solve();

#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;

int main() {
	freopen("input", "r", stdin);
	freopen("output","w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<"\n";
	}
	return 0;
}

void solve(){
	map<char, char> a;
a['e']='o';
a['j']='u';
a['p']='r';
a['m']='l';
a['y']='a';
a['s']='n';
a['l']='g';
a['c']='e';
a['k']='i';
a['d']='s';
a['x']='m';
a['v']='p';
a['n']='b';
a['r']='t';
a['i']='d';
a['b']='h';
a['t']='w';
a['a']='y';
a['h']='x';
a['w']='f';
a['f']='c';
a['o']='k';
a['u']='j';
a['g']='v';
a['z']='q';
a['q']='z';
string s;
getline(cin,s);
for(char t:s){
	if(a.find(t)!=a.end())
		cout<<a[t];
	else
		cout<<t;
}
}