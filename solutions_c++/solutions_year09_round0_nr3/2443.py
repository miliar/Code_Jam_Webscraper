
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

#define MAX_LINE 600
char * szWelcome = "acdejlmotw"; // welcome to code jam
char * szWelcomeToCodeJam = "welcome to code jam";

int indexWelcome[26];
char newMessage[MAX_LINE];

#define WELCOME_LENGTH 19

int Compare(int posSource, int targetPos, int size)
{
	int count = 0;

	if (posSource == WELCOME_LENGTH)
	{
		return 1;
	}

	for (int j = targetPos ; j < size ; j++)
	{
		if (szWelcomeToCodeJam[posSource] == newMessage[j])
		{
			count += Compare(posSource+1, j+1, size);
		}
	}
	
	return count;
	
}

int Count(char * message, int size)
{
	int count = 0;
	int pos = 0;
	memset(newMessage, '\0', MAX_LINE);

	for (int i = 0 ;i < size ;i++)
	{
		if (indexWelcome[message[i]-'a'] == 1 || message[i] == ' ')
		{
			newMessage[pos] = message[i];
			pos++;
		}
	}

	int newSize = pos;

	int cases = 0;
	pos = 0;
	int multipleCount = 0;

	for (int j = 0 ; j < newSize ; j++)
	{
		if (szWelcomeToCodeJam[pos] == newMessage[j])
		{
			cases += Compare(pos+1, j+1, newSize);
		}
	}

	return cases;
}


int main(int argc, char* argv[])
{
	FILE *fp = fopen(argv[1], "rt");
	if (fp == NULL)
		return 0;
	
	char buf[MAX_LINE];
	fgets(buf, MAX_LINE, fp);
	buf[strlen(buf)-1] = '\0';
	int n = atoi(buf);

	for(int i = 0 ;i < 26; i++)
	{
		indexWelcome[i] = 0;
	}
	indexWelcome[szWelcome[0]-'a'] = 1;
	indexWelcome[szWelcome[1]-'a'] = 1;
	indexWelcome[szWelcome[2]-'a'] = 1;
	indexWelcome[szWelcome[3]-'a'] = 1;
	indexWelcome[szWelcome[4]-'a'] = 1;
	indexWelcome[szWelcome[5]-'a'] = 1;
	indexWelcome[szWelcome[6]-'a'] = 1;
	indexWelcome[szWelcome[7]-'a'] = 1;
	indexWelcome[szWelcome[8]-'a'] = 1;
	indexWelcome[szWelcome[9]-'a'] = 1;


	for(i = 0 ;i < n; i++)
	{
		fgets(buf, MAX_LINE, fp);
		printf("Case #%d: %04d\n", i, Count(buf, strlen(buf)) % 10000);
	}

	fclose(fp);
	
	return 0;
}