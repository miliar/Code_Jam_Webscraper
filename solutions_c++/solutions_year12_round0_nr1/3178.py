#include <cstdio>

char a[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char b[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char key[128];
char str[111];
int main() {
	freopen("A-small-attempt6.in","r",stdin);
	freopen("out.out","w",stdout);
	for (int i = 0 ; a[i] ; i ++) {
		key[ a[i] ] = b[i];
	}
	key['z'] = 'q';
	key['q'] = 'z';
	int T;
	scanf("%d",&T);
	getchar();
	int cas = 1;
	while (T --) {
		gets(str);
		printf("Case #%d: ",cas ++);
		for (int i = 0 ; str[i] ; i ++) {
			printf("%c",key[ str[i] ]);
		}
		puts("");
	}
	return 0;
}