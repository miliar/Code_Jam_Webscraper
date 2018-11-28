#include <stdio.h>
#include <string.h>

int test;

int l;
char s[1000];

char t[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main() {              
	int i,j;
	scanf("%d ",&test);
	for (i=1; i<=test; i++) {
		gets(s);
		l = strlen(s);
		for (j=0; j<l; j++) {
			if (s[j] == ' ') continue;
			s[j] = t[s[j] - 'a'];
		}	
		printf("Case #%d: %s\n", i, s);
	}
	return 0;
}                                                            