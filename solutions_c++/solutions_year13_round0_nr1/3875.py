#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

void printMatrix(char matrix[4][4])
{
	int i,j;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			printf("%c", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

int main()
{
	int t = 0, T;
	char matrix[4][4];
	int i, j;
	int continue_flag = 0;
	char buff[50];
	scanf("%d", &T);
	int x_count, o_count, t_count, dot_count;
	while(t<T)
	{
		t++;
		dot_count = 0;
		continue_flag = 0;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf(" %c", &matrix[i][j]);
				if(matrix[i][j] == '.')
					dot_count++;
			}
		}
		gets(buff);
		//printMatrix(matrix);
		//fflush(stdout);

		// row win
		for(i=0; i<4; i++)
		{
			x_count = 0; o_count = 0; t_count = 0;
			for(j=0; j<4; j++)
			{
				if(matrix[i][j] == 'X')
					x_count++ ;
				if(matrix[i][j] == 'O')
					o_count++ ;
				if(matrix[i][j] == 'T')
					t_count++ ;
			}
			if((x_count+t_count) == 4)
			{
				printf("Case #%d: X won\n", t);
				continue_flag = 1;
				break;
			}

			if((o_count+t_count) == 4)
			{
				printf("Case #%d: O won\n", t);
				continue_flag = 1;
				break;
			}
		}
		if(continue_flag == 1)
			continue;

		// column win
		for(j=0; j<4; j++)
		{
			x_count = 0; o_count = 0; t_count = 0;
			for(i=0; i<4; i++)
			{
				if(matrix[i][j] == 'X')
					x_count++ ;
				if(matrix[i][j] == 'O')
					o_count++ ;
				if(matrix[i][j] == 'T')
					t_count++ ;
			}
			if((x_count+t_count) == 4)
			{
				printf("Case #%d: X won\n", t);
				continue_flag = 1;
				break;
			}

			if((o_count+t_count) == 4)
			{
				printf("Case #%d: O won\n", t);
				continue_flag = 1;
				break;
			}
		}
		if(continue_flag == 1)
			continue;


		// left diagonal win
		x_count = 0; o_count = 0; t_count = 0;
		for(i=0; i<4; i++)
		{
			if(matrix[i][i] == 'X')
				x_count++ ;
			if(matrix[i][i] == 'O')
				o_count++ ;
			if(matrix[i][i] == 'T')
				t_count++ ;
		}
		if((x_count+t_count) == 4)
		{
			printf("Case #%d: X won\n", t);
			continue;
		}

		if((o_count+t_count) == 4)
		{
			printf("Case #%d: O won\n", t);
			continue;
		}


		// right diagonal win
		x_count = 0; o_count = 0; t_count = 0;
		for(i=0; i<4; i++)
		{
			if(matrix[i][3-i] == 'X')
				x_count++ ;
			if(matrix[i][3-i] == 'O')
				o_count++ ;
			if(matrix[i][3-i] == 'T')
				t_count++ ;
		}
		if((x_count+t_count) == 4)
		{
			printf("Case #%d: X won\n", t);
			continue;
		}

		if((o_count+t_count) == 4)
		{
			printf("Case #%d: O won\n", t);
			continue;
		}


		// no winners
		if(dot_count > 0)
			printf("Case #%d: Game has not completed\n", t);
		else
			printf("Case #%d: Draw\n", t);

	}
	return 0;
}
