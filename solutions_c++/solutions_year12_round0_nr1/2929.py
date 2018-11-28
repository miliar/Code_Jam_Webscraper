#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int M[200];
void change(char *s, char *to) {
			int len = strlen(s);
			for( int i = 0; i < len; ++ i) {
				if(s[i] != ' ') {
					M[s[i]] = to[i];
				}
			}
}
int main() {
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
		int T;
		scanf("%d\n", &T);
		char s[109];
		char to[109];
		char *Map ="yhesocvxduiglbkrztnwjpfmaq";	
	//	change("ejp mysljylc kd kxveddknmc re jsicpdrysi", 
	//					"our language is impossible to understand");
	//	change("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
//						"there are twenty six factorial possibilities");
	//	change("de kr kd eoya kw aej tysr re ujdr lkgc jv",
	//					"so it is okay if you want to just give up");
		for( int cas = 1; cas <= T; ++cas) {
			gets(s);
			int len = strlen(s);
			printf("Case #%d: ", cas);
			for( int i = 0; i < len; ++ i) {
				if(s[i] != ' ') {
					s[i] = Map[s[i] - 'a'];
				}
				putchar(s[i]);
			}
			putchar('\n');
		}
		return 0;
		M['q'] = 'z';
		M['z'] = 'q';
		for( int i = 'a'; i <= 'z'; ++ i) {
			printf("%c", M[i]);
			bool flag =false;
			for( int j = 'a'; j <='z'; ++ j) {
				if(M[j] == i) flag = true;
			}
			if(!flag) {
			//	printf("no exist %c\n", i);
			}
		}
		
		return 0;
}
