#include <stdio.h>
#include <string.h>

char c[100][4], d[100][3];
int cp, dp;

char stack[1000];
int p, sp;

int main ()
{
	int t, ct = 0;

	for (scanf ("%d", &t); t > 0; t --)
	{
		scanf ("%d", &cp);
		for (int i = 0; i < cp; i ++)
			scanf ("%s", c[i]);

		scanf ("%d", &dp);
		for (int i = 0; i < dp; i ++)
			scanf ("%s", d[i]);

		scanf ("%d", &p);
		sp = 0;
		for (int i = 0; i < p; i ++)
		{
			char ch;

			do scanf("%c", &ch);
				while (ch <= ' ');

			stack[sp ++] = ch;
			for (int i = 0; i < cp; i ++)
				if (sp >= 2 && (
					stack[sp - 1] == c[i][0] && stack[sp - 2] == c[i][1]
					||
					stack[sp - 2] == c[i][0] && stack[sp - 1] == c[i][1]
					))
				{
					sp -= 2;
					stack[sp ++] = c[i][2];
				}

			stack[sp] = 0;
			for (int i = 0; i < dp; i ++)
				if (strchr(stack, d[i][0]) && strchr(stack, d[i][1]))
				{
					sp = 0;
					break;
				}
		}		

		printf ("Case #%d: [", ++ ct);

		for (int i = 0; i < sp; i ++)
		{
			printf ("%c", stack[i]);
			if (i + 1 < sp)
				printf (", ");
		}
		printf ("]\n");
	}
}
