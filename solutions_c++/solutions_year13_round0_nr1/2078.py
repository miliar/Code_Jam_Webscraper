#include <cstdio>
#include <cstring>
#include <cstdlib>


int main()
{
	FILE *input = fopen("A.in","r");
	FILE *output = fopen("A.out","w+");

	int tests; fscanf(input,"%d",&tests);

	for(int test = 1 ; test <= tests ; test ++)
	{
		char board[5][5];

		fscanf( input,"%s",board[0] );
		fscanf( input,"%s",board[1] );
		fscanf( input,"%s",board[2] );
		fscanf( input,"%s",board[3] );

		int tmp_x = 0;
		int tmp_o = 0;
		int total = 0;
		bool win = false;

		for(int j = 0 ; j < 4 ; j ++)
		{
			for(int i = 0 ; i < 4 ; i ++)
			{
				switch (board[j][i])
				{
				case 'T': 
					tmp_x ++;
					tmp_o ++;
					total ++;
					break;
				case 'X':
					tmp_x ++;
					total ++;
					break;
				case 'O':
					tmp_o ++;
					total ++;
					break;
				default:
					break;
				}
			}

			if( tmp_x == 4 ){
				fprintf(output,"Case #%d: X won\n",test);
				win = true;
				break;
			}
			if( tmp_o == 4 ){
				fprintf(output,"Case #%d: O won\n",test);
				win = true;
				break;
			}

			tmp_x = 0;
			tmp_o = 0;
		}

		if(win){
			continue;
		}

		tmp_x = 0;
		tmp_o = 0;
		win = false;

		for(int j = 0 ; j < 4 ; j ++)
		{
			for(int i = 0 ; i < 4 ; i ++)
			{
				switch (board[i][j])
				{
				case 'T': 
					tmp_x ++;
					tmp_o ++;
					break;
				case 'X':
					tmp_x ++;
					break;
				case 'O':
					tmp_o ++;
					break;
				default:
					break;
				}
			}

			if( tmp_x == 4 ){
				fprintf(output,"Case #%d: X won\n",test);
				win = true;
				break;
			}
			if( tmp_o == 4 ){
				fprintf(output,"Case #%d: O won\n",test);
				win = true;
				break;
			}

			tmp_x = 0;
			tmp_o = 0;
		}

		if(win){
			continue;
		}

		tmp_x = 0;
		tmp_o = 0;
		for(int i = 0 ; i < 4 ; i ++)
		{
			switch (board[i][i])
			{
			case 'X':
				tmp_x ++;
				break;
			case 'O':
				tmp_o ++;
				break;
			case 'T':
				tmp_x ++;
				tmp_o ++;
				break;
			default:
				break;
			}
		}

		if( tmp_x == 4 ){
			fprintf(output,"Case #%d: X won\n",test);
			continue;
		}
		if( tmp_o == 4 ){
			fprintf(output,"Case #%d: O won\n",test);
			continue;
		}

		tmp_x = 0;
		tmp_o = 0;
		for(int i = 0 ; i < 4 ; i ++)
		{
			switch (board[3-i][i])
			{
			case 'X':
				tmp_x ++;
				break;
			case 'O':
				tmp_o ++;
				break;
			case 'T':
				tmp_x ++;
				tmp_o ++;
				break;
			default:
				break;
			}
		}

		if( tmp_x == 4 ){
			fprintf(output,"Case #%d: X won\n",test);
			continue;
		}
		if( tmp_o == 4 ){
			fprintf(output,"Case #%d: O won\n",test);
			continue;
		}

		if(total == 16){
			fprintf(output,"Case #%d: Draw\n",test);
		}
		else{
			fprintf(output,"Case #%d: Game has not completed\n",test);
		}
	}
	
	return 0;
}