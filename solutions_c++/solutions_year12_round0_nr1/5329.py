#include <cstdlib>
#include <iostream>

using namespace std;
int main(int argc, char *argv[])
{
	const char* ex1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	const char* res1 = "our language is impossible to understand";
	const char* ex2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	const char* res2 = "there are twenty six factorial possibilities";
	const char* ex3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	const char* res3 = "so it is okay if you want to just give up";
	char table[256];
	for(int i = 0; i < strlen(ex1); i++) {
		if(ex1[i] != ' ') table[ex1[i]] = res1[i];
	}
	for(int i = 0; i < strlen(ex2); i++) {
		if(ex2[i] != ' ') table[ex2[i]] = res2[i];
	}
	for(int i = 0; i < strlen(ex3); i++) {
		if(ex3[i] != ' ') table[ex3[i]] = res3[i];
	}
	table['z'] = 'q';
	table['q'] = 'z';
	int T;
	scanf("%d\n", &T);
	for(int i = 0; i < T; i++) {
		printf("Case #%d: ", i+1);
		char c;
		while(scanf("%c", &c) == 1) {
			if(c == '\n') break;
			if(c == ' ') printf(" ");
			else printf("%c", table[c]);
		}
		printf("\n");
	}
	return 0;
}
