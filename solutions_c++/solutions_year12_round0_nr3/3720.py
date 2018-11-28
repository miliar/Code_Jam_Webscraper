#include <stdio.h>
#include <string.h>
#include <math.h>

#define BUFSIZE 2000

int num_cases = 0;

void
print_digits(char *cptr, int len)
{
	int i;
	for (i = len-1; i >= 0; i--)
	{
		// dbg_printf("%c", cptr[i]+'0');
	}
}

inline int
load_digits(char *digits, int number)
{
	int ret = 0;
	while (number)
	{
		digits[ret++] = number % 10;
		number /= 10;
	}

	int i;

	for (i=0; i < ret; i++)
	{
		digits[ret+i] = digits[i];
	}

	return ret;
}

inline int
cmp_digits(char *A, char *B, int len)
{
	int i;
	for (i = len-1; i >= 0; i--)
	{
		if (A[i] < B[i])
			return -1;

		if (A[i] > B[i])
			return 1;
	}

	return 0;
}

inline int
count(int A, int B)
{
	int ret=0;
	int c, i, j;
	char digitsA[20], digitsB[20], digitsC[20];
	int lenA, lenB, lenC;

	lenA = load_digits(digitsA, A);
	lenB = load_digits(digitsB, B);

	for (c=A; c < B; c++)
	{
		lenC = load_digits(digitsC, c);

		for (i=1; i < lenC; i++)
		{
			if (cmp_digits(&digitsC[i], digitsC, lenC) <= 0)
				continue;

			if (cmp_digits(&digitsC[i], digitsB, lenC) > 0)
				continue;

			// dbg_printf("found [%d]: ", c);
			print_digits(&digitsC[i], lenC);
			// dbg_printf("\n");


			for (j=i-1; j > 0; j--)
			{
				if (!cmp_digits(&digitsC[i], &digitsC[j], lenC))
				{
					// dbg_printf("rejected [%d]: ", c);
					print_digits(&digitsC[i], lenC);
					// dbg_printf("\n");

					break;
				}
			}

			if (!j)
				ret++;
		}

	}
	return ret;
}

int
main(int argc, char **argv)
{
	char buf[BUFSIZE+1];
	FILE *fp;

	int i, ret;
	int num_cases;
	int A, B;

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

		ret = sscanf(buf, "%d %d", &A, &B);
		if (ret != 2)
		{
			printf("Error in input file on line #%d\n", i+2);
			return 1;
		}

		// dbg_printf("case #%d: A=%d B=%d\n", i+1, A, B);
		printf("Case #%d: %d\n", i+1, count(A, B));
	}
}
