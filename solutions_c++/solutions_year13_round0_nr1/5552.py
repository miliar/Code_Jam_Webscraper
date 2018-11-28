#include <stdio.h>

#define FILENAME "A-small-attempt1.in"

void main()
{
	FILE *f = fopen(FILENAME, "rb");
	FILE *fOut = fopen("QR_A_out.txt", "wb");
	int T;
	fscanf(f, "%d", &T);
	for(int t = 0; t < T; ++t)
	{
		char line[4][5];
		for(int i = 0; i < 4; ++i)
			fscanf(f, "%s", line[i]);
		
		char C = 0;
		char R = 0;
		for(int row = 0; row < 4; ++row)
		{
			C = 0;
			for(int col = 0; col < 4; ++col)
			{
				if(!C && line[row][col] != 'T')
					C = line[row][col];

				if(line[row][col] == '.')
				{
					R = '.';
					break;
				}
				if(C && line[row][col] != C && line[row][col] != 'T')
					break;

				if(col == 3 && C && (C == line[row][col] || line[row][col] == 'T') && C != '.')
				{
					R = C;
					goto Out;
				}
			}
		}

		for(int col = 0; col < 4; ++col)
		{
			C = 0;
			for(int row = 0; row < 4; ++row)
			{
				if(!C && line[row][col] != 'T')
					C = line[row][col];

				if(line[row][col] == '.')
				{
					R = '.';
					break;
				}
				if(C && line[row][col] != C && line[row][col] != 'T')
					break;
				if(row == 3 && C && (C == line[row][col] || line[row][col] == 'T') && C != '.')
				{
					R = C;
					goto Out;
				}
			}
		}

		C = 0;
		for(int d = 0; d < 4; ++d)
		{
			if(!C && line[d][d] != 'T')
				C = line[d][d];
			if(line[d][d] == '.')
			{
				R = '.';
				break;
			}
			if(C && line[d][d] != C && line[d][d] != 'T')
				break;

			if(d == 3 && C && (C == line[d][d] || line[d][d] == 'T') && C != '.')
			{
				R = C;
				goto Out;
			}
		}

		C = 0;
		for(int d = 0; d < 4; ++d)
		{
			if(!C && line[3-d][d] != 'T')
				C = line[3-d][d];
			if(line[3-d][d] == '.')
			{
				R = '.';
				break;
			}
			if(C && line[3-d][d] != C && line[3-d][d] != 'T')
				break;

			if(d == 3 && C && (C == line[3-d][d] || line[3-d][d] == 'T') && C != '.')
			{
				R = C;
				goto Out;
			}
		}

Out:
		if(R == 'X' || R == 'O')
			fprintf(fOut, "Case #%d: %c won\r\n", t+1, R);
		else if(R == '.')
			fprintf(fOut, "Case #%d: Game has not completed\r\n", t+1);
		else
			fprintf(fOut, "Case #%d: Draw\r\n", t+1);
	}

	fclose(f);
	fclose(fOut);
}