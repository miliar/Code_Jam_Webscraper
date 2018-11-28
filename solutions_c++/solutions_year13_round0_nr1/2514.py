#include <cstdio>

char Map[4][5];

int isX(char C)
{
	return C == 'X' || C == 'T';
}

int isO(char C)
{
	return C == 'O' || C == 'T';
}

int Check()
{
	if (isX(Map[0][0]) && isX(Map[1][1]) && isX(Map[2][2]) && isX(Map[3][3]))
		return 1;
	if (isX(Map[0][3]) && isX(Map[1][2]) && isX(Map[2][1]) && isX(Map[3][0]))
		return 1;
	if (isO(Map[0][0]) && isO(Map[1][1]) && isO(Map[2][2]) && isO(Map[3][3]))
		return 2;
	if (isO(Map[0][3]) && isO(Map[1][2]) && isO(Map[2][1]) && isO(Map[3][0]))
		return 2;
	int CntRX[4] = {0}, CntCX[4] = {0}, CntRO[4] = {0}, CntCO[4] = {0}, Dot = 0;
	for (int i = 0; i < 4; i ++)
		for (int j = 0; j < 4; j ++)
		{
			if (Map[i][j] == '.')
				Dot = 1;
			else if (isX(Map[i][j]))
			{
				CntRX[i] ++;
				CntCX[j] ++;
			}
			else if (isO(Map[i][j]))
			{
				CntRO[i] ++;
				CntCO[j] ++;
			}
		}
	for (int i = 0; i < 4; i ++)
	{
		if (CntRX[i] == 4 || CntCX[i] == 4)
			return 1;
		if (CntRO[i] == 4 || CntCO[i] == 4)
			return 2;
	}
	return Dot ? 4 : 3;
}

void Work(int Case)
{
	for (int i = 0; i < 4; i ++)
		scanf("%s", Map[i]);
	int Status = Check();
	printf("Case #%d: ", Case);
	if (Status == 1)
		printf("X won\n");
	else if (Status == 2)
		printf("O won\n");
	else if (Status == 3)
		printf("Draw\n");
	else
		printf("Game has not completed\n");
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		Work(Case);
	return 0;
}