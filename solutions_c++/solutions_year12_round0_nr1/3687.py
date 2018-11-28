#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

map<char, char> convert;

inline void init()
{
	convert['a']='y';
convert['b']='h';
convert['c']='e';
convert['d']='s';
convert['e']='o';
convert['f']='c';
convert['g']='v';
convert['h']='x';
convert['i']='d';
convert['j']='u';
convert['k']='i';
convert['l']='g';
convert['m']='l';
convert['n']='b';
convert['o']='k';
convert['p']='r';
convert['q']='z';
convert['r']='t';
convert['s']='n';
convert['t']='w';
convert['u']='j';
convert['v']='p';
convert['w']='f';
convert['x']='m';
convert['y']='a';
convert['z']='q';
}

int n;
string str;

int main()
{
	init();
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);

	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
	{
		getline(cin, str);
		for (int j =0; j < str.size(); j++)
			if (str[j] >= 'a' && str[j] <= 'z')
				str[j] = convert[str[j]];

		printf("Case #%d: %s\n", i+1, str.c_str());
	}
}