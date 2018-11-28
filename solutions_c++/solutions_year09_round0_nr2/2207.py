#include <stdio.h>
#include <stdlib.h>

#define INPUTFILE "B-large.in"
#define OUTPUTFILE "B-large.out"

#define H_MAX 100
#define W_MAX 100

int value[H_MAX][W_MAX];
char label[H_MAX][W_MAX];

int H, W;
char labelChar;


void Travel(int x, int y)
{	
	label[x][y] = labelChar;

	int outFlag = 0;

	if (x-1 >= 0 )	// (x-1, y) is exist
	{
		if (label[x-1][y] == 0)
		{
			if (value[x-1][y] < value[x][y])
			{
				int existFlag = 0;

				if (y-1 >= 0 && value[x][y-1] < value[x-1][y])
					existFlag = 1;
				if (existFlag == 0)
				{
					if (y+1 <= W-1 && value[x][y+1] < value[x-1][y])
						existFlag = 1;
				}
				if (existFlag == 0)
				{
					if (x+1 <= H-1 && value[x+1][y] < value[x-1][y])
						existFlag = 1;
				}
				if (existFlag == 0)
				{
					Travel(x-1, y);		
					outFlag = 1;
				}
			} // if (value[x-1][y] < value[x][y])
			else if (value[x-1][y] > value[x][y])
			{
				int existFlag = 0;
				if (x-2 >= 0 && value[x-2][y] <= value[x][y])
					existFlag = 1;
				if (existFlag == 0)
				{
					if (y-1 >= 0 && value[x-1][y-1] <= value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
				{
					if (y+1 <= W-1 && value[x-1][y+1] <= value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
					Travel(x-1, y);
			}
		} // if (label[x-1][y] == 0)
	} // if (x-1 >= 0 )	// (x-1, y) is exist

	if (y-1 >= 0) // (x, y-1) is exist
	{
		if (label[x][y-1] == 0)
		{
			if (value[x][y-1] < value[x][y])
			{
				if (outFlag == 0)
				{
					int existFlag = 0;
					if (x-1 >= 0 && value[x-1][y] <= value[x][y-1])
					{
						existFlag = 1;
					}
					if (existFlag == 0)
					{
						if (y+1 <= W-1 && value[x][y+1] < value[x][y-1])
							existFlag = 1;
					}
					if (existFlag == 0)
					{
						if (x+1 <= H-1 && value[x+1][y] < value[x][y-1])
							existFlag = 1;
					}
					if (existFlag == 0)
					{
						Travel(x, y-1);
						outFlag = 1;
					}
				}
			} // if (value[x][y-1] < value[x][y])
			else if (value[x][y-1] > value[x][y])
			{
				int existFlag = 0;
				if (x-1 >= 0 && value[x-1][y-1] <= value[x][y])
					existFlag = 1;
				if (existFlag == 0)
				{
					if (y-2 >= 0 && value[x][y-2] <= value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
				{
					if (x+1 <= H-1 && value[x+1][y-1] < value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
					Travel(x, y-1);
			} // if (value[x][y-1] > value[x][y])
		} // if (label[x][y-1] == 0)
	} // if (y-1 >= 0) // (x, y-1) is exist


	if (y+1 <= W-1)	// (x, y+1) is exist
	{
		if (label[x][y+1] == 0)
		{
			if (value[x][y+1] < value[x][y]) 
			{
				if (outFlag == 0)
				{
					int existFlag = 0;

					if (x-1 >= 0 && value[x-1][y] <= value[x][y+1])
						existFlag = 1;
					if (existFlag == 0)
					{
						if (y-1 >= 0 && value[x][y-1] <= value[x][y+1])
							existFlag = 1;
					}
					if (existFlag == 0)
					{
						if (x+1 <= H-1 && value[x+1][y] < value[x][y+1])
							existFlag = 1;
					}
					if (existFlag == 0)
					{
						Travel(x, y+1);		
						outFlag = 1;
					}
				} // if (outFlag == 0)
			} // if (value[x][y+1] < value[x][y]) 
			else if (value[x][y+1] > value[x][y])
			{
				int existFlag = 0;

				if (x-1 >= 0 && value[x-1][y+1] <= value[x][y])
					existFlag = 1;
				if (existFlag == 0)
				{
					if (y+2 <= W-1 && value[x][y+2] < value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
				{
					if (x+1 <= H-1 && value[x+1][y+1] < value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
					Travel(x, y+1);
			} // if (value[x][y+1] > value[x][y])
		} // if (label[x][y+1] == 0)
	} // if (y+1 <= W-1)	// (x, y+1) is exist
	
	if (x+1 <= H-1)		// (x+1, y) is exist
	{
		if (label[x+1][y] == 0)
		{
			if (value[x+1][y] < value[x][y])
			{
				if (outFlag == 0)
				{
					int existFlag = 0;

					if (x-1 >= 0 && value[x-1][y] <= value[x+1][y])
						existFlag = 1;
					if (existFlag == 0)
					{
						if (y-1 >= 0 && value[x][y-1] <= value[x+1][y])
							existFlag = 1;
					}
					if (existFlag == 0)
					{
						if (y+1 <= W-1 && value[x][y+1] <= value[x+1][y])
							existFlag = 1;
					}
					if (existFlag == 0)
					{
						Travel(x+1, y);		
						outFlag = 1;
					}
				} // if (outFlag == 0)
			} // if (value[x+1][y] < value[x][y])
			else if (value[x+1][y] > value[x][y])
			{
				int existFlag = 0;

				if (y-1 >= 0 && value[x+1][y-1] < value[x][y])
					existFlag = 1;
				if (existFlag == 0)
				{
					if (y+1 <= W-1 && value[x+1][y+1] < value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
				{
					if (x+2 <= H-1 && value[x+2][y] < value[x][y])
						existFlag = 1;
				}
				if (existFlag == 0)
					Travel(x+1, y);
			}
		} // if (label[x+1][y] == 0)
	} // if (x+1 <= H-1)		// (x+1, y) is exist

} // void Travel(int x, int y)

int main()
{
	FILE *fpIn, *fpOut;

	fpIn = fopen(INPUTFILE, "r");
	fpOut = fopen(OUTPUTFILE, "w");

	int T;
	fscanf(fpIn, "%d", &T);	

	for (int cnt1 = 0; cnt1 < T; cnt1++)
	{		
		fscanf(fpIn, "%d %d", &H, &W);	

		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
			{
				fscanf(fpIn, "%d", &value[i][j]);
				label[i][j] = 0;
			}
	

		labelChar = 'a';
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				if (label[i][j] == 0)
				{
					Travel(i, j);
					labelChar = labelChar + 1;
				}
			}
		}
		
		fprintf(fpOut, "Case #%d:\n", cnt1+1);
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				fprintf(fpOut, "%c ", label[i][j]);
			}
			fprintf(fpOut, "\n");
		}
	} // for (int cnt1 = 0; cnt1 < T; cnt1++)

	fclose(fpIn);
	fclose(fpOut);
}