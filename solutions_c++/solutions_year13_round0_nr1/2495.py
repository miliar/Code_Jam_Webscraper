#include <cstdio>
#include <cstring>

using namespace std;

	enum chess
	{
		X = 0,
		O = 1,
		T = 2,
		SPACE = 3
	};
	enum status
	{
		Xwin = 0,
		Owin = 1,
		Draw = 2,
		None = 3
	};

status WhoWin(int count[])
{
	if ((count[T] == 1 && count[X] == 3)
	|| (count[T] == 0 && count[X] == 4))
	{
		return Xwin;
	}
	if ((count[T] == 1 && count[O] == 3)
	|| (count[T] == 0 && count[O] == 4))
	{
		return Owin;
	}
	return None;
}

chess Trans(char c)
{
	switch (c)
	{
	case 'X':return X;
	case 'O':return O;
	case '.':return SPACE;
	case 'T':return T;
	}
}
int main()
{
	bool isDone = false, isDraw = true;
	int num, count[4];
	char tmp, inName[30], outName[30];
        chess board[4][4];
	status outcome[1000];

	FILE *fin, *fout;

	scanf("%s", inName);
	scanf("%s", outName);
	fin = fopen(inName, "r");
	fout = fopen(outName, "w");
	fscanf(fin, "%d", &num);
	for (int k = 1; k <= num; k++)
	{
		fgetc(fin);
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				tmp = fgetc(fin);
				board[i][j] = Trans(tmp);
			}
			fgetc(fin);
		}

		isDone = false;
		isDraw = true;
		for (int i = 0; i < 4; i++)
		{
			memset(count, 0, sizeof(int)*4);
			for (int j = 0; j < 4; j++)
			{
				count[board[i][j]]++;
			}
			if((outcome[k] = WhoWin(count)) != None)
			{
				isDone = true;
				break;
			}
		}
		if (isDone)
		{
			continue;
		}
		for (int i = 0; i < 4; i++)
		{
			memset(count, 0, sizeof(int)*4);
			for (int j = 0; j < 4; j++)
			{
				count[board[j][i]]++;
			}
			if((outcome[k] = WhoWin(count)) != None)
			{
				isDone = true;
				break;
			}
		}
		if (isDone)
		{
			continue;
		}
		memset(count, 0, sizeof(int)*4);
		for (int i = 0; i < 4; i++)
		{
			count[board[i][i]]++;
		}
		if((outcome[k] = WhoWin(count)) != None)
		{
			continue;
		}
		memset(count, 0, sizeof(int)*4);
		for (int i = 0; i < 4; i++)
		{
			count[board[i][3-i]]++;
		}
		if((outcome[k] = WhoWin(count)) != None)
		{
			continue;
		}
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (board[i][j] == SPACE)
				{
					isDraw = false;
				}
			}
		}
		if (isDraw)
		{
			outcome[k] = Draw;
		}
		else
		{
			outcome[k] = None;
		}
	}

	for (int k = 1; k <= num; k++)
	{
		fprintf(fout, "Case #%d: ", k);
		switch (outcome[k])
		{
		case Xwin:fprintf(fout, "X won\n"); break;
		case Owin:fprintf(fout, "O won\n"); break;
		case Draw:fprintf(fout, "Draw\n"); break;
		case None:fprintf(fout, "Game has not completed\n"); break;
		}
	}
	fclose(fout);
	fclose(fout);
	return 0;
}

