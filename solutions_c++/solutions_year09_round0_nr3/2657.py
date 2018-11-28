#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int countInStr(int startPos, const char *inStr, const char *searchStr)
{
	int i = startPos;
	int inStrLen= strlen(inStr);

	int numFound = 0;
	while(i < inStrLen)
	{
		if(searchStr[0] == inStr[i])
		{
			if(strlen(searchStr) == 1)
			{
				numFound += 1;
			}
			else
			{
				numFound += countInStr(i + 1, inStr, &(searchStr[1]));
			}
		}
		
		i++;
	}
	
	return numFound;
}

static const char *sstr = "welcome to code jam";
static int intBuf[500];
static int newBuf[500];

#define max(a, b) ((a > b)? a : b)

int main()
{
	int nlines = 0;
	char buf[512];
	FILE *in = fopen("C-small.in", "r");
	fscanf(in, "%d\n", &nlines);

	for(int i = 0; i < nlines; i++)
	{
		fgets(buf, 512, in);
		
		int len = strlen(buf);
		buf[--len] = '\0';
		
		memset(intBuf, 0, sizeof(intBuf));
		memset(newBuf, 0, sizeof(newBuf));
		
		for(int k = strlen(sstr) - 1; k >= 0; k--)
		{
			for(int j = len - 1; j >= 0; j--)
			{
				if(buf[j] == sstr[k])
				{
					if(k == strlen(sstr) - 1)
						newBuf[j] = newBuf[j + 1] + 1;
					else
						newBuf[j] = intBuf[j + 1] + newBuf[j + 1];
						
				} else {
					newBuf[j] = newBuf[j + 1];
				}
			}
			
			memcpy(intBuf, newBuf, sizeof(newBuf));
		}
		
		printf("Case #%d: %04d\n", i + 1, intBuf[0]);
	}

	fclose(in);
}
