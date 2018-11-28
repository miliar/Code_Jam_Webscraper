#include <cstdio>
#include <cstring>

char t[] = "yhesocvxduiglbkrztnwjpfmaq";
char str[1000000];

int main()
{
	int z;
	scanf("%d", &z);
	getchar();
	for(int i = 1; i <= z; i++)
	{
		int n = 0;
		while((str[n] = getchar()) != '\n')
			n++;
		printf("Case #%d: ",i);
		for(int j = 0; j < n; j++)
			str[j] != ' ' ? printf("%c",t[str[j]-'a']) : printf(" ");
		printf("\n");
	}
}
