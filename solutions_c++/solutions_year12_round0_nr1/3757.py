#include <stdio.h>
#include <string.h>

char table[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main() {
	int T, x = 1;
	char str[500], buf;
	
	scanf("%d",&T);
	
	while(x<=T) {
		scanf("%c",&buf);
		scanf("%[^\n]s",str);
		
		int len = strlen(str);
		
		printf("Case #%d: ",x);
		for(int i=0;i<len;++i) {
			if(str[i]==' ')
				printf(" ");
			else {
				printf("%c",table[str[i]-'a']);
			}
		}
		printf("\n");
		++x;
	}
	
	return 0;
}