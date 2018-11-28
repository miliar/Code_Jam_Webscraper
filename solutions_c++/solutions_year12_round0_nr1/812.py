#include <cstdio>

char english[26]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int T;

int main()
{
	scanf("%d\n", &T);

	for(int i=0; i<T; i++) {
		printf("Case #%d: ", i+1);
		char c;
		do {
			scanf("%c", &c);
			if(c==' ' || c=='\n') printf("%c", c);
			else printf("%c", english[c-'a']);
		} while(c!='\n' && c!=EOF);
	}

	return 0;
}
