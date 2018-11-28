// �ȸ�Ԥ��.cpp : �������̨Ӧ�ó������ڵ㡣
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

	// �ж����Խ���
	cPlayer = (*pChessBoard)[0][0];
	if (cPlayer != '.')
	{
		nContinuation = 1;
		for (i = 1; i < 4; i ++)
		{
			if (cPlayer == 'T') // ���[0][0]λ��ΪT
			{
				cPlayer = (*pChessBoard)[i][i];
				nContinuation ++;
			}
			else // ���[0][0]λ�ò�ΪT
			{
				// �����ǰ[i][i]��ȣ� ����Ϊ'T'
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
		// �Խ���Ӯ��
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


	
	// �ж�����
	for (i = 0; i < 4; i ++)
	{
		// ����Խ���[i][i]Ϊ'.'������в����ܻ����Ӯ��
		cPlayer = (*pChessBoard)[i][i];
		if ( cPlayer != '.')
		{
			// �ж���
			nContinuation = 1;
			for(j = 0; j < 4; j ++)
			{
				if (i != j)
				{
					// ���в��ܴ��� '.'
					if((*pChessBoard)[i][j] == '.')
					{
						break;
					}
					// ����� i,i λ��ΪT�� ���滻Ϊ���еĵ�һ����ΪT����.��ѡ��
					else if (cPlayer == 'T') 
					{
						cPlayer = (*pChessBoard)[i][j];
						nContinuation ++;
						continue;
					}
					else  // ���е�λ�� Ϊ O ���� X
					{
						// ѡ��һ��
						if ((*pChessBoard)[i][j] == cPlayer || (*pChessBoard)[i][j] == 'T')
						{
							nContinuation ++;
						}
						// ѡ�ֲ�һ��
						else
						{
							break;
						}
					}

	
				}
			}// for j
			// ����Ӯ��
			if (nContinuation == 4)
			{
				nReturn = 1;
				if (cPlayer == 'X')
				{
					nReturn = 0;
				}

				return nReturn;
			}

			// �ж���
			nContinuation = 1;
			for(j = 0; j < 4; j ++)
			{
				if (i != j)
				{
					// ���в��ܴ��� '.'
					if((*pChessBoard)[j][i] == '.')
					{
						break;
					}
					// ����� i,i λ��ΪT�� ���滻Ϊ���еĵ�һ����ΪT����.��ѡ��
					else if (cPlayer == 'T') 
					{
						cPlayer = (*pChessBoard)[j][i];
						nContinuation ++;
						continue;
					}
					else  // ���е�λ�� Ϊ O ���� X
					{
						// ѡ��һ��
						if ((*pChessBoard)[j][i] == cPlayer || (*pChessBoard)[j][i] == 'T')
						{
							nContinuation ++;
						}
						// ѡ�ֲ�һ��
						else
						{
							break;
						}
					}


				}
			}// for j
			// ����Ӯ��
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



	// �жϷ�б�Խ���
	cPlayer = (*pChessBoard)[3][0];
	if (cPlayer != '.')
	{
		nContinuation = 1;
		for (i = 1, j = 2; j >= 0 && i <= 3; i ++, j --)
		{
			if (cPlayer == 'T') // ���[0][0]λ��ΪT
			{
				cPlayer = (*pChessBoard)[i][j];
				nContinuation ++;
			}
			else // ���[0][0]λ�ò�ΪT
			{
				// �����ǰ[i][i]��ȣ� ����Ϊ'T'
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
		// ��б�Խ���Ӯ��
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