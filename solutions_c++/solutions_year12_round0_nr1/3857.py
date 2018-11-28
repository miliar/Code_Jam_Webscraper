#include <stdio.h>

char s[110];
	      //abcdefghijklmnopqrstuvwxyz
char map[30] = "yhesocvxduiglbkrztnwjpfmaq";
	//"ynficwlbkuomxsevzpdrjgthaq";
		
int n;

int main() {
	scanf("%d", &n);

	for (int i=0; i<n; i++) {
		scanf(" %[^\n]", s);
		printf("Case #%d: ", i+1);
		for (int j=0; s[j]!='\0'; j++)
			if (s[j]==' ') printf(" ");
			else printf("%c", map[s[j]-'a']);
		printf("\n");
	}
	
	return 0;
}
