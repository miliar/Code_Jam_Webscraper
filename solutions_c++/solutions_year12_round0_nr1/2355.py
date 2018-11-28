#include <iostream>
using namespace std;

char buf[256];
char m[256];
char rm[256];

void solve(char *a) {
	for (int i = 0; a[i]; i++) {
		a[i] = m[a[i]];
	}
}

void process(char *a, char *b) {
	for (int i = 0; a[i]; i++) {
		m[a[i]] = b[i];
		rm[b[i]] = a[i];
	}
}

int main() {
	process("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	process("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	process("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
//	process("a zoo", "y qee");
	
 

/* 
	for (int i = 'a'; i <= 'z'; i++) {
		if (m[i] == 0) 
			printf("%c", i);
	}
	
	for (int i = 'a'; i <= 'z'; i++) {
		if (rm[i] == 0) 
			printf("%c", i);
	}

 */



	m['q'] = 'z';
	m['z'] = 'q'; //this is right
	
	int n;
	scanf("%d\n", &n);
	
	for (int i = 0; i < n; i++) {
		gets(buf);
		solve(buf);
		printf("Case #%d: %s\n", i+1, buf);
	}
	
	return 0;
}