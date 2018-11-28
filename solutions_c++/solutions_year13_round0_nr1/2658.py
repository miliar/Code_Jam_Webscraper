#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void setResult(int* result,unsigned int r,unsigned int c)
{
	if (3 < r || 3 < c)
	{
		return;
	}
	result[r]++;
        result[4+c]++;
        if (r == c)
        {
            result[8]++;
        }
        else if (r+c == 3)
        {
            result[9]++;
        }
}

bool win(int* result)
{
	for (int i  = 0; i < 10; i++)
	{
		//printf(" %d", result[i]);
		if (4 == result[i])
		{
			return true;
		}
	}

	//printf("\n");
	return false;
}

int main (void)
{
	char line[2049] = {0};
	char game[4][4] = {0};
	int resultx[10] = {0};
	int resulty[10] = {0};
	bool notComplete = false;
	char *p = NULL;
	FILE* f = NULL;
	int num = 0;
	int outline = 1;
	int colum = 0;
	int row = 0;

	f = fopen("input.txt", "r");

	p = fgets(line, 2048, f);
	//get linenum
	sscanf(line, "%d", &num);

	for (int i = 0; i < num; i++)
	{

		row = 0;
		colum = 0;
		memset(&resultx, 0, sizeof(resultx));
		memset(&resulty, 0, sizeof(resulty));
		notComplete = false;

		for (int row = 0; row < 4; row++)
		{
	                p = fgets(line, 2048, f);
        	        if (NULL == p)
                	{
                        	break;
                	}
		
			for (colum = 0; colum < 4; colum++)
			{

				if (('X' == line[colum]) || ('x' == line[colum]))
				{
					game[row][colum] = 'X';
					setResult(resultx, row, colum);
				}
				else if (('O' == line[colum]) || ('o' == line[colum]))
				{
					game[row][colum] = 'O';
					setResult(resulty, row, colum);
				}
				else if (('T' == line[colum]) || ('t' == line[colum]))
				{
					game[row][colum] = 'T';
					setResult(resultx, row, colum);
					setResult(resulty, row, colum);
       				}
				else
				{
					game[row][colum] = '.';
					notComplete = true;	
				}
			}
		}

		p = fgets(line, 2048, f);
		//printf("p=%x", p);
		if (NULL == p)
		{
			break;
		}

		if (win(resultx))
		{
       			printf("Case #%d: %s\n", outline++, "X won");
		}
		else if (win(resulty))
		{
			printf("Case #%d: %s\n", outline++, "O won");
		}
		else if (notComplete)
		{
			printf("Case #%d: %s\n", outline++, "Game has not completed");
		}
		else
		{
			printf("Case #%d: %s\n", outline++, "Draw");
		}
	}
	
	fclose(f);
	return 0;
}
