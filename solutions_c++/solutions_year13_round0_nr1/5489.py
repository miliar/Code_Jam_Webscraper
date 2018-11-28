// 谷歌预赛.cpp : 定义控制台应用程序的入口点。
//

#include <stdio.h>

static char szResult[4][30] = {
	"X won",
	"O won",
	"Draw",
	"Game has not completed"
};

// chess borad
static char szChessBoard[4][4] = { 0 };

// output Array
int szOutputArray[1000] = { 0 };


// Judge Who is win
int JudgeWiner(char (*pChessBoard)[4][4], int nEmptyNum)
{
	int nReturn = -1, i, j;
	char cPlayer;
	int nContinuation;

	// 判断正对角线
	cPlayer = (*pChessBoard)[0][0];
	if (cPlayer != '.')
	{
		nContinuation = 1;
		for (i = 1; i < 4; i ++)
		{
			if (cPlayer == 'T') // 如果[0][0]位置为T
			{
				cPlayer = (*pChessBoard)[i][i];
				nContinuation ++;
			}
			else // 如果[0][0]位置不为T
			{
				// 如果当前[i][i]相等， 或者为'T'
				if (cPlayer == (*pChessBoard)[i][i] || (*pChessBoard)[i][i] == 'T')
				{
					nContinuation ++;
				}
				else
				{
					break;
				}
			}
		}
		// 对角线赢了
		if (nContinuation == 4)
		{
			nReturn = 1;
			if (cPlayer == 'X')
			{
				nReturn = 0;
			}

			return nReturn;
		}
	}


	
	// 判断行列
	for (i = 0; i < 4; i ++)
	{
		// 如果对角线[i][i]为'.'则该行列不可能会产生赢家
		cPlayer = (*pChessBoard)[i][i];
		if ( cPlayer != '.')
		{
			// 判断行
			nContinuation = 1;
			for(j = 0; j < 4; j ++)
			{
				if (i != j)
				{
					// 该行不能存在 '.'
					if((*pChessBoard)[i][j] == '.')
					{
						break;
					}
					// 如果第 i,i 位置为T， 则替换为该行的第一个不为T或者.的选手
					else if (cPlayer == 'T') 
					{
						cPlayer = (*pChessBoard)[i][j];
						nContinuation ++;
						continue;
					}
					else  // 该行的位置 为 O 或者 X
					{
						// 选手一样
						if ((*pChessBoard)[i][j] == cPlayer || (*pChessBoard)[i][j] == 'T')
						{
							nContinuation ++;
						}
						// 选手不一样
						else
						{
							break;
						}
					}

	
				}
			}// for j
			// 该行赢了
			if (nContinuation == 4)
			{
				nReturn = 1;
				if (cPlayer == 'X')
				{
					nReturn = 0;
				}

				return nReturn;
			}

			// 判断列
			nContinuation = 1;
			for(j = 0; j < 4; j ++)
			{
				if (i != j)
				{
					// 该行不能存在 '.'
					if((*pChessBoard)[j][i] == '.')
					{
						break;
					}
					// 如果第 i,i 位置为T， 则替换为该行的第一个不为T或者.的选手
					else if (cPlayer == 'T') 
					{
						cPlayer = (*pChessBoard)[j][i];
						nContinuation ++;
						continue;
					}
					else  // 该行的位置 为 O 或者 X
					{
						// 选手一样
						if ((*pChessBoard)[j][i] == cPlayer || (*pChessBoard)[j][i] == 'T')
						{
							nContinuation ++;
						}
						// 选手不一样
						else
						{
							break;
						}
					}


				}
			}// for j
			// 该列赢了
			if (nContinuation == 4)
			{
				nReturn = 1;
				if (cPlayer == 'X')
				{
					nReturn = 0;
				}

				return nReturn;
			}
		}
	}



	// 判断反斜对角线
	cPlayer = (*pChessBoard)[3][0];
	if (cPlayer != '.')
	{
		nContinuation = 1;
		for (i = 1, j = 2; j >= 0 && i <= 3; i ++, j --)
		{
			if (cPlayer == 'T') // 如果[0][0]位置为T
			{
				cPlayer = (*pChessBoard)[i][j];
				nContinuation ++;
			}
			else // 如果[0][0]位置不为T
			{
				// 如果当前[i][i]相等， 或者为'T'
				if (cPlayer == (*pChessBoard)[i][j] || (*pChessBoard)[i][j] == 'T')
				{
					nContinuation ++;
				}
				else
				{
					break;
				}
			}
		}
		// 反斜对角线赢了
		if (nContinuation == 4)
		{
			nReturn = 1;
			if (cPlayer == 'X')
			{
				nReturn = 0;
			}

			return nReturn;
		}
	}



	nReturn = 3;
	if (nEmptyNum == 0)
	{
		nReturn = 2;
	}

	return nReturn;
}

int main()
{
	int i, nRow, nCol, nTNum = 0, nEmptyNum;
	char cTmp;
	FILE* pFile = fopen("A-small-attempt0.in", "r");

	// INPUT
	// Get the times number
	fscanf(pFile, "%d\n", &nTNum);
   // input the chess Game
	for (i = 0; i < nTNum; i ++)
	{
		nEmptyNum = 0;

		for (nRow = 0; nRow < 4; nRow ++)
		{
			for (nCol = 0; nCol < 4; nCol ++)
			{
				if (nCol != 3)
				{
					fscanf(pFile, "%c", &cTmp);
				}
				else
				{
					fscanf(pFile, "%c\n", &cTmp);
				}

				if (cTmp == '.')
				{
					nEmptyNum ++;
				}

				szChessBoard[nRow][nCol] = cTmp;
				
			}
		}

		// to judge who is win
		szOutputArray[i] = JudgeWiner(&szChessBoard, nEmptyNum);
	}

	fclose(pFile);

	// OUTPUT
	pFile = fopen("output.txt", "w");
	for (i = 0; i < nTNum; i ++)
	{
		fprintf(pFile,"Case #%d: %s\n", i + 1, szResult[szOutputArray[i]]);
	}

	fclose(pFile);
	return 0;
}