#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	int num;
	char res[35][200];
	int j = 0, k = 0;
	char ch;
	scanf("%d", &num);
	while(num < 0 || num > 31)
	{
		printf("Enter number again\n");
		scanf("%d", &num);
	}
	
	for(int i = 0; i <num; i++)
	{
		fgets(res[i], 200, stdin);
	}
	for(int i = 0; i< num; i++)
	{
		for(j = 0; res[i][j] != '\0' ; j++)
		{
			if(res[i][j] == 'a')
				res[i][j] = 'y';
			else if(res[i][j] == 'b')
				res[i][j] = 'h';
			else if(res[i][j] == 'c')
				res[i][j] = 'e';
			else if(res[i][j] == 'd')
				res[i][j] = 's';
			else if(res[i][j] == 'e')
				res[i][j] = 'o';
			else if(res[i][j] == 'f')
				res[i][j] = 'c';
			else if(res[i][j] == 'g')
				res[i][j] = 'v';
			else if(res[i][j] == 'h')
				res[i][j] = 'x';
			else if(res[i][j] == 'i')
				res[i][j] = 'd';
			else if(res[i][j] == 'j')
				res[i][j] = 'u';
			else if(res[i][j] == 'k')
				res[i][j] = 'i';
			else if(res[i][j] == 'l')
				res[i][j] = 'g';
			else if(res[i][j] == 'm')
				res[i][j] = 'l';
			else if(res[i][j] == 'n')
				res[i][j] = 'b';
			else if(res[i][j] == 'o')
				res[i][j] = 'k';
			else if(res[i][j] == 'p')
				res[i][j] = 'r';
			else if(res[i][j] == 'q')
				res[i][j] = 'z';
			else if(res[i][j] == 'r')
				res[i][j] = 't';
			else if(res[i][j] == 's')
				res[i][j] = 'n';
			else if(res[i][j] == 't')
				res[i][j] = 'w';
			else if(res[i][j] == 'u')
				res[i][j] = 'j';
			else if(res[i][j] == 'v')
				res[i][j] = 'p';
			else if(res[i][j] == 'w')
				res[i][j] = 'f';
			else if(res[i][j] == 'x')
				res[i][j] = 'm';
			else if(res[i][j] == 'y')
				res[i][j] = 'a';
			else if(res[i][j] == 'z')
				res[i][j] = 'q';
		}
	}

	for(int i = 0; i < num; i++)
	{
		printf("Case #%d: %s\n", i,res[i]);
	}
}
