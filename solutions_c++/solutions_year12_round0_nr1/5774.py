#include <map>
#include <stdio.h>
#include <string.h>

using namespace std;

char *source = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char *dest = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

int t;

char in[1024];

map<char,char> h;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.out","w",stdout);

	h['y'] = 'a';
	h['e'] = 'o';
	h['q'] = 'z';
	h['z'] = 'q';

	scanf("%d\n",&t);

	for (int i = 0 ; i < strlen(source); ++i) {
		h[source[i]] = dest[i];
	}
	int nr = 1;

	while (t--) {
		memset(in,0,sizeof(in));
		gets(in);
		printf("Case #%d: ",nr);
		++nr;
		
		int len = strlen(in);
		for (int i = 0 ; i < len ; ++i) {
			printf("%c",h[in[i]]);
		}
		if ( t != 0) {
			printf("\n");
		}
	}

	return 0;
}
