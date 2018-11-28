#include <cstdio>
using namespace std;

void change(char &c) {
	switch(c) {
		case 'a': c = 'y'; break;
		case 'b': c = 'h'; break;
		case 'c': c = 'e'; break;
		case 'd': c = 's'; break;
		case 'e': c = 'o'; break;
		case 'f': c = 'c'; break;
		case 'g': c = 'v'; break;
		case 'h': c = 'x'; break;
		case 'i': c = 'd'; break;
		case 'j': c = 'u'; break;
		case 'k': c = 'i'; break;
		case 'l': c = 'g'; break;
		case 'm': c = 'l'; break;
		case 'n': c = 'b'; break;
		case 'o': c = 'k'; break;
		case 'p': c = 'r'; break;
		case 'q': c = 'z'; break;
		case 'r': c = 't'; break;
		case 's': c = 'n'; break;
		case 't': c = 'w'; break;
		case 'u': c = 'j'; break;
		case 'v': c = 'p'; break;
		case 'w': c = 'f'; break;
		case 'x': c = 'm'; break;
		case 'y': c = 'a'; break;
		case 'z': c = 'q'; break;
	}
	printf("%c", c);
}

int main() {
	int t;
 	scanf("%d", &t);
	getchar();
	for (int i=1; i<=t; i++) {
		char in[109];
//		getchar();
		gets(in);
		printf("Case #%d: ", i);
		for (int j=0; in[j] != '\0'; j++) {
			change(in[j]);
		}
		printf("\n");
	}
	return 0;
}
