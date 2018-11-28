#include <cstdio>
#include <cstring>
char s[105];
char rp[256];
int main(){
	rp['a']='y';
	rp['b']='h';
	rp['c']='e';
	rp['d']='s';
	rp['e']='o';
	rp['f']='c';
	rp['g']='v'; //notice
	rp['h']='x';
	rp['i']='d';
	rp['j']='u';
	rp['k']='i';
	rp['l']='g';
	rp['m']='l';
	rp['n']='b';
	rp['o']='k';
	rp['p']='r';
	rp['q']='z';
	rp['r']='t';
	rp['s']='n';
	rp['t']='w';
	rp['u']='j';
	rp['v']='p';
	rp['w']='f';
	rp['x']='m';
	rp['y']='a';
	rp['z']='q'; //notice
	rp[' ']=' ';
	int T;
	scanf("%d\n",&T);
	for (int i=1;i<=T;++i){
		memset(s,0,sizeof(s));
		gets(s);
		for (int j=0;j<strlen(s);++j){
			s[j]=rp[s[j]];
		}
		printf("Case #%d: %s\n",i,s);
	}
	return 0;
}
