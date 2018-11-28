// Google Code Jam 2012
// Qualification Round
// Program A. Speaking in Tongues
#include <cstdio>
#include <cstring>

char to[] = { 'y', 'h', 'e', 's', 'o',
              'c', 'v', 'x', 'd', 'u',
              'i', 'g', 'l', 'b', 'k',
              'r', 'z', 't', 'n', 'w',
              'j', 'p', 'f', 'm', 'a',
              'q' };

int main()
{
	int T;
	scanf("%d", &T);
	getchar();
	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		char c = getchar();
		while (c != '\n' && c != '\r')
		{
			if (c == ' ')
				printf(" ");
			else
				printf("%c", to[c-'a']);
			c = getchar();
		}
		printf("\n");
	}
	return 0;
}
