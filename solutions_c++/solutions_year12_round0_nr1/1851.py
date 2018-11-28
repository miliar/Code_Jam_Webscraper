#include <cstdio>
#include <cstring>

char s[200], match[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	int nT;
	scanf("%d", &nT);
	gets(s);
	for (int test = 1; test <= nT; test++){
		printf("Case #%d: ", test);
		gets(s);
		for (int i = 0, l = strlen(s); i < l; i++)
			if ('a' <= s[i] && s[i] <= 'z')
				s[i] = match[(int)s[i] - 'a'];
		puts(s);
	}
	
	return 0;
}
