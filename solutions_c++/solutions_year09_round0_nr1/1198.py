#include <stdio.h>
#include <ctype.h>


int L, D, N;
char string[5001][20];
char map[5001];

void InitMap()
{
	for(int i = 0; i < D; i++)
	{
		map[i] = 0;
	}
}

int getMap()
{
	int result = 0;
	for(int i = 0; i < D; i++)
	{
		if(map[i] == L) result++;
	}

	return result;
}

void IncreaseOne(int pos, char val)
{
	for(int i = 0; i < D; i++)
	{
		if(string[i][pos] == val) map[i]++;
	}
}

int main()
{
	scanf("%d%d%d",&L,&D,&N);
	for(int i = 0; i < D; i++)
	{
		scanf("%s", string[i]);
	}

	char input;
	int option = 0; // n : ÀÚ¸®, 
	int order = 0;
	int caseNumber = 1;
	for(int i = 0; i < N; i++)
	{
		InitMap();
		order = 0;
		for(;;)
		{
			scanf("%c", &input);
			if(input == ' ' || input == '\n' || input == '\t') continue;
			if(isalpha(input))
			{
				IncreaseOne(order, input);
				if(option == 0) order++;
			}
			else if(input == '(')
			{
				option = 1;
			}
			else if(input == ')')
			{
				option = 0;
				order++;
			}
			if(order == L) break;
		}
		printf("Case #%d: %d\n", caseNumber, getMap());
		caseNumber++;
	}

	return 0;
}

