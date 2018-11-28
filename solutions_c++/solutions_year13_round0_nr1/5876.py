#include <stdio.h>
#include <vector>

bool FindAtHorizon(char* cArr, char findChar);
bool FindAtVertical(char* cArr, char findChar);
bool FindAtDiagonal(char* cArr, char findChar);
bool IsDraw(char* cArr);

void main()
{
	FILE *fp = NULL;
	FILE *fwp = NULL;

	fp = fopen("D:\\Codejam\\prob1\\tik\\A-small-attempt0.in", "r");
	fwp = fopen("output.in", "w");
	if( fp == NULL)
		return;
	
	int nCase = 0;
	fscanf(fp, "%d", &nCase);

	for(int i=0; i < nCase; i++)
	{
		char cArr[4][4];

		for(int j=0; j < 4; j++)
		{
			for(int k=0; k < 4; k++)
			{
				char value;
				fscanf(fp, "%c", &value);
				if( value != 84 && value != 46 && value != 79 && value != 88)
				{
					k--;
					continue;
				}

				cArr[j][k] = value;
			}
		}

		if(FindAtHorizon(cArr[0], 'X') || FindAtVertical(cArr[0], 'X') || FindAtDiagonal(cArr[0], 'X'))
		{
			//printf("Case #%d: X won\n", i + 1);
			fprintf(fwp, "Case #%d: X won\n", i + 1);
			continue;
		}

		if(FindAtHorizon(cArr[0], 'O') || FindAtVertical(cArr[0], 'O') || FindAtDiagonal(cArr[0], 'O'))
		{
			//printf("Case #%d: O won\n", i + 1);
			fprintf(fwp,"Case #%d: O won\n", i + 1);
			continue;
		}

		if( IsDraw(cArr[0]) )
		{
			//printf("Case #%d: Draw\n", i + 1);
			fprintf(fwp, "Case #%d: Draw\n", i + 1);
			continue;
		}
		else
		{
			//printf("Case #%d: Game has not completed\n", i + 1);
			fprintf(fwp, "Case #%d: Game has not completed\n", i + 1);
			continue;
		}
	}
}

bool FindAtHorizon(char *cArr, char findChar)
{
	for(int i=0; i < 4; i++)
	{
		int nFindCount = 0;
		for(int j=0; j < 4; j++)
		{
			if(*(cArr + i*4 + j) == 'T' || *(cArr + i*4 + j) == findChar )
				nFindCount++;
		}

		if( nFindCount == 4 )
			return true;
	}
	return false;	
}

bool FindAtVertical(char* cArr, char findChar)
{
	for(int i=0; i < 4; i++)
	{
		int nFindCount = 0;
		for(int j=0; j < 4; j++)
		{
			if(*(cArr + i + j*4) == 'T' || *(cArr + i + j*4) == findChar )
				nFindCount++;
		}

		if( nFindCount == 4 )
			return true;
	}
	return false;	
}

bool FindAtDiagonal(char* cArr, char findChar)
{
	int nFindCount = 0;
	for(int i=0; i < 4; i++)
	{
		if(*(cArr + i + 4*i) == 'T' || *(cArr + i + 4*i) == findChar )
			nFindCount++;
	}

	if( nFindCount == 4 )
		return true;

	nFindCount = 0;
	for(int i=0; i < 4; i++)
	{
		if(*(cArr + 3*(i+1) ) == 'T' || *(cArr + 3*(i+1) ) == findChar )
			nFindCount++;
	}
	if( nFindCount == 4 )
		return true;

	return false;	
}

bool IsDraw(char* cArr)
{
	for(int i=0; i < 4; i++)
	{
		for(int j=0; j < 4; j++)
		{
			if(*(cArr  +i + j) == '.')
				return false;
		}
	}
	return true;
}