#include <stdio.h>

int T;

char table [5][5];
int direction [4][2] = {1,0,0,1,1,1,1,-1};

bool check3(int a, int b, char who)
{
	bool flag;
	for (int d=0;d<4;++d)
	{
		if (a+2*direction[d][0]>=0 && a+2*direction[d][0]<4 && b+2*direction[d][1]>=0 && b+2*direction[d][1]<4)
		{
			flag = true;
			for (int i=0;i<3;i++)
			{
				if (table[a+i*direction[d][0]][b+i*direction[d][1]]!=who)
					flag = false;
			}
			if (flag)
				return true;
		}
	}
	return false;
}

bool check4(int a, int b, char who)
{
	bool flag;
	for (int d=0;d<4;++d)
	{
		if (a+3*direction[d][0]>=0 && a+3*direction[d][0]<4 && b+3*direction[d][1]>=0 && b+3*direction[d][1]<4)
		{
			flag = true;
			for (int i=0;i<4;i++)
			{
				if (table[a+i*direction[d][0]][b+i*direction[d][1]]!=who && table[a+i*direction[d][0]][b+i*direction[d][1]]!='T')
					flag = false;
			}
			if (flag)
				return true;
		}
	}
	return false;
}

int win(char who)
{
	int ret = 0;
	int i,j;
	for (i=0;i<4;++i)
		for (j=0;j<4;++j)
		{
			if (check3(i,j,who))
				ret = ret==0 ? 3 : ret;
			if (check4(i,j,who))
				ret = 4;
		}
	return ret;
}

int main(int argc, char *argv())
{
	int i,j;
	char tmp;
	scanf("%d", &T);
	int X,O;
	for (int t=0;t<T;++t)
	{
		printf("Case #%d: ", t+1);
		for (i=0;i<4;++i)
			scanf("%s", table+i);
		bool finish = true;
		for (i=0;i<4;++i)
			for (j=0;j<4;++j)
				if (table[i][j]=='.')
					finish = false;
		;
		X = win('X');
		O = win('O');
		if (X>O)
			printf("X won\n");
		else if (O>X)
			printf("O won\n");
		else if (finish)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}