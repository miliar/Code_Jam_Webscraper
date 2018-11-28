#include<cstdio>
#include<iostream>
using namespace std;
int test;
char s[1000];
char a[200];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&test);
	gets(s);
	a[' ']=' ';
	a['a']='y';
	a['b']='h';
	a['c']='e';
	a['d']='s';
	a['e']='o';
	a['f']='c';
	a['g']='v';
	a['h']='x';
	a['i']='d';
	a['j']='u';
	a['k']='i';
	a['l']='g';
	a['m']='l';
	a['n']='b';
	a['o']='k';
	a['p']='r';
	a['q']='z';
	a['r']='t';
	a['s']='n';
	a['t']='w';
	a['u']='j';
	a['v']='p';
	a['w']='f';
	a['x']='m';
	a['y']='a';
	a['z']='q';
	for (int t=1;t<=test;t++){
		gets(s);
		printf("Case #%d: ",t);
		for (int i=0;s[i];i++)
			putchar(a[s[i]]);
		putchar('\n');
	}
	return 0;
}
