#include <cstdio>
char map[] = "yhesocvxduiglbkrztnwjpfmaq";
void print(char* str)
{
	for (int i = 0; str[i]; i++)
		if (str[i] != ' ')
			printf("%c", map[str[i] - 'a']);
		else
			printf("%c", str[i]);
}
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	char g[101];
	scanf("%d%*c", &t);
	for (int i = 1; i <= t; i++)
	{
		gets(g);
		printf("Case #%d: ", i);
		print(g);
		printf("\n");
	}
	return 0;
}