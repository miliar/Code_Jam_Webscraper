// 1.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <stdio.h>


#define MAX_NUM_WORDS 5001
#define MAX_LENGTH	16
char dict[MAX_NUM_WORDS][MAX_LENGTH];
int numWords;

#define LINE_SIZE (((26 + 2) * MAX_LENGTH) + 1)
char line[LINE_SIZE + 1];


int match(char *word, char *pattern)
{
	char *p = pattern;
	char *s = word;

	while (*s)
	{
		if (*p == '(')
		{
			p++;
			while (*p != ')')
			{
				if (*p == *s)
				{
					break;
				}
				p++;
			}
			if (*p == ')')
			{
				return 0;
			}
			while (*p != ')')
			{
				p++;
			}
			p++;
		}
		else
		{
			if (*p != *s)
			{
				return 0;
			}
			p++;
		}
		s++;
	}
	return 1;
}

int doIt(char *pattern)
{
	int count = 0;
	int i;
	for (i = 0; i < numWords; i++)
	{
		if (match(dict[i], pattern))
		{
			count++;
		}
	}
	return count;
}

int main(int argc, char* argv[])
{
	int length, numTests;
	gets(line);
	sscanf(line, "%d %d %d", &length, &numWords, &numTests);
	int i;
	for (i = 0; i < numWords; i++)
	{
		gets(dict[i]);
	}
	for (i = 0; i < numTests; i++)
	{
		gets(line);
		int result = doIt(line);
		printf("Case #%d: %d\n", i + 1, result);
	}

	return 0;
}

