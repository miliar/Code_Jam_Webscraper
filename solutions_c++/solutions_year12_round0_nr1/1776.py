//Jakub "Cubix651" Cisło
//Zadanie: A - Google Code Jam
#include <cstdio>

char tab['z'-'a'+1] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char c;
int i = 1, n;

int main()
{
	scanf("%d\n", &n);
	printf("Case #%d: ", i);
	while(scanf("%c", &c) != EOF)
	{
		if(c == ' ') printf(" ");
		else if(c == '\n'){ if(i < n) printf("\nCase #%d: ", ++i);}
		else printf("%c", tab[c-'a']);
	}
	printf("\n");
	return 0;
}
