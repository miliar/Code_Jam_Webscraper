#include <cstdio>

const int TABLE_SIZE=4;

inline char readChar()
{
	char c;
	do { c=getchar(); } while(c=='\n');
	return c;
}

#ifdef DEBUG
void dumpMap(char map[TABLE_SIZE][TABLE_SIZE])
{
	for(int row=0; row < TABLE_SIZE; row++)
	{
		for(int col=0; col < TABLE_SIZE; col++)
			printf("%c", map[row][col]);
		printf("\n");
	}
}
#endif

char map[TABLE_SIZE][TABLE_SIZE];

bool checkCase(const int row, const int col, char& winner)
{
	if(map[row][col] == '.')
		return false;
	if(map[row][col] == 'T')
		return true;
	if(winner == 'T') // && map[row][col] != T, useless to check
		winner=map[row][col];
	if(map[row][col] != winner)
		return false;
	return true;
}

void processTest(int test)
{
	// check cols
	for(int col=0; col < TABLE_SIZE; col++)
	{
		char winner=map[0][col];
		if(winner == '.')
			continue;
		bool won=true;
		for(int row=1; row < TABLE_SIZE; row++)
		{
			if(!checkCase(row,col,winner))
			{
				won=false;
				break;
			}
		}
		if(won)
		{
			printf("Case #%d: %c won\n", test+1, winner);
			return;
		}
	}

	//check rows
	for(int row=0; row < TABLE_SIZE; row++)
	{
		char winner=map[row][0];
		if(winner == '.')
			continue;
		bool won=true;
		for(int col=1; col < TABLE_SIZE; col++)
		{
			if(!checkCase(row,col,winner))
			{
				won=false;
				break;
			}
		}
		if(won)
		{
			printf("Case #%d: %c won\n", test+1, winner);
			return;
		}
	}

	// check diag \
	//
	
	char winner = map[0][0];
	if(winner!='.')
	{
		bool won=true;
		int row=1,col=1;
		while(row < TABLE_SIZE)
		{
			if(!checkCase(row,col,winner))
			{
				won=false;
				break;
			}

			row++;
			col++;
		}
		if(won)
		{
			printf("Case #%d: %c won\n", test+1, winner);
			return;
		}
	}

	// check diag / 

	winner = map[TABLE_SIZE-1][0];
	if(winner!='.')
	{
		bool won=true;
		int row=TABLE_SIZE-2,col=1;
		while(col < TABLE_SIZE)
		{
			if(!checkCase(row,col,winner))
			{
				won=false;
				break;
			}

			row--;
			col++;
		}
		if(won)
		{
			printf("Case #%d: %c won\n", test+1, winner);
			return;
		}
	}

	for(int row=0; row < TABLE_SIZE; row++)
	{
		for(int col=0; col < TABLE_SIZE; col++)
		{
			if(map[row][col] == '.')
			{
				printf("Case #%d: Game has not completed\n", test+1);
				return;
			}
		}
	}

	printf("Case #%d: Draw\n", test+1);
}

int main(void)
{
	int nbTests;
	scanf("%d", &nbTests);

	for(int test=0; test < nbTests; test++)
	{
		for(int row=0; row < TABLE_SIZE; row++)
			for(int col=0; col < TABLE_SIZE; col++)
				map[row][col] = readChar();

#ifdef DEBUG
		dumpMap(map);
#endif

		processTest(test);
	}
}

