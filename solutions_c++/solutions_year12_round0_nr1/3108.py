#include <stdio.h>
#include <string.h>
char G[102];
char m[260];
int main() {
	m['a']='y';m['b']='h';m['c']='e';m['d']='s';m['e']='o';m['f']='c';m['g']='v';m['h']='x';m['i']='d';m['j']='u';m['k']='i';m['l']='g';m['m']='l';m['n']='b';m['o']='k';m['p']='r';m['q']='z';m['r']='t';m['s']='n';m['t']='w';m['u']='j';m['v']='p';m['w']='f';m['x']='m';m['y']='a';m['z']='q';m[' ']=' ';
	int T;
	scanf("%d\n", &T);
	for( int t = 0 ; t < T ; ++t ) {
		fgets(G, 102, stdin); int s = strlen(G);
		if(G[s - 1]=='\n'){ G[s - 1]=0; --s; }
		for( int i = 0 ; i < s ; ++i )
			G[i]=m[G[i]];
		printf("Case #%d: %s\n", t + 1, G);
	}
}