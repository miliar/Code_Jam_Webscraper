#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <map>
using namespace std;

map<char,char> mp;
void mapping()
{
	mp['y']='a';
	mp['n']='b';
	mp['f']='c';
	mp['i']='d';
	mp['c']='e';
	mp['w']='f';
	mp['l']='g';
	mp['b']='h';
	mp['k']='i';
	mp['u']='j';
	mp['o']='k';
	mp['m']='l';
	mp['x']='m';
	mp['s']='n';
	mp['e']='o';
	mp['v']='p';
	mp['z']='q';
	mp['p']='r';
	mp['d']='s';
	mp['r']='t';
	mp['j']='u';
	mp['g']='v';
	mp['t']='w';
	mp['h']='x';
	mp['a']='y';
	mp['q']='z';
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	mapping();
	int Case,len;
	string str;
	scanf("%d ",&Case);
	for(int ca=0;ca<Case;ca++)
	{
		getline(cin,str);
		len=str.length();
		printf("Case #%d: ",ca+1);
		for(int i=0;i<len;i++)
		{
			if(mp.find(str[i]) != mp.end())
			{
				printf("%c",mp[str[i]]);
			}
			else printf("%c",str[i]);
		}
		puts("");
	}
	return 0;
}
