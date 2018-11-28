#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

char win;
bool incomplete = false;
bool done = false;

int conv(char c)
{

	switch (c)
	{
	case 'X':
		return 2;
		break;
	case 'O':
		return 3;
		break;
	case 'T':
		return 6;
		break;
	case '.':
		return 0;
		break;
	default:
		exit(-257);
		break;
	}
}

bool check(char c1, char c2, char c3, char c4)
{
	int result = conv(c1) * conv(c2) * conv(c3) * conv(c4);

	if (result == 0)
	{
		incomplete = true;
		return false;
	}

	if (result % 16 == 0)
	{
		win = 'X';
		return true;
	}

	if (result % 81 == 0)
	{
		win = 'O';
		return true;
	}

	return false;
}

int main()
{
	char cells[4][4];
	int t;
	scanf("%d", &t);

	for (int n = 0; n < t; n++)
	{

		incomplete = false;
		done = false;
		win = '0';

		//for (int i = 0; i < 4; i++)
		//{
			for (int r = 0; r < 4; r++)
			{
				scanf("%s", cells[r]);
				//cin.getline(cells[r], 4);
			}
		//}


		/*for (int r = 0; r < 4; r++)
		{
			for (int c = 0; c < 4; c++)
            {
                printf("%c", cells[r][c]);
            }
            printf("\n");
		}*/

		//diagonals

		if (check(cells[0][0], cells[1][1], cells[2][2], cells[3][3]))
			{
				printf("Case #%d: %c won\n", n+1, win);
				continue;
			}
		if (check(cells[0][3], cells[1][2], cells[2][1], cells[3][0]))
			{
				printf("Case #%d: %c won\n", n+1, win);
				continue;
			}

		// rows and columns
		for (int i = 0; i < 4; i++)
 	   	{
 	       	if (check(cells[i][0], cells[i][1], cells[i][2], cells[i][3]))
			{
				printf("Case #%d: %c won\n", n+1, win);
				done = true;
				break;
			}

			if (check(cells[0][i], cells[1][i], cells[2][i], cells[3][i]))
			{
				printf("Case #%d: %c won\n", n+1, win);
				done = true;
				break;
			}
    	}

    	if (!done)
		{
			if (!incomplete)
				printf("Case #%d: Draw\n", n+1);
			else
				printf("Case #%d: Game has not completed\n", n+1);
		}
	}

	printf("\n");

    return 0;
}
