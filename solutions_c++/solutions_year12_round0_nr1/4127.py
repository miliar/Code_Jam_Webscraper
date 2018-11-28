#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char trans(char ch) {
	switch(ch) {
	case 'a':ch='y';break;
	case 'b':ch='h';break;
	case 'c':ch='e';break;
	case 'd':ch='s';break;
	case 'e':ch='o';break;
	case 'f':ch='c';break;
	case 'g':ch='v';break;
	case 'h':ch='x';break;
	case 'i':ch='d';break;
	case 'j':ch='u';break;
	case 'k':ch='i';break;
	case 'l':ch='g';break;
	case 'm':ch='l';break;
	case 'n':ch='b';break;
	case 'o':ch='k';break;
	case 'p':ch='r';break;
	case 'q':ch='z';break;
	case 'r':ch='t';break;
	case 's':ch='n';break;
	case 't':ch='w';break;
	case 'u':ch='j';break;
	case 'v':ch='p';break;
	case 'w':ch='f';break;
	case 'x':ch='m';break;
	case 'y':ch='a';break;
	case 'z':ch='q';break;
	}
	return ch;
}
int main() {
	int i,j,k,T;
	char str[1000000];
	freopen("A-small-attempt5.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	getchar();
	for(k=1;k<=T;k++) {
		gets(str);
		for(i=0;str[i]!='\0';i++) {
			if(str[i]==' ')	continue;
			else
				str[i]=trans(str[i]);
		}
		printf("Case #%d: %s\n",k,str);
	}
	return 0;
}