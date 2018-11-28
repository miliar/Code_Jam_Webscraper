#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<string>

using namespace std;

int s['{'];

string nows;

int main()
{
	s['a']='y';
	s['b']='h';
	s['c']='e';
	s['d']='s';
	s['e']='o';
	s['f']='c';
	s['g']='v';
	s['h']='x';
	s['i']='d';
	s['j']='u';
	s['k']='i';
	s['l']='g';
	s['m']='l';
	s['n']='b';
	s['o']='k';
	s['p']='r';
	s['q']='z';
	s['r']='t';
	s['s']='n';
	s['t']='w';
	s['u']='j';
	s['v']='p';
	s['w']='f';
	s['x']='m';
	s['y']='a';
	s['z']='q';
	int t;
	scanf("%d",&t);
	for (int a=1;a<=t;a++)
	{
		printf("Case #%d: ",a);
		getline(cin,nows);
		if (a==1) getline(cin,nows);
		int l=nows.size();
		for (int a=0;a<l;a++)
			if ((nows[a]>='a') && (nows[a]<='z')) printf("%c",s[nows[a]]);
			else printf("%c",nows[a]);
		printf("\n");
	}

	return 0;
}
