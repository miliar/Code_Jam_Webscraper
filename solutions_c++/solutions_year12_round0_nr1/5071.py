#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

char s[50] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't',
	 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	char g[200];
	scanf("%d", &n);
	getchar();
	for (int i = 0; i < n; i++)
	{
		gets(g);
		int l = strlen(g);
		printf("Case #%d: ", i+1);
		for (int j = 0; j < l; j++)
			if (g[j] == ' ')
				printf(" ");
			else
				printf("%c", s[g[j] - 'a']);
		printf("\n");
	}
	return 0;
}