#include <stdio.h>

int Winner(char arr[5][5]);

int main(void)
{
	int n, i, flag;
	char TTT[5][5]={0};
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("A-large.out", "w");

	fscanf(in, "%d", &n);
	for( i=1; i<=n; i++ )
	{
		for ( int j=0; j<4; j++ )
			fscanf(in, "%s", TTT[j]);

		if ( !Winner(TTT) )
		{
			fprintf(out, "Case #%d: O won\n", i);
			continue;
		}
		else
		{
			flag=0;

			for ( int j=0; j<4; j++ )
			{
				for ( int k=0; k<4; k++ )
				{
					if ( TTT[j][k] == 'O' )
						TTT[j][k] = 'X';
					else if ( TTT[j][k] == 'X' )
						TTT[j][k] = 'O';
					else if ( TTT[j][k] == '.' )
						flag = 1;
				}
			}

			if ( !Winner(TTT) )
			{
				fprintf(out, "Case #%d: X won\n", i);
				continue;
			}
		}

		if ( flag )
			fprintf(out, "Case #%d: Game has not completed\n", i);
		else fprintf(out, "Case #%d: Draw\n", i);
	}
	return 0;
}

int Winner(char arr[5][5])
{
	int i, j;

	for ( i=0; i<4; i++ )
	{
		// l
		if ( arr[0][i] == 'O' || arr[0][i] == 'T' )
		{
			for ( j=1; j<4; j++ )
				if ( arr[j][i] != 'O' && arr[j][i] != 'T' )
					break;

			if ( j == 4 )
				return 0;
		}

		// ---
		if ( arr[i][0] == 'O' || arr[i][0] == 'T' )
		{
			for ( j=1; j<4; j++ )
				if ( arr[i][j] != 'O' && arr[i][j] != 'T' )
					break;

			if ( j == 4 )
				return 0;
		}
	}
	// i, i
	if ( arr[0][0] == 'O' || arr[0][0] == 'T' )
	{
		for ( i=1; i<4; i++ )
			if ( arr[i][i] != 'O' && arr[i][i] != 'T' )
				break;

		if ( i == 4 )
			return 0;
	}

	// i, 3-i
	if ( arr[0][3] == 'O' || arr[0][3] == 'T' )
	{
		for ( i=1; i<4; i++ )
			if ( arr[i][3-i] != 'O' && arr[i][3-i] != 'T' )
				break;

		if ( i == 4 )
			return 0;
	}
	
	return 1;
}