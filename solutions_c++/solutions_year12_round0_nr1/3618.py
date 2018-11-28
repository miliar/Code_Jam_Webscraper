#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main() {
	//yhesocvxduiglbkrtnwjpfma
	const char *s1 = "qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	const char *s2 = "zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	char conv[256] = {0};
	int len = strlen(s1);
	
	for (int i = 0; i < len; i++)
		conv[s1[i]] = s2[i];
	
	//for (char ch = 'a'; ch <= 'z'; ch++) {
		//putchar(conv[ch]);
		//putchar(' ');
	//}
	
	int n;
	scanf("%d", &n);
	char s[10000];
	gets(s);
	for (int t = 0; t < n; t++) {
	
		printf("Case #%d: ", t+1);
		
		
		gets(s);
		int len = strlen(s);
		for (int i = 0; i < len; i++)
			putchar(s[i] >= 'a' && s[i] <= 'z' ? conv[s[i]] : s[i]);
		putchar(10);
		
	}
}

