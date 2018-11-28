#include <stdio.h>
#include <string.h>
#include <math.h>

#define BUFSIZE 2000

int num_cases = 0;

int
main(int argc, char **argv)
{
	char buf[BUFSIZE+1];
	FILE *fp;
	char *cptr;

	static char xlate[26] = {
		'y',
		'h',
		'e',
		's',
		'o',
		'c',
		'v',
		'x',
		'd',
		'u',
		'i',
		'g',
		'l',
		'b',
		'k',
		'r',
		'z',
		't',
		'n',
		'w',
		'j',
		'p',
		'f',
		'm',
		'a',
		'q',
	};
	int i, ret;
	int num_cases;

	if (argc == 1)
		fp = stdin;
	else
	{
		fp = fopen(*++argv, "r");
		if (!fp)
		{
			printf("Can't open file: \"%s\"\n", *argv);
			return 1;
		}
	}

	fgets(buf, BUFSIZE, fp);
	sscanf(buf, "%d", &num_cases);

	if (num_cases <= 0)
	{
		printf("Invalid # of test cases\n");
		return 1;
	}

	// dbg_printf("cases: %d\n", num_cases);
	for (i=0; i < num_cases; i++)
	{
		fgets(buf, BUFSIZE, fp);

		printf("Case #%d: ", i+1);

		for (cptr = buf; *cptr; cptr++)
		{
			if (*cptr == ' ')
				printf(" ");
			else if (*cptr < 'a' || *cptr > 'z')
				continue;
			else
				printf("%c", xlate[*cptr-'a']);
		}

		printf("\n");
	}
}
