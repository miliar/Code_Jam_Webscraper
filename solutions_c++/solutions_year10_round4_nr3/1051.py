#include <cstdio>
#include <cstring>

bool cell[102][102], newcell[102][102];
int ntest, nrect;

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		scanf("%d", &nrect);
		memset(cell, 0, sizeof(cell));
		for(int k = 0;k < nrect;++k)
		{
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int i = x1;i < x2 + 1;++i)
				for(int j = y1;j < y2 + 1;++j)
					cell[i][j] = 1;
		}
		int t = 0;
		for(;;++t)
		{
			int cnt = 0;
			for(int i = 0;i < 102;++i)
				for(int j = 0;j < 102;++j)
					cnt += cell[i][j];
			/*printf("--------\n");
			for(int i = 0;i < 10;++i)
				for(int j = 0;j < 10;++j)
					printf("%d%c", cell[i][j], j == 9 ? '\n' : ' ');*/
			if(cnt == 0)
				break;
			for(int i = 0;i < 102;++i)
				for(int j = 0;j < 102;++j)
					if(i > 0 && j > 0)
					{
						newcell[i][j] = cell[i][j];
						if(cell[i][j] && !cell[i - 1][j] && !cell[i][j - 1])
							newcell[i][j] = 0;
						else if(!cell[i][j] && cell[i - 1][j] && cell[i][j - 1])
							newcell[i][j] = 1;
					}
					else
						newcell[i][j] = cell[i][j];
			memcpy(cell, newcell, sizeof(newcell));
		}
		printf("Case #%d: %d\n", test, t);
	}
}
