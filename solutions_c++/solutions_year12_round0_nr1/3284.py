#include <cstdio>
#include <cstring>

int main ()
{
	freopen ("outa.txt","w",stdout);
	freopen ("A-small-attempt1.in","r",stdin);

	char input [101], arr []	=	{'y', 'h', 'e', 's', 'o', 'c',
									 'v', 'x', 'd', 'u', 'i', 'g',
									 'l', 'b', 'k', 'r', 'z', 't',
									 'n', 'w', 'j', 'p', 'f', 'm',
									 'a', 'q'};

	int tc, len, i, j;

	scanf ("%d\t", &tc);

	for (j = 1; j <= tc; j++)	{

		gets (input);
		printf ("Case #%d: ", j);
		len	=	strlen (input);

		for (i = 0; i < len; i++)	{

			if (input [i] != ' ')
				printf ("%c", arr [input[i] - 97]);
			else
				printf (" ");

		}

		printf ("\n");
	}

	return 0;
}