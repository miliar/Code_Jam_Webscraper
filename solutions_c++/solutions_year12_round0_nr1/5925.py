#include<iostream>
#include<cstdio>

char d[200];

using namespace std;

int main (int argc, char const* argv[])
{
	d['e']='o';
d['j']='u';
d['p']='r';
d[' ']=' ';
d['m']='l';
d['y']='a';
d['s']='n';
d['l']='g';
d['c']='e';
d['k']='i';
d['d']='s';
d['x']='m';
d['v']='p';
d['n']='b';
d['r']='t';
d['i']='d';
d['\n']='\n';
d['b']='h';
d['t']='w';
d['a']='y';
d['h']='x';
d['w']='f';
d['f']='c';
d['o']='k';
d['u']='j';
d['g']='v';
d['q']='z';
d['z']='q';
	int t;
	cin >> t;
	char s[200];
	gets(s);
	for (unsigned int i = 0; i < t; i += 1)
	{
		gets(s);
		//cout << s;
		cout << "Case #" << i+1 << ": ";	
		for (char* j = s; *j!='\0' ; ++j)
		{
			//cout  << *j;
			printf("%c", d[*j]);
		}
		printf("\n");
	}
	
	return 0;
}


