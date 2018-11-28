#include<cstdio>
#include<cstring>
using namespace std;

char mat[10][10];
char ipt[10][10];

bool isHeWin(char ch)
{
	memcpy(mat,ipt,sizeof(ipt));
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(mat[i][j]=='T')
				mat[i][j]=ch;
		}
	}
	if(mat[0][0]==ch&&mat[1][1]==ch&&mat[2][2]==ch&&mat[3][3]==ch)
		return true;
	if(mat[3][0]==ch&&mat[2][1]==ch&&mat[1][2]==ch&&mat[0][3]==ch)
		return true;
	for(int i=0;i<4;i++)
	{
		if(mat[i][0]==ch&&mat[i][1]==ch&&mat[i][2]==ch&&mat[i][3]==ch)
			return true;
		if(mat[0][i]==ch&&mat[1][i]==ch&&mat[2][i]==ch&&mat[3][i]==ch)
			return true;
	}
	return false;
}

int main()
{
	int T,TT;
	scanf("%d",&T);
	TT=T;
	while(T--)
	{
		for(int i=0;i<4;i++)
			scanf("%s",ipt[i]);

		printf("Case #%d: ",TT-T);
		if(isHeWin('X'))
		{
			printf("X won\n");
			continue;
		}

		if(isHeWin('O'))
		{
			printf("O won\n");
			continue;
		}

		bool notover=false;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(ipt[i][j]=='.'){
					notover=true;
					break;
				}
			}
			if(notover)
				break;
		}
		if(notover)
		{
			printf("Game has not completed\n");
			continue;
		} else {
			printf("Draw\n");
		}

	}
	return 0;
}