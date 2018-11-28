#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void)
{
	int size;
	FILE *input, *output;
	char str[5][5];
	char* xwin = "X won";
	char* owin = "O won";
	char* draw = "Draw";
	char* ncom = "Game has not completed";
	char temp[5];

	memset(str, 0, sizeof(char)*16);

	if((input = fopen("A-large.in", "rt")) == NULL)
	{
		printf("input fopen err\n");
		return 0;
	}

	if((output = fopen("A-large.out", "wt")) == NULL)
	{
		printf("output fopen err\n");
		return 0;
	}

	fscanf(input,"%d",&size);

	for( int i = 0 ; i < size ; i++ )
	{
		int flag = 0;

		for( int j = 0 ; j < 4; j++ )
		{
			fscanf(input, "%s\n", str[j]);
			str[j][4] = 0;

			if(strcmp(str[j], "OOOO") == 0  || strcmp(str[j], "OOOT") == 0 || strcmp(str[j], "OOTO") == 0 || strcmp(str[j], "OTOO") == 0 || strcmp(str[j], "TOOO") == 0)
			{
				fprintf(output, "Case #%d: %s\n", i+1, owin);
				flag = 1;
			}

			if(strcmp(str[j], "XXXX") == 0 || strcmp(str[j], "XXXT") == 0 || strcmp(str[j], "XXTX") == 0 || strcmp(str[j], "XTXX") == 0 || strcmp(str[j], "TXXX") == 0 )
			{
				fprintf(output, "Case #%d: %s\n", i+1, xwin);
				flag = 1;
			}
		}

		if(flag == 1) continue;

		for( int j = 0 ; j < 4 && flag != 1  ; j++ )
		{
			memset(temp, 0, 5);

			int k=0;
			for(; k<4  ; k++ )
				temp[k] = str[k][j];

			temp[k] = 0;

			if(strcmp(temp, "OOOO") == 0 || strcmp(temp, "OOOT") == 0 || strcmp(temp, "OOTO") == 0 || strcmp(temp, "OTOO") == 0 || strcmp(temp, "TOOO") == 0)
			{
				fprintf(output, "Case #%d: %s\n", i+1, owin);
				flag = 1;
			}

			if(strcmp(temp, "XXXX") == 0 || strcmp(temp, "XXXT") == 0 || strcmp(temp, "XXTX") == 0 || strcmp(temp, "XTXX") == 0 || strcmp(temp, "TXXX") == 0)
			{
				fprintf(output, "Case #%d: %s\n", i+1, xwin);
				flag = 1;
			}

			memset(temp, 0, 5);
		}

		if(flag == 1) continue;

		for( int j = 0; j < 2 && flag != 1  ; j++ )
		{
			memset(temp, 0, 5);
			if( j == 0 )
			{
				for(int a=0, b=0 ; a < 4 ; a++,b++)
					temp[a] = str[a][b];
				
				temp[4] = 0;
			}
			else
			{
				for(int a=0, b=3 ; a < 4 ; a++,b--)
					temp[a] = str[a][b];

				temp[4] = 0;
			}

			if(strcmp(temp, "OOOO") == 0 || strcmp(temp, "OOOT") == 0 || strcmp(temp, "OOTO") == 0 || strcmp(temp, "OTOO") == 0 || strcmp(temp, "TOOO") == 0)
			{
				fprintf(output, "Case #%d: %s\n", i+1, owin);
				flag = 1;
			}

			if(strcmp(temp, "XXXX") == 0 || strcmp(temp, "XXXT") == 0 || strcmp(temp, "XXTX") == 0 || strcmp(temp, "XTXX") == 0 || strcmp(temp, "TXXX") == 0)
			{
				fprintf(output, "Case #%d: %s\n", i+1, xwin);
				flag = 1;
			}
			memset(temp, 0, 5);
		}

		if(flag == 1) continue;

		else
		{
			for(int a=0 ; a<4 ; a++)
			{
				for( int b=0 ; b<4 ; b++)
				{
					if(str[a][b] == '.')
					{
						flag = 2;
						break;
					}
				}
			}

			if(flag == 2)
				fprintf(output, "Case #%d: %s\n", i+1, ncom);
			else
				fprintf(output, "Case #%d: %s\n", i+1, draw);
		}
	}

	fclose(input);
	fclose(output);
	return 0;
}
