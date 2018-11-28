#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

char s[300];
char G[300];

void init(){
	s['a'] = 'y';
	s['b'] = 'h';
	s['c'] = 'e';
	s['d'] = 's';
	s['e'] = 'o';
	s['f'] = 'c';
	s['g'] = 'v';
	s['h'] = 'x';
	s['i'] = 'd';
	s['j'] = 'u';
	s['k'] = 'i';
	s['l'] = 'g';
	s['m'] = 'l';
	s['n'] = 'b';
	s['o'] = 'k';
	s['p'] = 'r';
	s['q'] = 'z';
	s['r'] = 't';
	s['s'] = 'n';
	s['t'] = 'w';
	s['u'] = 'j';
	s['v'] = 'p';
	s['w'] = 'f';
	s['x'] = 'm';
	s['y'] = 'a';
	s['z'] = 'q';
}
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	init();
	gets(G);
	for ( int cas = 1 ; gets(G) ; cas++ ){
		int len = strlen(G);
		for ( int i = 0 ; i < len ; i++ )
			if (G[i]>=97 && G[i]<=122) G[i] = s[G[i]];
		printf("Case #%d: %s\n",cas,G);
	}
}
