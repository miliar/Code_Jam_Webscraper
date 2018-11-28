/*
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define MAXDIC 60

char dic[MAXDIC][20] = {
	"the", "our", "is", "it", "so", "if", "you", "to", "are", "up",
	"our", "language", "impossible", "understand", "there", "twenty", "factorial", "possibilities", "okay", " want",
	"just", "give", "zoo", "google", "end", "test", "problem", "we", "have", "come",
	"with", "best", "possible", "language", "at", "text", "message", "and", "each", "letter"
	"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
	"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
};

char * downlang(char lang[50])
{
	int i;

	for(i = 0; i < 26; i++)
	{
		if(lang[i] >=65 && lang[i] <= 90)
			lang[i] += 32;
	}
	return lang;
}

int main(void)
{
	int i, j, t, count;
	char *token, input[5000], lang[100][50], transTable[26];

	scanf("%d ", &t);
	for(i = 0; i < t; i++)
	{
		count = 0;
		fgets(input, 5000, stdin);

		// token whitespace to language
		token = strtok(input, " ");
		strcpy(lang[0], token);
		for(j = 1; token = strtok(NULL, " "); j++)
		{
			strcpy(lang[j], token);
			count++;
		}

		// find same string lengh
		for(j = 0; j < MAXDIC; j++)
			for(k = 0; k < count; k++)
				if(strlen(dic[j]) == strlen(lang[k])
				{
					for(l = 0; l < strlen(lang[k]); l++)
					{
						transTable[lang[k]
					}
				}
	}
	return 0;
}*/

#include<stdio.h>
#include<string.h>

char match[27] = "ynficwlbkuomxsevzpdrjgthaq";

char trans(char ch)
{
	int i;

	for(i = 0; i < strlen(match); i++)
		if(match[i] == ch)
			return i+97;
}

int main(void)
{
	int i, j, t;
	char input[5000], output[5000];

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d ", &t);
	for(i = 0; i < t; i++)
	{
		fgets(input, 5000, stdin);

		for(j = 0; input[j] != NULL; j++)
		{
			if(input[j] == ' ')
				output[j] = ' ';
			else
				output[j] = trans(input[j]);
		}
		output[j-1] = 0;

		printf("Case #%d: %s\n", i+1, output);
	}

	return 0;
}