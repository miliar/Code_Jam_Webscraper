// 01_X.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <basetsd.h>
#include <iostream>

#define SMALL_DATASET

#ifdef SMALL_DATASET
# define FILE_NAME_IN  "A-small-practice.in"

# define FILE_NAME_OUT "A-small-practice.out"
#else
# define FILE_NAME_IN  "A-large.in"
# define FILE_NAME_OUT "A-large.out"
#endif

int _tmain(int argc, _TCHAR* argv[])
{
  FILE * fileIn = NULL;
  FILE * fileOut = NULL;

  fopen_s(&fileIn, FILE_NAME_IN, "r");
  _ASSERT(fileIn!=NULL);

  fopen_s(&fileOut, FILE_NAME_OUT, "w+");
  _ASSERT(fileOut!=NULL);

  int num_of_test_cases;
  fscanf_s(fileIn, "%d", &num_of_test_cases);

  for (int i=0; i<num_of_test_cases; i++)
  {
    char str[5];
    bool completed = false;
	bool plrX = false;
	bool plrO = false;

	UINT8 plrXH;
	UINT8 plrXV[4] = {0};
	UINT8 plrX1 = 0;
	UINT8 plrX2 = 0;

	UINT8 plrOH;
	UINT8 plrOV[4] = {0};
	UINT8 plrO1 = 0;
	UINT8 plrO2 = 0;

    for (int lineNum=0; lineNum<4; lineNum++)
    {
		plrXH = 0;
		plrOH = 0;
		fscanf_s(fileIn, "%s", str, sizeof(str) );
		for ( int pos=0; pos<4; pos++)
		{
			switch ( str[pos])
			{
			case '.':
				completed = true;
				break;
			case 'O':
				plrOH++;
				plrOV[pos]++;
				if ( lineNum == pos )
					plrO1++;
				if ( lineNum == 3-pos )
					plrO2++;
				break;
			case 'X':
				plrXH++;
				plrXV[pos]++;
				if ( lineNum == pos )
					plrX1++;
				if ( lineNum == 3-pos )
					plrX2++;

				break;
			case 'T':
				plrXH++;
				plrOH++;
				plrXV[pos]++;
				plrOV[pos]++;
				if ( lineNum == pos )
				{
					plrX1++;
					plrO1++;
				}
				if ( lineNum == 3-pos )
				{
					plrX2++;
					plrO2++;
				}
				break;
			}
		}
		if ( plrXH == 4 ) plrX = true;
		if ( plrOH == 4 ) plrO = true;
    }

	if ( plrX1 == 4 || plrX2 == 4 )
		plrX = true;

	for ( int i=0; i<4; i++)
	{
		if ( plrXV[i] == 4 )
			plrX = true;
	}

	if ( plrO1 == 4 || plrO2 == 4 )
		plrO = true;

	for ( int i=0; i<4; i++)
	{
		if ( plrOV[i] == 4 )
			plrO = true;
	}

	if ( plrX )
	{
		fprintf(fileOut, "Case #%d: X won\n",i+1);
	}
	else if ( plrO )
	{
		fprintf(fileOut, "Case #%d: O won\n",i+1);
	}
	else if ( completed )
	{
		fprintf(fileOut, "Case #%d: Game has not completed\n",i+1);
	}
	else
	{
		fprintf(fileOut, "Case #%d: Draw\n",i+1);
	}

	if ( plrX && plrO )
		plrX = false;
  }

  _fcloseall();

#define SHOW_FILE(x) "type "##x
  system(SHOW_FILE(FILE_NAME_IN));
  printf("\n");
  system(SHOW_FILE(FILE_NAME_OUT));
  printf("\n");
  system("PAUSE");
  return 0;
}



