#include<stdio.h>
#include<string.h>
char change[250];
int T;
char s[2000];
void predo(){
	change['a'] = 'y' ;
	change['b'] = 'h' ;
	change['c'] = 'e' ;
	change['d'] = 's' ;
	change['e'] = 'o' ;
	change['f'] = 'c' ;
	change['g'] = 'v' ;
	change['h'] = 'x' ;
	change['i'] = 'd' ;
	change['j'] = 'u' ;
	change['k'] = 'i' ;
	change['l'] = 'g' ;
	change['m'] = 'l' ;
	change['n'] = 'b' ;
	change['o'] = 'k' ;
	change['p'] = 'r' ;
	change['q'] = 'z' ;
	change['r'] = 't' ;
	change['s'] = 'n' ;
	change['t'] = 'w' ;
	change['u'] = 'j' ;
	change['v'] = 'p' ;
	change['w'] = 'f' ;
	change['x'] = 'm' ;
	change['y'] = 'a' ;
	change['z'] = 'q' ;
}
int main(){
	freopen("ansa.out","w",stdout);
	predo();
	scanf("%d\n",&T);
	for  (int t = 1 ; t <= T ; t ++){
		memset(s,0,sizeof(s));
		printf("Case #%d: ",t);
		gets(s);
		int l = strlen(s);
		for  ( int i = 0 ;  i < l ; i ++ ){
			if ( s[i] >= 'a' && s[i] <= 'z' )
				s[i] = change[s[i]];
		}
		puts(s);
	}
}
