// develo.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <utility>
#include <queue>
#include <iostream>
#include <sstream>
#include <map>
#include <ctype.h>

#define LL long long
#define fr(i,n) for(i=0;i<n;i++)
#define INF (2000000000)
#define FOR(n) for(int i = 0;i < n;i++)
#define CLEAR(x) memset(x,0,sizeof(x))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back((a))

using namespace std;

map<char,char> g;

void init(){
	g['a']='y';
	g['b']='h';
	g['c']='e';
	g['d']='s';
	g['e']='o';
	g['f']='c';
	g['g']='v';
	g['h']='x';
	g['i']='d';
	g['j']='u';
	g['k']='i';
	g['l']='g';
	g['m']='l';
	g['n']='b';
	g['o']='k';
	g['p']='r';
	g['q']='z';
	g['r']='t';
	g['s']='n';
	g['t']='w';
	g['u']='j';
	g['v']='p';
	g['w']='f';
	g['x']='m';
	g['y']='a';
	g['z']='q';
	g[' ']=' ';
}

int main()
{
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	init();
	string str;
	int n;
	cin >> n;
	getchar();
	FOR(n){
		cout << "Case #" << i+1 << ": "; 
		getline(cin,str);
		for (int j = 0;j < str.size();j++){
			cout << g[str[j]];
		}
		cout << endl;
	}

	return 0;
}

