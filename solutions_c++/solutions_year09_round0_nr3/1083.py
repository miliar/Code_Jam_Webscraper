#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char line [1024];

char welcome [] = "welcome to code jam"; // length = 19
int dp [20][510];

int main()
{
	gets (line);
	int kase = atoi (line);

	const int welLen = 19;
	int serial = 0, len;

	while (kase--)
	{
		//	start a test case

		gets (line);
		len = strlen (line);

		for (int i=0; i<len; ++i)
			dp [0][i] = 1;

		for (int w=1, i; w<=welLen; ++w) {
			for (i=1; i<=len; ++i)
				if (line [i-1] == welcome [w-1])
					dp [w][i] = (dp [w][i-1] + dp [w-1][i-1]) % 10000;
				else
					dp [w][i] = dp [w][i-1];
		}

		printf ("Case #%d: %04d\n", ++serial, dp [welLen][len] % 10000);

		//	end a test case
	}

	return 0;
}