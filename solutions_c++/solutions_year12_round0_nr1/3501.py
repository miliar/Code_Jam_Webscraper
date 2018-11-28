
/* Aishvarya Vishvesh
   Singh */

#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<cstring>
#include<stack>

using namespace std;

int main() {
	char ch[1000];
	char hash[1000];
	memset(hash,0,sizeof hash);
	hash['a']='y'; hash['b']='h'; hash['c']='e'; hash['d']='s'; hash['e']='o';
	hash['f']='c'; hash['g']='v'; hash['h']='x'; hash['i']='d'; hash['j']='u';
	hash['k']='i'; hash['l']='g'; hash['m']='l'; hash['n']='b'; hash['o']='k';
	hash['p']='r'; hash['q']='z'; hash['r']='t'; hash['s']='n'; hash['t']='w';
	hash['u']='j'; hash['v']='p'; hash['w']='f'; hash['x']='m'; hash['y']='a';
	hash['z']='q'; hash[' ']=' ';
	int t;
	cin >> t;
	for (int cas=1;cas<=t;cas++) {
		scanf(" %[^\n]",ch);
		int l=strlen(ch);
		cout << "Case #" << cas << ": ";
		for (int i=0;i<l;i++)
			if (hash[ch[i]])
				cout << hash[ch[i]];
			else
				cout << ch[i];
		cout << endl;
	}
	return 0;
}
