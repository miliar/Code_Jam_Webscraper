#include<stdio.h>
#include<string.h>

char buf[1024],buf2[1024];
char map[254];

int main(){
	
	map['a'] = 'y';
	map['b'] = 'h';
	map['c'] = 'e';
	map['d'] = 's';
	map['e'] = 'o';
	map['f'] = 'c';
	map['g'] = 'v';
	map['h'] = 'x';
	map['i'] = 'd';
	map['j'] = 'u';
	map['k'] = 'i';
	map['l'] = 'g';
	map['m'] = 'l';
	map['n'] = 'b';
	map['o'] = 'k';
	map['p'] = 'r';
	map['q'] = 'z';
	map['r'] = 't';
	map['s'] = 'n';
	map['t'] = 'w';
	map['u'] = 'j';
	map['v'] = 'p';
	map['w'] = 'f';
	map['x'] = 'm';
	map['y'] = 'a';
	map['z'] = 'q';
	map[' '] = ' ';
	map['\0'] = '\0';
	
	int nteste;
	scanf("%d ",&nteste);
	
	for(int nt = 1;nt <= nteste;nt++){
		
		printf("Case #%d: ",nt);
		gets(buf);
		int tam = strlen(buf);
		
		for(int i=0;i <= tam;i++){
			buf2[i] = map[buf[i]];
		}
		
		printf("%s\n",buf2);
		
	}
}
