#include<cstdio>
#include<cstring>

char a[100];

int main(){
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
int t;
char s1[200];
scanf("%d",&t); gets(s1);
for (int tt=1;tt<=t;++tt){
	gets(s1);
	int len=strlen(s1);
	for (int i=0;i<len;++i) if (s1[i]!=' ') s1[i]=a[s1[i]];
	printf("Case #%d: %s\n",tt,s1);
}
return 0;
}
