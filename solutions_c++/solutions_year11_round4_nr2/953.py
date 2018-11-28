// Question B.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <list>
#include <vector>
#include <cassert>
#include <cstdio>

using namespace std;

bool debug = false;

int grid[500][500];
int wrGrid[500][500];
int wcGrid[500][500];

int _tmain(int argc, _TCHAR* argv[])
{
	int T;

//	FILE *fp = fopen("C:\\Users\\Public\\Documents\\Codejam\\Source\\B-sample.txt", "r");
	FILE *fp = stdin;
	FILE *outFile = stdout;

	if (fp == 0)
	{
		printf("couldn't open input!");
		exit(1);
	}

	char line[1000];

	fgets(line, 1000, fp);
	
	sscanf(line, "%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int R, C, D;
		int maxK;
		int maxSide;

		fgets(line, 1000, fp);
		if (debug)
		{
//			printf("|%s|\n", line);
		}

        assert(sscanf(line, "%d %d %d", &R, &C, &D) == 3);

		if (R > C)
			maxSide = R;
		else
			maxSide = C;

		maxK = maxSide;

		for (int r = 0; r < R; r++)
		{
			fgets(line, 1000, fp);
			for (int c = 0; c < C; c++)
			{
				grid[r][c] = line[c] - '0' + D;
			}
		}

		if (debug)
		{
		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				printf("%c", grid[r][c] - D + '0');
			}
			printf("\n");
		}
		}

		int bestK = 0;
		int minK = 3;

		// eval each point as possible center of mass
		for (int cr = 1; cr < R - 1; cr++)
		{
			for (int cc = 1; cc < C - 1; cc++)
			{
				for (int r = 0; r < R; r++)
				{
					for (int c = 0; c < C; c++)
					{
						wrGrid[r][c] = grid[r][c] * (r - cr);
						wcGrid[r][c] = grid[r][c] * (c - cc);
					}

				}

				for (int k = maxK; k >= minK; k--)
				{
					int startR = cr - k/2;
					int startC = cc - k/2;
					int endR = startR + k - 1;
					int endC = startC + k - 1;
					
					if (k % 2 == 0)
					{
						endC++;
						endR++;
					}

					long long sumR = 0;
					long long sumC = 0;


					if ((startR < 0) || (startC < 0))
					{
						continue;
					}

					if ((endR >= R) || (endC >= C))
					{
						continue;
					}

					int rScale;
					int cScale;

					for (int r = startR; r <= endR; r++)
					{
						if (k % 2 == 0)
						{
							if ((r == startR) || (r == endR))
								rScale = 1;
							else
								rScale = 2;
						}
						else
						{
							rScale = 2;
						}

						for (int c = startC; c <= endC; c++)
						{
						
							if (k % 2 == 0)
							{
							if ((c == startC) || (C == endC))
								cScale = 1;
							else
								cScale = 2;
							}
							else
							{
								cScale = 2;
							}


							sumR += cScale*rScale*wrGrid[r][c];
							sumC += cScale*rScale*wcGrid[r][c];
						}
					}

					if (k % 2 == 0)
					{
						rScale = cScale = 1;
					}
					else
					{
						rScale = cScale = 2;
					}

					sumR -= cScale*rScale*wrGrid[startR][startC];
					sumR -= cScale*rScale*wrGrid[startR][endC];
					sumR -= cScale*rScale*wrGrid[endR][startC];
					sumR -= cScale*rScale*wrGrid[endR][endC];

					sumC -= cScale*rScale*wcGrid[startR][startC];
					sumC -= cScale*rScale*wcGrid[startR][endC];
					sumC -= cScale*rScale*wcGrid[endR][startC];
					sumC -= cScale*rScale*wcGrid[endR][endC];

					if ((sumR == 0) && (sumC == 0))
					{
						bestK = k;
						minK = k + 1;

						if (debug)
						{
						  printf("%d,%d %d\n", cr, cc, k);
						}
						break;
					}
				}
			}
		}

		// eval each point as possible center of mass
		for (int cr = 1; cr < R - 1; cr++)
		{
			for (int cc = 1; cc < C - 1; cc++)
			{
				for (int r = 0; r < R; r++)
				{
					for (int c = 0; c < C; c++)
					{
						wrGrid[r][c] = grid[r][c] * ((r - cr)*2 - 1);
						wcGrid[r][c] = grid[r][c] * ((c - cc)*2 - 1);
					}

				}

				if ((cc == 1) && (cr == 1) && (t == 3))
				{
							for (int r = 0; r < R; r++)
							{
								for (int c = 0; c < C; c++)
								{
						//			printf("%6d", wrGrid[r][c]);
								}
				//				printf("    weight %d maxK %d", (r - cr) * 2 - 1, maxK);
					//			printf("\n");
							}
				}

				for (int k = maxK; k >= minK; k--)
				{
					int startR = cr - k/2 + 1;
					int startC = cc - k/2 + 1;
					int endR = startR + k - 1;
					int endC = startC + k - 1;
					
					if (k % 2 == 1)
					{
						endC++;
						endR++;
					}

				    if ((cc == 1) && (cr == 1) && (t == 3))
					{
			//			printf("R %d %d C %d %d k %d\n", startR, endR, startC, endC, k);
					}


					long long sumR = 0;
					long long sumC = 0;


					if ((startR < 0) || (startC < 0))
					{
						continue;
					}

					if ((endR >= R) || (endC >= C))
					{
						continue;
					}

					int rScale;
					int cScale;

					for (int r = startR; r <= endR; r++)
					{
						if (k % 2 == 1)
						{
							if ((r == startR) || (r == endR))
								rScale = 1;
							else
								rScale = 2;
						}
						else
						{
							rScale = 2;
						}

						for (int c = startC; c <= endC; c++)
						{
						
							if (k % 2 == 1)
							{
							if ((c == startC) || (C == endC))
								cScale = 1;
							else
								cScale = 2;
							}
							else
							{
								cScale = 2;
							}


							sumR += cScale*rScale*wrGrid[r][c];
							sumC += cScale*rScale*wcGrid[r][c];
						}
					}

					if (k % 2 == 1)
					{
						rScale = cScale = 1;
					}
					else
					{
						rScale = cScale = 2;
					}

					sumR -= cScale*rScale*wrGrid[startR][startC];
					sumR -= cScale*rScale*wrGrid[startR][endC];
					sumR -= cScale*rScale*wrGrid[endR][startC];
					sumR -= cScale*rScale*wrGrid[endR][endC];

					sumC -= cScale*rScale*wcGrid[startR][startC];
					sumC -= cScale*rScale*wcGrid[startR][endC];
					sumC -= cScale*rScale*wcGrid[endR][startC];
					sumC -= cScale*rScale*wcGrid[endR][endC];

					if ((sumR == 0) && (sumC == 0))
					{
						bestK = k;
						minK = k + 1;

						if (debug)
						{
						  printf("%d,%d %d\n", cr, cc, k);
						}
						break;
					}
				}
			}
		}


		printf ("Case #%d: ", t);

		if (bestK == 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", bestK);
	}

//	getchar();

	return 0;
}

