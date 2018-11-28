#include <cstdio>
#include <map>
#include <cstring>

using namespace std;
char *a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char *b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char m[255];
void init(){
     int len = strlen(a);
     for(int i = 0; i < len; i ++){
             m[a[i]] = b[i];
     }
}

int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	init();
	m['z'] = 'q';
	m['q'] = 'z';
	int n;
	char str[111];
	scanf("%d", &n);
	gets(str);
	for(int i = 1; i <= n; i ++){
		gets(str);
		printf("Case #%d: ", i);
		int len = strlen(str);
		for(int j = 0; j < len; j++){
			printf("%c", m[str[j]]);
		}
		putchar(10);
	}
    return 0;
}

