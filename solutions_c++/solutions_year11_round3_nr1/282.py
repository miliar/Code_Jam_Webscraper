#include <stdio.h>
#include <string.h>

int R, C, nBCnt;
char Table[100][100];

void Read()
{
	scanf("%d %d", &R, &C);
	nBCnt = 0;
	for(int i = 0; i < R; i++){
		scanf("%s", Table[i]);
		for(int j = 0; j < C; j++)
			if(Table[i][j] == '#')
				nBCnt++;
	}
}

int GetBlurCount(int i, int j)
{
	if(i < 0 || j < 0 || i+1 >= R || j+1 >= C)
		return 0;
	int nCount = 0;
	if(Table[i][j] == '#') nCount++;
	if(Table[i][j+1] == '#') nCount++;
	if(Table[i+1][j] == '#') nCount++;
	if(Table[i+1][j+1] == '#') nCount++;
	return nCount;
}

void MakeRed(int i, int j)
{
	if(i < 0 || j < 0 || i+1 >= R || j+1 >= C)
		return ;
	Table[i][j]='/'; Table[i][j+1]='\\';
	Table[i+1][j]='\\'; Table[i+1][j+1]='/';
}

void Solve()
{
	if(nBCnt%4){
		printf("Impossible\n");
	}else{
		for(int i = 0; i < R-1; i++)
			for(int j = 0; j < C-1; j++){
				if(Table[i][j] == '#'){
					if(GetBlurCount(i,j) == 4){
						MakeRed(i,j);
						nBCnt -= 4;
					}else{
						printf("Impossible\n");
						return ;
					}
				}
			}
			if(nBCnt != 0)
				printf("Impossible\n");
			else{
				for(int i = 0; i < R; i++)
					printf("%s\n", Table[i]);
			}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		Read();
		printf("Case #%d:\n", i);
		Solve();
	}
}
