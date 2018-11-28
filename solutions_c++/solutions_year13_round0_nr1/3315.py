#include <stdio.h>

int main()
{
    int T, C;
    char game[4][4], blank;
	int result; //0 = unknown, 1 = x win, 2 = o win, 3 = busy, 4 = draw
	int tx, ty;//find the T
	int dotcount;

    scanf("%i\n", &T);

    for (C = 1;C <= T;C++)
    {
		result = 0;//clear result
        for (int y = 0;y < 4;y++)//read shit
        {
			for (int x = 0;x < 4;x++)
			{
                scanf("%c", &game[y][x]);
			}
			scanf("\n");
        }

		tx = -1;
		ty = -1;
        for (int y = 0;y < 4;y++)
            for (int x = 0;x < 4;x++)
                if (game[y][x] == 'T')
				{
					tx = x;
					ty = y;
				}

		//swop the T with X
		if ((tx != -1) && (ty != -1))//there is a T
			game[ty][tx] = 'X';
		
		//there can only be 10 different ways to win, here we check them
		//X
		//horisontal
		if ((result == 0)&&(game[0][0] == 'X')&&(game[0][1] == 'X')&&(game[0][2] == 'X')&&(game[0][3] == 'X')) result = 1;
		if ((result == 0)&&(game[1][0] == 'X')&&(game[1][1] == 'X')&&(game[1][2] == 'X')&&(game[1][3] == 'X')) result = 1;
		if ((result == 0)&&(game[2][0] == 'X')&&(game[2][1] == 'X')&&(game[2][2] == 'X')&&(game[2][3] == 'X')) result = 1;
		if ((result == 0)&&(game[3][0] == 'X')&&(game[3][1] == 'X')&&(game[3][2] == 'X')&&(game[3][3] == 'X')) result = 1;
		//vertical
		if ((result == 0)&&(game[0][0] == 'X')&&(game[1][0] == 'X')&&(game[2][0] == 'X')&&(game[3][0] == 'X')) result = 1;
		if ((result == 0)&&(game[0][1] == 'X')&&(game[1][1] == 'X')&&(game[2][1] == 'X')&&(game[3][1] == 'X')) result = 1;
		if ((result == 0)&&(game[0][2] == 'X')&&(game[1][2] == 'X')&&(game[2][2] == 'X')&&(game[3][2] == 'X')) result = 1;
		if ((result == 0)&&(game[0][3] == 'X')&&(game[1][3] == 'X')&&(game[2][3] == 'X')&&(game[3][3] == 'X')) result = 1;
		//diagonal
		if ((result == 0)&&(game[0][0] == 'X')&&(game[1][1] == 'X')&&(game[2][2] == 'X')&&(game[3][3] == 'X')) result = 1;
		if ((result == 0)&&(game[0][3] == 'X')&&(game[1][2] == 'X')&&(game[2][1] == 'X')&&(game[3][0] == 'X')) result = 1;
		
		if ((tx != -1) && (ty != -1))//there is a T
			game[ty][tx] = 'O';
		//O
		//horisontal
		if ((result == 0)&&(game[0][0] == 'O')&&(game[0][1] == 'O')&&(game[0][2] == 'O')&&(game[0][3] == 'O')) result = 2;
		if ((result == 0)&&(game[1][0] == 'O')&&(game[1][1] == 'O')&&(game[1][2] == 'O')&&(game[1][3] == 'O')) result = 2;
		if ((result == 0)&&(game[2][0] == 'O')&&(game[2][1] == 'O')&&(game[2][2] == 'O')&&(game[2][3] == 'O')) result = 2;
		if ((result == 0)&&(game[3][0] == 'O')&&(game[3][1] == 'O')&&(game[3][2] == 'O')&&(game[3][3] == 'O')) result = 2;
		//vertical
		if ((result == 0)&&(game[0][0] == 'O')&&(game[1][0] == 'O')&&(game[2][0] == 'O')&&(game[3][0] == 'O')) result = 2;
		if ((result == 0)&&(game[0][1] == 'O')&&(game[1][1] == 'O')&&(game[2][1] == 'O')&&(game[3][1] == 'O')) result = 2;
		if ((result == 0)&&(game[0][2] == 'O')&&(game[1][2] == 'O')&&(game[2][2] == 'O')&&(game[3][2] == 'O')) result = 2;
		if ((result == 0)&&(game[0][3] == 'O')&&(game[1][3] == 'O')&&(game[2][3] == 'O')&&(game[3][3] == 'O')) result = 2;
		//diagonal
		if ((result == 0)&&(game[0][0] == 'O')&&(game[1][1] == 'O')&&(game[2][2] == 'O')&&(game[3][3] == 'O')) result = 2;
		if ((result == 0)&&(game[0][3] == 'O')&&(game[1][2] == 'O')&&(game[2][1] == 'O')&&(game[3][0] == 'O')) result = 2;

		//ok, now we check for open spaces
		dotcount = 0;
		if (result == 0)
		{
	        for (int y = 0;y < 4;y++)//search for .
				for (int x = 0;x < 4;x++)

					if (game[y][x] == '.') dotcount++;
					
			if (dotcount != 0) //there is unused spaces = game is busy
				result = 3;
			else 
				result = 4;//this is draw
        }

        printf("Case #%i: ", C);

		if (result == 1) printf("X won\n");
		if (result == 2) printf("O won\n");
		if (result == 3) printf("Game has not completed\n");
		if (result == 4) printf("Draw\n");

    }

    return 0;
}
