#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	
	int num, cont = 1;
	scanf("%d\n", &num);
	for(int j = 0; j<num; j++){
		char s[100000];
		gets(s);
		for(int i = 0 ; ((s[i]>='a' && s[i]<='z') || s[i]==' '); i++){
			switch(s[i]){
				case 'a': s[i] = 'y'; break;
				case 'b': s[i] = 'h'; break;
				case 'c': s[i] = 'e'; break;
				case 'd': s[i] = 's'; break;
				case 'e': s[i] = 'o'; break;
				case 'f': s[i] = 'c'; break;
				case 'g': s[i] = 'v'; break;
				case 'h': s[i] = 'x'; break;
				case 'i': s[i] = 'd'; break;
				case 'j': s[i] = 'u'; break;
				case 'k': s[i] = 'i'; break;
				case 'l': s[i] = 'g'; break;
				case 'm': s[i] = 'l'; break;
				case 'n': s[i] = 'b'; break;
				case 'o': s[i] = 'k'; break;
				case 'p': s[i] = 'r'; break;
				case 'q': s[i] = 'z'; break;
				case 'r': s[i] = 't'; break;
				case 's': s[i] = 'n'; break;
				case 't': s[i] = 'w'; break;
				case 'u': s[i] = 'j'; break;
				case 'v': s[i] = 'p'; break;
				case 'w': s[i] = 'f'; break;
				case 'x': s[i] = 'm'; break;
				case 'y': s[i] = 'a'; break;
				case 'z': s[i] = 'q'; break;
			}
		}
		printf("Case #%d: %s\n",(j+1),s);
	}
	return 0;
}

