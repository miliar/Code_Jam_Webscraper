#include <cstdio>

int T;
char A[10][10];
bool Win(char c)
{
	int i,j,s1,s2;
	for(i=1;i<=4;i++)
	{
		s1 = s2 = 0;
		for(j=1;j<=4;j++)
		{
			if(A[i][j] == c || A[i][j] == 'T')	s1++;
			if(A[j][i] == c || A[j][i] == 'T')	s2++;
		}
		if(s1 == 4 || s2 == 4)
			return 1;
	}
	s1 = s2 = 0;
	for(i=1;i<=4;i++)
	{
		if(A[i][i] == c 	|| A[i][i] == 'T')	s1++;
		if(A[i][5-i] == c || A[i][5-i] == 'T')	s2++;
	}
	return s1 == 4 || s2 == 4;
}
void Read()
{
	int i,j,k;
	bool flg;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		flg = false;
		for(j=1;j<=4;j++)
			for(k=1;k<=4;k++)
			{
				scanf(" %c",&A[j][k]);
				if(A[j][k] == '.')
					flg = true;
			}
		printf("Case #%d: ",i);
		if(Win('X'))			puts("X won");
		else if(Win('O'))		puts("O won");
		else if(!flg)			puts("Draw");
		else					puts("Game has not completed");
	}
}
int main()
{
	Read();
	return 0;
}
