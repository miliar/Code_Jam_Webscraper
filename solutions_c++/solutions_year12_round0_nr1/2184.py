#include <stdlib.h>
#include <stdio.h>

char change(char a){
	switch(a){
	case 'a':{return 'y'; break;}
	case 'b':{return 'h'; break;}
	case 'c':{return 'e'; break;}
	case 'd':{return 's'; break;}
	case 'e':{return 'o'; break;}
	case 'f':{return 'c'; break;}
	case 'g':{return 'v'; break;}
	case 'h':{return 'x'; break;}
	case 'i':{return 'd'; break;}
	case 'j':{return 'u'; break;}
	case 'k':{return 'i'; break;}
	case 'l':{return 'g'; break;}
	case 'm':{return 'l'; break;}
	case 'n':{return 'b'; break;}
	case 'o':{return 'k'; break;}
	case 'p':{return 'r'; break;}
	case 'q':{return 'z'; break;}
	case 'r':{return 't'; break;}
	case 's':{return 'n'; break;}
	case 't':{return 'w'; break;}
	case 'u':{return 'j'; break;}
	case 'v':{return 'p'; break;}
	case 'w':{return 'f'; break;}
	case 'x':{return 'm'; break;}
	case 'y':{return 'a'; break;}
	case 'z':{return 'q'; break;}
	default:{return ' ';}
	}
}

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int h=0;
	scanf("%d\n",&h);
	for(int t=0;t<h;t++){
		char a;
		printf("Case #%d: ",t+1);
		scanf("%c",&a);
		int i=0;
		while(a!='\n'){
			printf("%c",change(a));
			i++;
			scanf("%c",&a);
		}
		printf("\n");
	}
}