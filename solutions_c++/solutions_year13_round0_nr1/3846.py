#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char map[4][5];

int main()
{
	int T;
	scanf("%d",&T);
	for (int caseno = 1;caseno<=T;++caseno)
	{
		getchar();
		for (int i=0;i<4;++i)
			gets(map[i]);
		int emptyCnt = 0;
		int lineX = 0;
		int lineY = 0;
		int lineT = 0;
		bool xwin = false;
		bool ywin = false;
		for (int i=0;i<4;++i)
		{
			lineX = lineY = lineT = 0;
			for (int j=0;j<4;++j)
			{
				if (map[i][j] == 'X') lineX++;
				else if (map[i][j] == 'O') lineY++;
				else if (map[i][j] == '.') emptyCnt++;
				else lineT++;
			}
			if (lineX + lineT == 4){
				xwin = true;
			}else if (lineY + lineT == 4){
				ywin = true;
			}
		}
		if (!(xwin || ywin))
		{
			for (int j=0;j<4;++j)
			{
				lineX = lineY = lineT = 0;
				for (int i=0;i<4;++i)
				{
					if (map[i][j] == 'X') lineX++;
					else if (map[i][j] == 'O') lineY++;
					else if (map[i][j] == '.') emptyCnt++;
					else lineT++;
				}
				if (lineX + lineT == 4){
					xwin = true;
				}else if (lineY + lineT == 4){
					ywin = true;
				}
			}
		}
		if (!(xwin || ywin))
		{
			lineX = lineY = lineT = 0;
			for (int j=0;j<4;++j)
			{
				if (map[j][j] == 'X') lineX++;
				else if (map[j][j] == 'O') lineY++;
				else if (map[j][j] == '.') emptyCnt++;
				else lineT++;
			}
			if (lineX + lineT == 4){
				xwin = true;
			}else if (lineY + lineT == 4){
				ywin = true;
			}
		}
		if (!(xwin || ywin))
		{
			lineX = lineY = lineT = 0;
			for (int j=0;j<4;++j)
			{
				if (map[3-j][j] == 'X') lineX++;
				else if (map[3-j][j] == 'O') lineY++;
				else if (map[3-j][j] == '.') emptyCnt++;
				else lineT++;
			}
			if (lineX + lineT == 4){
				xwin = true;
			}else if (lineY + lineT == 4){
				ywin = true;
			}
		}
		printf("Case #%d: ",caseno);
		if (xwin)
		{
			printf("X won");
		}else if (ywin)
		{
			printf("O won");
		}else if (emptyCnt)
		{
			printf("Game has not completed");
		}else{
			printf("Draw");
		}
		printf("\n");
	}
	return 0;
}