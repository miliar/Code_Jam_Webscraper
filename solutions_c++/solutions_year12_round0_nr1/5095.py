#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	char *line;
	int noOfInput;
	//char *input;
	char input[10];

	//scanf("%d", &noOfInput);
	line = (char *) malloc (sizeof(char) * 1024);
	//scanf("%s", line);
	gets(input);
	noOfInput = atoi(input);

	for(int i=0; i<noOfInput; i++)
	{
		line = gets(line);
		int length = strlen(line);

		for(int j=0; j<length; j++)
		{
			int ch = line[j];
			if(ch == ' ')
				continue;
			
			line[j] = map[ch-'a'];
		}
		printf("Case #%d: ", i+1);
		puts(line);
	}
	return 0;
}