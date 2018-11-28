#include<cstdio>
#include<string.h>
#include<iostream>
using namespace std;
int main() {
	int T; scanf("%d", &T);
	char c; scanf("%c", &c);
	int i = 1;
	char s[103];
	while (i <= T) {
	
		cin.getline(s, 102);
		for(int j = 0; j < strlen(s); j++) {
			switch (s[j]) {
				case 'e': s[j] = 'o'; break; 
				case 'j': s[j] = 'u'; break;
				case 'p': s[j] = 'r'; break;
				case 'm': s[j] = 'l'; break;
				case 'y': s[j] = 'a'; break;
				case 's': s[j] = 'n'; break;
				case 'l': s[j] = 'g'; break;
				case 'c': s[j] = 'e'; break;
				case 'k': s[j] = 'i'; break;
				case 'd': s[j] = 's'; break; 
				case 'x': s[j] = 'm'; break;
				case 'v': s[j] = 'p'; break;
				case 'n': s[j] = 'b'; break;
				case 'r': s[j] = 't'; break;
				case 'i': s[j] = 'd'; break;
				case 'a': s[j] = 'y'; break;
				case 'o': s[j] = 'k'; break;
				case 'z': s[j] = 'q'; break;
				case 'f': s[j] = 'c'; break;
				case 'g': s[j] = 'v'; break; 
				case 'h': s[j] = 'x'; break;
				case 'q': s[j] = 'z'; break;
				case 't': s[j] = 'w'; break;
				case 'b': s[j] = 'h'; break;
				case 'w': s[j] = 'f'; break;
				case 'u': s[j] = 'j'; break;
				default:
				 s[j] = s[j];
			}
		}
		printf("Case #%d: %s\n", i, s);
		i++;
	}
}
