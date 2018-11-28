#include <stdio.h>
#include <string.h>
char A[50];
int main() {
    freopen("A-small-attempt0.in", "r",stdin);
    freopen("output.txt", "w",stdout);
	A['a'-'a'] = 'y';
	A['b'-'a'] = 'h';
	A['c'-'a'] = 'e';
	A['d'-'a'] = 's';
	A['e'-'a'] = 'o';
	A['f'-'a'] = 'c';
	A['g'-'a'] = 'v';
	A['h'-'a'] = 'x';
	A['i'-'a'] = 'd';
	A['j'-'a'] = 'u';
	A['k'-'a'] = 'i';
	A['l'-'a'] = 'g';
	A['m'-'a'] = 'l';
	A['n'-'a'] = 'b';
	A['o'-'a'] = 'k';
	A['p'-'a'] = 'r';
	
	A['q'-'a'] = 'z';
	
	A['r'-'a'] = 't';
	A['s'-'a'] = 'n';
	A['t'-'a'] = 'w';
	A['u'-'a'] = 'j';
	A['v'-'a'] = 'p'; 
	A['w'-'a'] = 'f'; 
	A['x'-'a'] = 'm'; 
	A['y'-'a'] = 'a'; 
	
	A['z'-'a'] = 'q'; 
	
	int N;
	scanf("%d\n", &N);
	int i, j, n;
	char G[100];
	for(i=0;i<N;i++) {
 		gets (G);
		n = strlen(G);
		printf("Case #%d: ", i+1);
		for(j=0;j<n;j++) {
			if(G[j] == ' ') printf(" ");
			else printf("%c", A[G[j]-'a']);
		}
		printf("\n");
	}
	return 0;
}
