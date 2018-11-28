#include <stdio.h>
#include <string.h>
char text[200];
char mapa[260];
int main() {
	freopen("input.txt", "r", stdin);
	//freopen("ouput.txt", "w", stdout);
	mapa['a']='y';
	mapa['b']='h';
	mapa['c']='e';
	mapa['d']='s';
	mapa['e']='o';
	mapa['f']='c';
	mapa['g']='v';
	mapa['h']='x';
	mapa['i']='d';
	mapa['j']='u';
	mapa['k']='i';
	mapa['l']='g';
	mapa['m']='l';
	mapa['n']='b';
	mapa['o']='k';
	mapa['p']='r';
	mapa['q']='z';
	mapa['r']='t';
	mapa['s']='n';
	mapa['t']='w';
	mapa['u']='j';
	mapa['v']='p';
	mapa['w']='f';
	mapa['x']='m';
	mapa['y']='a';
	mapa['z']='q';
	mapa[' ']=' ';

	int lines;
	scanf("%d\n", &lines);
	int caso = 1;
	
	while(fgets(text, 200, stdin)!=NULL){
		int size = strlen(text);
		if(text[size-1]=='\n'){	text[size-1]=0;	--size;	}
		for(int i=0;i<size;++i){
			text[i]=mapa[text[i]];
		}
		printf("Case #%d: %s\n", caso, text);
		caso++;
	}
}