#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <bitset>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-out.txt","w",stdout);
	int t,T;
	int i;
	char str[1000],m[256];
	m['a']='y';
	m['b']='h';
	m['c']='e';
	m['d']='s';
	m['e']='o';
	m['f']='c';
	m['g']='v';
	m['h']='x';
	m['i']='d';
	m['j']='u';
	m['k']='i';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	m['q']='z';
	m['r']='t';
	m['s']='n';
	m['t']='w';
	m['u']='j';
	m['v']='p';
	m['w']='f';
	m['x']='m';
	m['y']='a';
	m['z']='q';
	m[' ']=' ';
	cin>>T;
	gets(str);
	for(t=1;t<=T;t++)
	{
		gets(str);
		printf("Case #%d: ",t);
		for(i=0;str[i];i++) putchar(m[str[i]]);
		puts("");
	}
	return 0;
}



