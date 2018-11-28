#include <stdio.h>
#include <string.h>

#define LINE_SIZE	501
char line[LINE_SIZE + 1];
char welcome[] = "welcome to code jam";
//char welcome[] = "ab c";

int doIt()
{
	gets(line);
	int wLen = strlen(welcome);
	char *wp = welcome + wLen - 1;
	int inSize = strlen(line);
	
	int oldBuf[LINE_SIZE];
	int newBuf[LINE_SIZE];
	int i;
	for (i = 0; i < LINE_SIZE; i++)
	{
		oldBuf[i] = 0;
		newBuf[i] = 0;
	}
	int cur = 0;
	char lastChar = welcome[wLen - 1];
	for (i = inSize - 1; i >= 0; i--)
	{
		if (line[i] == lastChar)
		{
			cur++;
		}
		oldBuf[i] = cur;
	}
	for (wp = welcome + wLen - 2; wp >= welcome; wp--)
	{
		cur = 0;
		for (i = inSize - 1; i >= 0; i--)
		{
			if (line[i] == *wp)
			{
				if (i < inSize - 1)
				{
					cur = cur + oldBuf[i + 1];
					cur %= 1000;
				}
			}
			newBuf[i] = cur;
		}
		for (i = 0; i < inSize; i++)
		{
			oldBuf[i] = newBuf[i];
		}
	}
	return cur;
}

int main(int argc, char* argv[])
{
	gets(line);
	int numTests;
	sscanf(line, "%d", &numTests);
	for (int i = 0; i < numTests; i++)
	{
		printf("Case #%d: %04d\n", i + 1, doIt());
	}
	return 0;
}

