#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char str[102];
int k,t;
char x;
main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("data.out","w",stdout);
	while(scanf("%d",&t)==1){
		getchar();
		for(k=0;k<t;k++){
			gets(str);
			printf("Case #%d: ",k+1);
			for(int i=0;i<strlen(str);i++){
				switch(str[i]){
					case ' ':
						putchar(' ');
						break;
					case 'a':
						putchar('y');
						break;
					case 'b':
						putchar('h');
						break;
					case 'c':
						putchar('e');
						break;
					case 'd':
						putchar('s');
						break;
					case 'e':
						putchar('o');
						break;
					case 'f':
						putchar('c');
						break;
					case 'g':
						putchar('v');
						break;
					case 'h':
						putchar('x');
						break;
					case 'i':
						putchar('d');
						break;
					case 'j':
						putchar('u');
						break;
					case 'k':
						putchar('i');
						break;
					case 'l':
						putchar('g');
						break;
					case 'm':
						putchar('l');
						break;
					case 'n':
						putchar('b');
						break;
					case 'o':
						putchar('k');
						break;
					case 'p':
						putchar('r');
						break;
					case 'q':
						putchar('z');
						break;
					case 'r':
						putchar('t');
						break;
					case 's':
						putchar('n');
						break;
					case 't':
						putchar('w');
						break;
					case 'u':
						putchar('j');
						break;
					case 'v':
						putchar('p');
						break;
					case 'w':
						putchar('f');
						break;
					case 'x':
						putchar('m');
						break;
					case 'y':
						putchar('a');
						break;
					case 'z':
						putchar('q');
						break;
				}
			}
			putchar(10);
		}
	}
}
