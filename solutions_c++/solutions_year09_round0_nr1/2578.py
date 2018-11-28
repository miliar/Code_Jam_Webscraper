// code_a.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

int l = 0;
int d = 0;
int n = 0;

#define MAX_PATTERN 16
#define MAX_LINE	400

int IsMatch(char * message, char * pattern)
{
	int patternPos = 0;
	int ret = 1;

	for(int i = 0 ; i < l ; i++)
	{
		if (pattern[patternPos] != '(')
		{
			if (message[i] != pattern[patternPos])
			{
				ret = 0;
				break;
			}
			patternPos++;
		}
		else
		{
			int bOK = 0;
			while(pattern[patternPos] != ')')
			{
				if (pattern[patternPos] == message[i])
				{
					bOK = 1;
				}
				patternPos++;
			}

			if (bOK == 0)
			{
				ret = 0;
				break;
			}

			patternPos++;
		}
	}

	return ret;
}


int main(int argc, char* argv[])
{
	FILE *fp = fopen(argv[1], "rt");
	if (fp == NULL)
		return 0;

	char buf[MAX_LINE];
	fgets(buf, MAX_LINE, fp);
	char *token = strtok(buf, " ");
	l = atoi(token);
	token = strtok(NULL, " ");
	d = atoi(token);
	token = strtok(NULL, " ");
	n = atoi(token);

	// Messages...
	//
	char **messages = new char*[d];
	for(int m = 0 ;m < d; m++)
	{
		messages[m] = new char[l+1];
		memset(messages[m], '\0', l+1);
	}

	for(int i = 0 ; i < d ; i++)
	{
		fgets(buf, MAX_LINE, fp);
		strcpy(messages[i], buf);
		messages[i][l] = '\0';
	}

	char **cases = new char*[n];
	for(int c = 0 ;c < n; c++)
	{
		cases[c] = new char[MAX_LINE];
		memset(cases[c], '\0', MAX_LINE);
	}

	for (int j = 0 ; j < n ; j++)
	{
		fgets(buf, MAX_LINE, fp);
		strcpy(cases[j], buf);
		cases[j][strlen(cases[j])-1] = '\0';
	}

	int * caseResult = new int[n];
	for( c = 0 ;c < n; c++)
	{
		caseResult[c] = 0;
	}

	for(m = 0 ;m < d; m++)
	{

		for( int c = 0 ;c < n; c++)
		{
			if (IsMatch(messages[m], cases[c]))
			{
				caseResult[c]++;
			}
		}
	}


	for( c = 0 ;c < n; c++)
	{
		printf("Case #%d: %d\n", (c+1), caseResult[c]);
	}


	fclose(fp);
	
	return 0;
}

