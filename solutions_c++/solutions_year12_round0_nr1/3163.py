#include<cstdio>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

char f[128];

void solve(){
	char s[128]; gets(s);
	for(int i=0;s[i];i++) putchar(f[s[i]]);
	puts("");
}

int main(){
	f[' ']=' '; f['a']='y'; f['b']='h'; f['c']='e'; f['d']='s'; f['e']='o';
	f['f']='c'; f['g']='v'; f['h']='x'; f['i']='d'; f['j']='u'; f['k']='i';
	f['l']='g'; f['m']='l'; f['n']='b'; f['o']='k'; f['p']='r'; f['q']='z';
	f['r']='t'; f['s']='n'; f['t']='w'; f['u']='j'; f['v']='p'; f['w']='f';
	f['x']='m'; f['y']='a'; f['z']='q';

	int T; scanf("%d ",&T);
	for(int t=1;t<=T;t++) printf("Case #%d: ",t), solve();
	return 0;
}
